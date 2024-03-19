# -*- coding: UTF-8 -*-

from typing import Optional

import numpy as np
from pandas import DataFrame
from ykenan_log import Logger

from anndata import AnnData
import scanpy as sc

from ._algorithm_ import z_score_marginal, z_score_normalize, adjustment_tf_idf
from scLift.util import to_sparse

log = Logger("scLift_model_preprocessing", is_form_file=False)


def filter_data(
    adata: AnnData,
    min_cells: int = 1,
    min_peaks: int = 1,
    min_peaks_counts: int = 1,
    min_cells_counts: int = 1,
    cell_rate: Optional[float] = None,
    peak_rate: Optional[float] = None,
    is_copy: bool = False,
    is_min_cell: bool = True,
    is_min_peak: bool = False
) -> AnnData:
    """
    Filter scATAC data
    :param adata: scATAC-seq data
    :param min_peaks_counts: Minimum number of counts required for a peak to pass filtering
    :param min_cells: Minimum number of cells expressed required for a peak to pass filtering
    :param min_cells_counts: Minimum number of counts required for a cell to pass filtering
    :param min_peaks: Minimum number of peaks expressed required for a cell to pass filtering
    :param cell_rate: Removing the percentage of cell count in total cell count only takes effect when the min_cells parameter is None
    :param peak_rate: Removing the percentage of peak count in total peak count only takes effect when the min_peaks parameter is None
    :param is_copy: Do you want to deeply copy data
    :param is_min_cell: Whether to screen cells
    :param is_min_peak: Whether to screen peaks
    :return: scATAC-seq data
    """
    log.info("Filter scATAC data")

    if adata.shape[0] == 0:
        log.error("The scATAC data is empty")
        raise ValueError("The scATAC data is empty")

    filter_adata = adata.copy() if is_copy else adata
    cells_count, peaks_count = filter_adata.shape

    if cell_rate is not None:

        if cell_rate <= 0 or cell_rate >= 1:
            log.error("`cell_rate`")
            raise ValueError("")

        _min_cells_ = int(filter_adata.shape[0] * cell_rate)

        if _min_cells_ > 1:
            min_cells = _min_cells_

    if peak_rate is not None:

        if peak_rate <= 0 or peak_rate >= 1:
            log.error("")
            raise ValueError("")

        _min_peaks_ = int(filter_adata.shape[1] * peak_rate)

        if _min_peaks_ > 1:
            min_peaks = _min_peaks_

    log.info(f"min cells: {min_cells}, min peaks: {min_peaks}")
    sc.pp.filter_genes(filter_adata, min_cells=min_cells)
    sc.pp.filter_cells(filter_adata, min_genes=min_peaks)

    # filter peaks and cell
    if is_min_peak:
        sc.pp.filter_genes(filter_adata, min_counts=min_peaks_counts)

    if is_min_cell:
        sc.pp.filter_cells(filter_adata, min_counts=min_cells_counts)
    else:
        sc.pp.filter_cells(filter_adata)

    # judge cells count
    if filter_adata.shape[0] == 0:
        log.error("After screening, the number of cells was 0. Suggest setting the `is_min_peak` parameter to `False` or lowering the `cell_rate` and `peak_rate` parameters to try again")
        return filter_adata

    log.info(f"filter cells {cells_count - filter_adata.shape[0]}, filter peaks {peaks_count - filter_adata.shape[1]}")
    log.debug(f"Size of filtered scATAC data: {filter_adata.shape}")
    return filter_adata


def handle_sc_atac(
    adata: AnnData,
    cell_rate: Optional[float] = None,
    peak_rate: Optional[float] = None
) -> AnnData:
    """
    Preprocessing scATAC data
    :param adata: scATAC-seq data
    :param cell_rate: Removing the percentage of cell count in total cell count
    :param peak_rate: Removing the percentage of peak count in total peak count
    :return: scATAC-seq data
    """
    if adata.shape[0] == 0 or adata.shape[1] == 0:
        log.error("The scATAC data is empty")
        raise ValueError("The scATAC data is empty")

    data = adata.copy()
    data = filter_data(data, cell_rate=cell_rate, peak_rate=peak_rate, is_copy=True)
    # TF-IDF, Z-score
    handle_common(data)
    return data


def handle_feature(
    adata: AnnData,
    cell_anno: DataFrame,
    is_fileter: bool = False,
    scale: float = 10
) -> AnnData:
    """
    Preprocessing cicero gene/chromVAR tf data
    :param scale:
    :param is_fileter:
    :param adata: cicero gene/chromVAR tf data
    :param cell_anno: scATAC-seq data
    :return: cicero gene/chromVAR tf data
    """
    if adata.shape[0] == 0 or cell_anno.shape[0] == 0:
        log.error("The cicero gene data/chromVAR tf or scATAC data is empty")
        raise ValueError("The cicero gene data/chromVAR tf or scATAC data is empty")

    data = adata.copy()
    # Filter and specify order
    atac_obs: DataFrame = cell_anno.copy()
    data = data[list(atac_obs["barcode"]), :]
    # Filter feature
    if is_fileter:
        extreme_value = np.amax(data.X, axis=0) - np.amin(data.X, axis=0)
        value = extreme_value.min() + (extreme_value.max() - extreme_value.min()) / scale
        data = data[:, extreme_value > value]
    # TF-IDF, Z-score
    handle_common(data)
    # update cell information
    data.obs = atac_obs
    return data


def handle_overlap(
    adata: AnnData
) -> None:
    """
    Preprocessing overlap data, Ensure independence for each trait or disease
    :param adata: overlap data
    :return: overlap data
    """
    if adata.shape[0] == 0:
        log.error("The overlap data is empty")
        raise ValueError("The overlap data is empty")
    z_score, _ = z_score_marginal(adata.X, axis=0)
    adata.layers["normalization"] = to_sparse(z_score)


def handle_common(
    adata: AnnData,
    is_marginal: bool = False
) -> None:
    # TF-IDF
    tf_idf_data = adjustment_tf_idf(adata.X, ri_sparse=False)

    # Z-score
    if is_marginal:
        z_score, _ = z_score_marginal(tf_idf_data, axis=1)
    else:
        z_score = z_score_normalize(tf_idf_data)

    adata.layers["normalization"] = z_score
