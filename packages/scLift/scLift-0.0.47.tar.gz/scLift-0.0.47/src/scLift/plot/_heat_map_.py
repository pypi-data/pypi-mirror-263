# -*- coding: UTF-8 -*-

from anndata import AnnData
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.backends.backend_pdf import PdfPages
from PyComplexHeatmap import HeatmapAnnotation, anno_simple, ClusterMapPlotter, anno_label
from pandas import DataFrame
import seaborn as sns
from ykenan_log import Logger

from scLift.util import path

log = Logger("scLift_plot_heat_map", is_form_file=False)


def heatmap_annotation(
    adata: AnnData,
    layer: str = None,
    width: float = 8.0,
    label: str = "value",
    row_name: str = "clusters",
    feature_name: str = None,
    row_anno_label: bool = False,
    col_anno_label: bool = False,
    row_anno_text: bool = False,
    col_anno_text: bool = False,
    row_legend: bool = False,
    col_legend: bool = False,
    row_df_label: bool = False,
    col_df_label: bool = False,
    row_cluster: bool = False,
    col_cluster: bool = False,
    top: float = 0.05,
    right: float = 0.15,
    bottom: float = 0.05,
    left: float = 0.05,
    is_position: bool = False,
    x_name: str = None,
    y_name: str = None,
    cmap: str = "Oranges",
    is_sort: bool = True,
    show: bool = True,
    output: path = None
):
    if output is None and not show:
        log.info(f"At least one of the `output` and `show` parameters is required")
    else:
        # noinspection DuplicatedCode
        fig, ax = plt.subplots(figsize=(width, 8))
        data = adata.copy()

        # judge layers
        if layer is not None:

            if layer not in list(data.layers):
                log.error("The `layer` parameter needs to include in `adata.layers`")
                raise ValueError(f"The `{layer}` parameter needs to include in `adata.layers`")

            data.X = data.layers[layer]

        if is_sort:
            data = data[data.obs.sort_values(row_name).index, data.var.sort_values(feature_name).index]

        # DataFrame
        df: DataFrame = data.to_df()

        if is_position:
            plt.subplots_adjust(left=left, right=1 - right, top=1 - top, bottom=bottom)

        cell_anno: DataFrame = data.obs.copy()

        feature_anno: DataFrame = data.var.copy()

        row_ha = HeatmapAnnotation(
            label=anno_label(cell_anno[row_name], cmap="cmap50", merge=True) if row_anno_label else None,
            Category=anno_simple(
                cell_anno[row_name],
                cmap="cmap50",
                legend=row_legend,
                add_text=row_anno_text,
                text_kws=dict(color="black", rotation=0),
            ),
            axis=0,
            verbose=0,
            label_kws=dict(color="white", rotation=90, horizontalalignment="left")
        )
        col_ha_args = {"rotation": 90}
        col_ha = HeatmapAnnotation(
            label=anno_label(feature_anno[feature_name], cmap="cmap50", merge=True, **col_ha_args) if col_anno_label else None,
            Category=anno_simple(
                feature_anno[feature_name],
                cmap="cmap50",
                add_text=col_anno_text,
                legend=col_legend
            ) if feature_name is not None else None,
            axis=1,
            verbose=0,
            label_side='left',
            label_kws=dict(color="white", rotation=0, horizontalalignment="right")
        )
        """
        It is worth noting here that, `row_cluster_metric="correlation"`,
        When the default parameter `row_cluster_metric` in method `ClusterMapPlotter` is passed into method `distance.pdist`, that is `metric='correlation'`,
        and this method derives from this `https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.distance.pdist.html`,
        it can be inferred that there is a division formula in one step, which may result in the possibility of `NA`.
        For example, in this scATAC-seq data, if there are two or more traits without any intersection, the denominator will appear as zero.
        Therefore, use the `"euclidean"` value for parameter `row_cluster_metric`
        """
        ClusterMapPlotter(
            data=df,
            top_annotation=col_ha if feature_name is not None else None,
            left_annotation=row_ha,
            label=label,
            row_cluster_method="median",
            row_cluster_metric="euclidean",
            col_cluster_method="median",
            col_cluster_metric="euclidean",
            show_rownames=row_df_label,
            show_colnames=col_df_label,
            xticklabels_kws=dict(labelrotation=-75, labelcolor='black', labelsize=10),
            yticklabels_kws=dict(labelrotation=0, labelcolor='black', labelsize=10),
            cmap=cmap,
            xlabel=x_name,
            ylabel=y_name,
            xlabel_kws=dict(color='black', fontsize=15),
            ylabel_kws=dict(color='black', fontsize=15),
            col_cluster=col_cluster,
            row_cluster=row_cluster,
            col_dendrogram=col_cluster,
            row_dendrogram=row_cluster
        )

        # noinspection DuplicatedCode
        if output is not None:

            if output.endswith(".png") or output.endswith(".jpg"):
                plt.savefig(output, dpi=300)
            else:
                output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"

                with PdfPages(output_pdf) as pdf:
                    pdf.savefig(fig)

        if show:
            plt.show()

        plt.close()


def heatmap(
    adata: AnnData,
    output: path = None,
    layer: str = None,
    width: float = 8.0,
    annot: bool = False,
    rotation: float = 65,
    show: bool = True,
    is_cluster: bool = True
) -> None:
    if output is None and not show:
        log.info(f"At least one of the `output` and `show` parameters is required")
    else:
        # noinspection DuplicatedCode
        fig, ax = plt.subplots(figsize=(8, width))
        data = adata.copy()

        # judge layers
        if layer is not None:

            if layer not in list(data.layers):
                log.error("The `layer` parameter needs to include in `adata.layers`")
                raise ValueError("The `layer` parameter needs to include in `adata.layers`")

            data.X = data.layers[layer]

        # DataFrame
        log.info(f"to DataFrame")
        df: DataFrame = data.to_df()
        # seaborn
        heat_map: Axes = sns.clustermap(data=df, square=False, annot=annot, fmt=".1f") \
            if is_cluster else \
            sns.heatmap(data=df, square=False, annot=annot, fmt=".1f")

        if not is_cluster:
            plt.subplots_adjust(left=0.2, bottom=0.3)
            plt.setp(
                heat_map.get_xticklabels(), rotation=65, ha="right", rotation_mode="anchor"
            )
        else:
            plt.setp(heat_map.ax_heatmap.get_xticklabels(), rotation=rotation)

        # noinspection DuplicatedCode
        if output is not None:

            if output.endswith(".png") or output.endswith(".jpg"):
                plt.savefig(output, dpi=300)
            else:
                output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"

                if is_cluster:
                    plt.savefig(output_pdf, dpi=300)
                else:
                    with PdfPages(output_pdf) as pdf:
                        pdf.savefig(fig)

        if show:
            plt.show()

        plt.close()
