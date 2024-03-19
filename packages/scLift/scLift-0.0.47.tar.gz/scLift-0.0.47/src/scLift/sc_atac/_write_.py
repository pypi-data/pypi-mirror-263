# -*- coding: UTF-8 -*-

import os.path

import numpy as np
import pandas as pd
from anndata import AnnData
import scipy.io as scio
from pandas import DataFrame

from ykenan_log import Logger
from ykenan_file import StaticMethod

from scLift.util import path, to_sparse, to_dense
from scLift.util._check_ import check_adata_get

file_method = StaticMethod(is_form_log_file=False)
log = Logger("scLift_scATAC_write", is_form_file=False)


def to_meta(adata: AnnData, dir_path: path, feature_name: str = "peaks.bed"):
    dir_path = str(dir_path)
    file_method.makedirs(dir_path)

    #  Convert dense matrices to sparse matrices
    sparse_matrix = to_sparse(adata.X)
    # write mtx file
    log.info(f"Write mtx file")
    scio.mmwrite(os.path.join(dir_path, 'matrix.mtx'), sparse_matrix.T)

    # Cell annotation
    log.info(f"Write cell annotation")
    cell_info: DataFrame = adata.obs
    cell_info["barcodes"] = adata.obs.index.to_list()
    cell_info.to_csv(os.path.join(dir_path, "annotation.txt"), index=False, sep="\t", lineterminator="\n", encoding="utf-8")

    # barcodes
    log.info(f"Write barcodes")
    barcodes = pd.DataFrame(adata.obs.index.to_list(), columns=["index"])
    barcodes.to_csv(os.path.join(dir_path, "barcodes.tsv"), index=False, header=False, sep="\t", lineterminator="\n", encoding="utf-8")

    # feature
    log.info(f"Write feature")
    feature_info: DataFrame = adata.var
    if feature_name.split(".")[0] == "peaks":
        feature = pd.DataFrame(feature_info.index.to_list(), columns=["index"])
        new_feature = feature["index"].astype(str).str.split("[:-]", expand=True)
        new_feature.to_csv(os.path.join(dir_path, feature_name), index=False, header=False, sep="\t", lineterminator="\n", encoding="utf-8")
    else:
        feature = pd.DataFrame(feature_info.index.to_list(), columns=["index"])
        feature.to_csv(os.path.join(dir_path, feature_name), index=False, header=False, sep="\t", lineterminator="\n", encoding="utf-8")


def to_fragments(
    adata: AnnData,
    fragments: str,
    layer: str = None,
    record_count: int = 100000
) -> None:
    output_path = os.path.dirname(fragments)
    file_method.makedirs(output_path)

    data = check_adata_get(adata=adata, layer=layer).T

    # get group information
    data_obs: DataFrame = data.obs.copy()
    data_var: DataFrame = data.var.copy()

    if "chr" not in data_obs.columns or "start" not in data_obs.columns or "end" not in data_obs.columns:
        log.error("`chr` or `start`or  `end` not in obs column")
        raise ValueError("`chr` or `start` or `end` not in obs column")

    if "barcodes" not in data_var.columns:
        log.error(f"`barcodes` not in obs column")
        raise ValueError(f"`barcodes` not in obs column")

    log.info("Sort chr start")
    data_obs.sort_values(["chr", "start"], inplace=True)
    data = data[data_obs.index, :]
    matrix = to_dense(data.X, is_array=True)

    row_size, col_size = data.shape
    row_range, col_range = range(row_size), range(col_size)
    all_number: int = row_size * col_size
    log.info(f"Get size {row_size, col_size} ==> {all_number}")

    # Convert to dictionary
    barcodes_dict: dict = dict(zip(list(col_range), data_var.index))
    peaks_dict: dict = dict(zip(list(row_range), zip(data_obs["chr"], data_obs["start"], data_obs["end"])))

    count = 0

    log.info("Sort write info")
    with open(fragments, mode="w", encoding="utf-8", newline="\n") as f:
        for value in np.nditer(matrix):

            if count >= record_count and count % record_count == 0:
                log.info(f"Processed {count} lines, completed {round(count / all_number, 4) * 100} %")

            # index
            row_index = count // col_size
            col_index = count % col_size
            # info
            peaks = peaks_dict[row_index]
            barcodes = barcodes_dict[col_index]
            f.write(f"{peaks[0]}\t{peaks[1]}\t{peaks[2]}\t{barcodes}\t{value}\n")
            count += 1
