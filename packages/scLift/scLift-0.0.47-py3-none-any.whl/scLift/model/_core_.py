# -*- coding: UTF-8 -*-

import os.path
from typing import Optional, Tuple

import numpy as np
import pandas as pd
import scvi

from anndata import AnnData
from pandas import DataFrame
from scipy import stats

from ykenan_file import StaticMethod
from ykenan_log import Logger

from ._algorithm_ import (
    RandomWalk,
    adata_group,
    adata_map_df,
    tsne_data,
    symmetric_scale,
    cluster_score,
    mutual_knn,
    umap_data,
    davies_bouldin,
    euclidean_distances,
    adjustment_tf_idf,
    z_score_normalize,
    k_means
)

from scLift.plot import (
    scatter_atac,
    scatter_trait,
    communities_graph,
    violin_trait,
    box_trait,
    bar_trait,
    scatter_base,
    barcode_trait,
    heatmap_annotation,
    kde,
    pie_trait
)

from scLift.util import to_sparse, number, path, to_dense, get_index, matrix_data

file_method = StaticMethod("scLift_model_core", is_form_log_file=False)
log = Logger("scLift_model_core", is_form_file=False)


def overlap(regions: DataFrame, variants: DataFrame) -> DataFrame:
    log.info("start overlap variant information")
    columns = ['variant_id', 'index', 'chr', 'position', 'rsId', 'chr_a', 'start', 'end']

    if regions.shape[0] == 0 or variants.shape[0] == 0:
        log.warn("Data is empty.")
        return pd.DataFrame(columns=columns)

    regions = regions.rename_axis("index")
    regions = regions.reset_index()
    # sort
    regions_sort = regions.sort_values(["chr", "start", "end"])[["index", "chr", "start", "end"]]
    variants_sort = variants.sort_values(["chr", "position"])[["variant_id", "chr", "position", "rsId"]]

    # Intersect and Sort
    chr_keys: list = list(set(regions_sort["chr"]).intersection(set(variants_sort["chr"])))
    chr_keys.sort()

    variants_chr_type: dict = {}
    variants_position_list: dict = {}

    # Cyclic region chromatin
    for chr_key in chr_keys:
        # variant chr information
        sort_chr_regions_chr = variants_sort[variants_sort["chr"] == chr_key]
        variants_chr_type.update({chr_key: sort_chr_regions_chr})
        variants_position_list.update({chr_key: list(sort_chr_regions_chr["position"])})

    variants_overlap_info_list: list = []

    log.info("Start adding variants to each region")

    for index, chr_a, start, end in zip(regions_sort["index"], regions_sort["chr"], regions_sort["start"], regions_sort["end"]):

        # judge chr
        if chr_a in chr_keys:
            # get chr variant
            variants_chr_type_position_list = variants_position_list[chr_a]
            # judge start and end position
            if start <= variants_chr_type_position_list[-1] and end >= variants_chr_type_position_list[0]:
                # get index
                start_index = get_index(start, variants_chr_type_position_list)
                end_index = get_index(end, variants_chr_type_position_list)

                # Determine whether it is equal, Equality means there is no overlap
                if start_index != end_index:
                    start_index = start_index if isinstance(start_index, number) else start_index[1]
                    end_index = end_index + 1 if isinstance(end_index, number) else end_index[1]

                    if start_index > end_index:
                        log.error("The end index in the region is greater than the start index.")
                        raise IndexError("The end index in the region is greater than the start index.")

                    variants_chr_type_chr_a = variants_chr_type[chr_a]
                    # get data
                    variants_overlap_info: DataFrame = variants_chr_type_chr_a[start_index:end_index].copy()
                    variants_overlap_info["index"] = index
                    variants_overlap_info["chr_a"] = chr_a
                    variants_overlap_info["start"] = start
                    variants_overlap_info["end"] = end
                    variants_overlap_info_list.append(variants_overlap_info)

    log.info("end overlap variant information")
    # merge result
    if len(variants_overlap_info_list) > 0:
        overlap_data: DataFrame = pd.concat(variants_overlap_info_list, axis=0)
    else:
        log.info("Overlap is empty.")
        return pd.DataFrame(columns=columns)

    return overlap_data


def overlap_sum(regions: AnnData, variants: dict, trait_info: DataFrame) -> AnnData:
    """
    Overlap regional data and mutation data and sum the PP values of all mutations in a region as the values for that region
    :param regions: region data
    :param variants: variant data
    :param trait_info: trait information
    :return: overlap data
    """

    # Unique feature set
    label_all = list(regions.var.index)
    # Peak number
    label_all_size: int = len(label_all)

    # trait information
    trait_names: list = list(trait_info["id"])

    matrix = np.zeros((label_all_size, len(trait_names)))

    for trait_name in trait_names:
        variant: AnnData = variants[trait_name]
        index: int = trait_names.index(trait_name)
        log.info(f"Start {index + 1} trait/disease {trait_name}")

        # handle overlap data
        overlap_info: DataFrame = overlap(regions.var, variant.obs)

        if overlap_info.shape[0] == 0:
            continue

        overlap_info.rename({"index": "label"}, axis="columns", inplace=True)
        overlap_info.reset_index(inplace=True)
        overlap_info["region_id"] = overlap_info["chr"].astype(str) + ":" + overlap_info["start"].astype(str) + "-" + overlap_info["end"].astype(str)

        # get region
        region_info = overlap_info.groupby("region_id", as_index=False)["label"].first()
        region_info.index = region_info["label"].astype(str)
        label: list = list(region_info["label"])

        # Mutation information with repetitive features
        label_size: int = len(label)
        # Define a matrix
        log.info("Sum each region")

        for j in range(label_size):

            # Determine whether the features after overlap exist, In other words, whether there is overlap in this feature
            if label[j] in label_all:
                # get the index of label
                label_index = label_all.index(label[j])
                overlap_info_region = overlap_info[overlap_info["label"] == label[j]]
                # sum value
                overlap_variant = variant[list(overlap_info_region["variant_id_index"]), :]
                matrix[label_index, index] = overlap_variant.X.sum(axis=0)

    overlap_adata = AnnData(to_sparse(matrix), var=trait_info, obs=regions.var)
    overlap_adata.uns["trait_info"] = trait_info
    return overlap_adata


def group_heatmap(
    adata: AnnData,
    layer: str = None,
    feature_name: str = "feature",
    clusters: str = "clusters",
    width: float = 8.0,
    plot_output: str = None,
    show: bool = True
) -> None:
    # The relationship between cluster and trait
    adata_cluster: AnnData = adata_group(adata, clusters, layer=layer)

    # create path
    new_path: path = os.path.join(plot_output, feature_name) if plot_output is not None else None
    file_method.makedirs(new_path)

    # plot
    heatmap_annotation(
        adata_cluster.T,
        row_name="labels",
        feature_name=clusters,
        width=width,
        label="Mean TRS",
        row_legend=True,
        row_cluster=True,
        col_cluster=True,
        row_df_label=True,
        col_df_label=True,
        x_name="Cell type",
        y_name="Trait",
        show=show,
        output=os.path.join(new_path, f"{layer}_cluster_trait_mean.pdf") if new_path is not None else None
    )
    heatmap_annotation(
        adata_cluster.T,
        layer="matrix_sum",
        row_name="labels",
        feature_name=clusters,
        width=width,
        label="Sum TRS",
        row_legend=True,
        row_cluster=True,
        col_cluster=True,
        row_df_label=True,
        col_df_label=True,
        x_name="Cell type",
        y_name="Trait",
        show=show,
        output=os.path.join(new_path, f"{layer}_cluster_trait_sum.pdf") if new_path is not None else None
    )
    heatmap_annotation(
        adata_cluster.T,
        layer="matrix_max",
        row_name="labels",
        feature_name=clusters,
        width=width,
        label="Max TRS",
        row_legend=True,
        row_cluster=True,
        col_cluster=True,
        row_df_label=True,
        col_df_label=True,
        x_name="Cell type",
        y_name="Trait",
        show=show,
        output=os.path.join(new_path, f"{layer}_cluster_trait_max.pdf") if new_path is not None else None
    )
    heatmap_annotation(
        adata_cluster.T,
        layer="matrix_min",
        row_name="labels",
        feature_name=clusters,
        width=width,
        label="Min TRS",
        row_legend=True,
        row_cluster=True,
        col_cluster=True,
        row_df_label=True,
        col_df_label=True,
        x_name="Cell type",
        y_name="Trait",
        show=show,
        output=os.path.join(new_path, f"{layer}_cluster_trait_min.pdf") if new_path is not None else None
    )


def map_df_plot(
    adata: AnnData,
    layer: str = None,
    trait_cluster_map: dict = None,
    clusters: str = "clusters",
    feature_name: str = "feature",
    width: float = 16,
    y_name: str = "value",
    column: str = "value",
    plot_output: path = None
) -> None:
    # create path
    new_path: path = os.path.join(plot_output, f"{feature_name}_{layer}" if layer is not None else feature_name) if plot_output is not None else None
    file_method.makedirs(new_path)
    # create data
    adata_df: DataFrame = adata_map_df(adata, column=column, layer=layer)
    # violin plot
    violin_trait(
        adata_df,
        y_name=y_name,
        value=column,
        width=width,
        clusters=clusters,
        title=feature_name,
        output=new_path if plot_output is not None else None
    )
    # box plot
    box_trait(
        adata_df,
        y_name=y_name,
        value=column,
        clusters=clusters,
        width=width,
        title=feature_name,
        output=new_path if plot_output is not None else None
    )
    # rank plot
    barcode_trait(
        adata_df,
        sort_column=column,
        clusters=clusters,
        title=feature_name,
        output=new_path if plot_output is not None else None
    )
    # pie plot
    if trait_cluster_map is not None:
        pie_trait(
            adata_df,
            trait_cluster_map=trait_cluster_map,
            title=feature_name,
            output=new_path if plot_output is not None else None
        )


def rate_bar_plot(
    adata: AnnData,
    layer: str = None,
    feature_name: str = "feature",
    column: str = "value",
    clusters: str = "clusters",
    width: float = 16,
    plot_output: path = None,
    show: bool = True
) -> None:
    # create path
    new_path: path = os.path.join(plot_output, f"{feature_name}_{layer}") if plot_output is not None else None
    file_method.makedirs(new_path)
    # create data
    adata_df: DataFrame = adata_map_df(adata, column=column, layer=layer)
    clusters_group = adata_df.groupby(["id", "clusters"], as_index=False).size()
    value_group = adata_df.groupby(["id", "clusters", "value"], as_index=False).size()
    new_value_group = value_group.merge(clusters_group, on=["id", "clusters"], how="left")

    # Completion
    id_list = list(set(new_value_group["id"]))
    clusters_list = list(set(new_value_group["clusters"]))
    value_list = [1.0, 0.0]
    total_size = len(id_list) * len(clusters_list) * len(value_list)

    if total_size != new_value_group.shape[0]:
        new_value_group_index = new_value_group["id"].astype(str) + "_" + new_value_group["clusters"].astype(str) + "_" + new_value_group["value"].astype(int).astype(str)
        new_value_group.index = new_value_group_index
        new_value_group_index = list(new_value_group_index)

        trait_df: DataFrame = pd.DataFrame(columns=new_value_group.columns)

        # [id clusters  value  size_x  size_y]
        for _id_ in id_list:
            for _clusters_ in clusters_list:
                for _value_ in value_list:

                    # At this point, it means that the enrichment effect is 1, while the non enrichment effect is 0, so it does not exist during grouping and needs to be added here
                    if (_id_ + "_" + _clusters_ + "_" + str(int(_value_))) not in new_value_group_index:
                        exit_value = 0 if int(_value_) == 1 else 1
                        exit_index = _id_ + "_" + _clusters_ + "_" + str(exit_value)
                        exit_data = new_value_group[new_value_group.index == exit_index]
                        exit_data.loc[exit_index, "value"] = _value_
                        exit_data.loc[exit_index, "size_x"] = 0
                        exit_data.index = [_id_ + "_" + _clusters_ + "_" + str(int(_value_))]
                        trait_df = pd.concat((trait_df, exit_data), axis=0)

        new_value_group = pd.concat((trait_df, new_value_group), axis=0)

    new_value_group["rate"] = new_value_group["size_x"] / new_value_group["size_y"]

    bar_trait(
        trait_df=new_value_group,
        value="rate",
        clusters=clusters,
        title=feature_name,
        width=width,
        output=new_path if plot_output is not None else None,
        show=show
    )


def calculate_init_score(
    atac_adata: AnnData,
    da_peaks_adata: AnnData,
    overlap_adata: AnnData
) -> AnnData:
    if "trait_info" not in list(overlap_adata.uns.keys()):
        log.error("The description of trait `trait_info` is not in `overlap_data.uns.keys()`")
        raise ValueError("The description of trait `trait_info` is not in `overlap_data.uns.keys()`")

    # Processing data
    latent = to_dense(atac_adata.obsm["latent"])
    overlap_matrix = to_dense(overlap_adata.X)
    weight_bf = to_dense(da_peaks_adata.X)

    # handler
    weight_bf_tf_idf = to_dense(adjustment_tf_idf(weight_bf))
    weight_bf_normalize = z_score_normalize(weight_bf_tf_idf)
    da_peaks_adata.layers["bf_normalize"] = to_sparse(weight_bf_normalize)

    log.info("Start calculate leiden cluster init_score")
    cluster_weight: matrix_data = weight_bf_normalize @ overlap_matrix
    da_peaks_adata.obsm["cluster_weight"] = to_sparse(cluster_weight)

    log.info("Start set weight")
    anno_info = atac_adata.obs
    cell_weight = np.zeros((atac_adata.shape[0], cluster_weight.shape[1]))

    for cluster in da_peaks_adata.obs_names:
        cell_weight[anno_info["k_clusters"] == cluster, :] = to_dense(da_peaks_adata[cluster, :].obsm["cluster_weight"], is_array=True).flatten()

    cell_weight = symmetric_scale(cell_weight, scale=np.abs(cell_weight).mean(axis=0), axis=0)

    init_score = latent @ weight_bf_normalize.T @ overlap_matrix
    init_score_weight = np.multiply(init_score, cell_weight)

    init_score_weight_scale = symmetric_scale(init_score_weight, scale=np.abs(init_score_weight).mean(axis=0), axis=0)
    init_score_weight_adata = AnnData(to_sparse(init_score_weight_scale), var=overlap_adata.uns["trait_info"], obs=atac_adata.obs)
    init_score_weight_adata.layers["init_score"] = to_sparse(init_score)
    init_score_weight_adata.layers["init_score_weight"] = to_sparse(init_score_weight)
    return init_score_weight_adata


def perform_cluster_type(
    matrix: matrix_data,
    cell_anno: DataFrame,
    plot_output: path = None,
) -> Tuple[dict, Tuple[matrix_data, matrix_data]]:
    tmp_cell_anno = cell_anno.copy()
    # tSNE
    tsne_coordinate = tsne_data(matrix)
    tmp_cell_anno[f"tsne1"] = tsne_coordinate[:, 0]
    tmp_cell_anno[f"tsne2"] = tsne_coordinate[:, 1]
    # cluster plot
    scatter_base(tmp_cell_anno, "clusters", right=0.75, columns=(f"tsne1", f"tsne2"), output=f"{plot_output}_tsne")

    umap_coordinate = tsne_coordinate.copy()
    try:
        umap_coordinate = umap_data(matrix)
        tmp_cell_anno[f"UMAP1"] = umap_coordinate[:, 0]
        tmp_cell_anno[f"UMAP2"] = umap_coordinate[:, 1]
        scatter_base(tmp_cell_anno, "clusters", right=0.75, columns=(f"UMAP1", f"UMAP2"), output=f"{plot_output}_umap")
    except Exception as e:
        log.error(f"{str(e.args)}")

    # cluster method
    k_means_score = cluster_score(matrix, cell_anno["clusters"], method="k_means")
    spectral_score = cluster_score(matrix, cell_anno["clusters"], method="spectral")
    return {"k_means": k_means_score, "spectral": spectral_score}, (tsne_coordinate, umap_coordinate)


def cell_trait_related_score(
    adata: AnnData,
    init_status: AnnData,
    mutual_knn_k: int = 50,
    gamma: float = 0.05,
    stationary_cutoff: float = 1e-05,
    p: int = 2
) -> Tuple[AnnData, AnnData]:
    # data
    latent = adata.obsm["latent"]
    cell_anno = adata.obs

    # euclidean distances
    ed_data = euclidean_distances(latent)
    ed_scale_data = symmetric_scale(ed_data, ed_data.mean(axis=1), axis=1)

    log.info("Start affinity matrix")
    distances = to_dense(ed_scale_data, is_array=True)
    affinity_data = stats.gamma.pdf(distances, a=1, scale=1)
    cell_affinity = symmetric_scale(affinity_data, affinity_data.mean(axis=1), axis=1)

    # Define KNN network
    cell_mutual_knn = mutual_knn(cell_affinity, mutual_knn_k)

    # cell-cell graph
    cc_data: AnnData = AnnData(to_sparse(cell_mutual_knn), var=cell_anno[['barcode', 'clusters', "k_clusters"]], obs=cell_anno[['barcode', 'clusters', "k_clusters"]])
    cc_data.layers["cell_affinity"] = to_sparse(cell_affinity)
    cc_data.layers["distances"] = to_sparse(ed_data)
    cc_data.layers["distances_scale"] = to_sparse(ed_scale_data)

    # DBI
    cc_data.uns["DBI"] = davies_bouldin(cell_affinity, cell_anno["k_clusters"])

    # random walk
    random_walk: RandomWalk = RandomWalk(
        cc_adata=cc_data,
        init_status=init_status,
        gamma=gamma,
        stationary_cutoff=stationary_cutoff,
        p=p
    )
    random_walk.run_core()
    random_walk.run_random()
    random_walk.run_none()
    random_walk.run_enrichment()
    trs = random_walk.trs_data

    return trs, cc_data


def poisson_vi(adata: AnnData, model_dir: Optional[path] = None) -> AnnData:
    log.info("Start PoissonVI")
    # PoissonVI, Binarization
    scvi.data.reads_to_fragments(adata)

    # PoissonVI
    scvi.external.POISSONVI.setup_anndata(adata, layer="fragments")
    model = scvi.external.POISSONVI(adata)
    model.train()

    if model_dir is not None:
        file_method.makedirs(model_dir)
        model.save(model_dir, overwrite=True)

    # latent space
    latent = model.get_latent_representation()
    adata.obsm["latent"] = latent

    # cluster
    cluster_types = k_means(latent, latent.shape[1])
    adata.obs["k_clusters"] = cluster_types

    # differential peak
    da_peaks = model.differential_accessibility(adata, groupby="k_clusters", two_sided=False)
    adata.uns["da_peaks"] = da_peaks
    da_peaks.reset_index(inplace=True)
    da_peaks_info = da_peaks[["index", "bayes_factor", "emp_prob1", "group1"]]
    da_peaks_info.loc[:, "group1"] = da_peaks_info["group1"].astype(str)

    clusters = list(set(list(cluster_types)))
    clusters.sort()
    adata.uns["info"] = {
        "model_dir": model_dir,
        "cluster_size": len(clusters)
    }
    peaks_info = adata.var.copy()
    peaks_info["index"] = peaks_info.index

    matrix_bf = np.zeros((len(clusters), adata.shape[1]))
    matrix_ep1 = np.zeros((len(clusters), adata.shape[1]))

    for i in range(len(clusters)):
        cluster_info = da_peaks_info[da_peaks_info["group1"] == clusters[i]]
        cluster_info = pd.merge(left=peaks_info, right=cluster_info, left_on="index", right_on="index", how="left")
        matrix_bf[i, :] = cluster_info["bayes_factor"]
        matrix_ep1[i, :] = cluster_info["emp_prob1"]

    log.info("End PoissonVI")

    obs = pd.DataFrame(clusters, columns=["id"])
    obs.index = obs["id"].astype(str)
    da_peaks_adata = AnnData(to_sparse(matrix_bf), obs=obs, var=adata.var)
    da_peaks_adata.layers["emp_prob1"] = matrix_ep1
    return da_peaks_adata


def data_plot(
    adata: AnnData,
    init_score: AnnData,
    cc_data: AnnData,
    trs: AnnData,
    plot_output: str,
    plot_columns: Tuple[str, str] = ("UMAP1", "UMAP2"),
    width: float = 8
):
    # scatter
    scatter_atac(adata, output=os.path.join(plot_output, "scATAC_cluster.pdf"), columns=plot_columns)

    kde(init_score, axis=0, layer="init_score", title="Initial score (source)", output=os.path.join(plot_output, "init_score_source_kde"))
    kde(init_score, axis=0, title="Initial score (symmetric scale)", output=os.path.join(plot_output, "init_score_scale_kde"))

    # Display of Heat Map and Violin Map
    group_heatmap(adata=init_score, feature_name="init_score", plot_output=plot_output)
    map_df_plot(adata=init_score, feature_name="init_score", y_name="Initial score", column="value", plot_output=plot_output)
    # plot
    file_method.makedirs(os.path.join(plot_output, "init_score"))
    scatter_trait(init_score, title="Initial", bar_label="Initial score", output=os.path.join(plot_output, "init_score"), columns=plot_columns)

    # heatmap
    heatmap_annotation(
        cc_data,
        layer="cell_affinity",
        feature_name="clusters",
        row_legend=True,
        row_anno_label=True,
        col_anno_label=True,
        output=os.path.join(plot_output, "cc_heatmap.png")
    )
    heatmap_annotation(
        cc_data,
        feature_name="clusters",
        row_legend=True,
        row_anno_label=True,
        col_anno_label=True,
        output=os.path.join(plot_output, "cc_heatmap_mknn.png")
    )

    # Cell-cell network
    communities_graph(adata=cc_data, labels=adata.obs["clusters"], output=os.path.join(plot_output, "cc_graph"))

    # Data distribution
    kde(trs, layer="trait_cell_source", axis=0, title="Trait-cell type (source)", output=os.path.join(plot_output, "trait_cell_source_kde"))
    kde(trs, layer="trait_cell_scale", axis=0, title="Trait-cell type (symmetric scale)", output=os.path.join(plot_output, "trait_cell_scale_kde"))

    trs_layers: list = list(trs.layers)

    # plot
    file_method.makedirs(os.path.join(plot_output, "trait_cell"))
    scatter_trait(trs, output=os.path.join(plot_output, "trait_cell"), title="", layers=trs_layers, columns=plot_columns)

    # Display of Heat Map and Violin Map
    for layer in trs_layers:
        group_heatmap(adata=trs, layer=layer, feature_name="heatmap", plot_output=plot_output)
        map_df_plot(adata=trs, layer=layer, feature_name="cell", y_name="Cell score", column="value", width=width, plot_output=plot_output)

    rate_bar_plot(adata=trs, feature_name="enrichment", layer="trait_cell_enrichment", width=width, column="value", plot_output=plot_output)

    # Data distribution plot
    kde(adata, title="scATAC-seq (source)", output=f"{plot_output}/kde_scATAC_source.pdf")
    kde(adata, layer="fragments", title="scATAC-seq (fragments)", output=f"{plot_output}/kde_scATAC_fragments.pdf")
    # distances
    kde(cc_data, layer="distances", title="distances", output=os.path.join(plot_output, "distances_atac_kde"))
    kde(cc_data, layer="distances_scale", title="distances_scale", output=os.path.join(plot_output, "distances_scale_atac_kde"))
