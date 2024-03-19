# -*- coding: UTF-8 -*-

import os

import numpy as np
import pandas as pd
from anndata import AnnData
from pandas import DataFrame
from ykenan_log import Logger

from ._constant_ import path
from ._matrix_ import to_dense, to_sparse

from scLift.sc_atac import to_meta, read_sc_atac

log = Logger("scLift_util_adata_merge", is_form_file=False)


def sc_adata_merge(input_path: path, output_path: path, about_cell_number: int = 20000):
    dir_names: list = os.listdir(input_path)

    # Number of cells per sample
    each_cell_number = int(about_cell_number / len(dir_names))

    sc_atac_list = []
    sc_atac_obs: DataFrame = pd.DataFrame(columns=['barcode', 'barcodes', 'UMAP1', 'UMAP2', 'clusters'])
    sc_atac_var: DataFrame = pd.DataFrame()

    for dir_name in dir_names:
        log.info(f"Start {dir_name}")
        # read
        sc_atac_adata = read_sc_atac(
            base_path=os.path.join(input_path, dir_name, "metadata"),
            annotation_file=os.path.join(input_path, dir_name, "metadata", "annotation.txt")
        )
        sc_atac_var = sc_atac_adata.var

        sc_data = to_dense(sc_atac_adata.X)
        # calculate sum
        sc_data_sum = sc_data.sum(axis=1)
        sc_data_sum_sort = np.sort(sc_data_sum, axis=0)
        sc_data_sum_value = np.array(sc_data_sum_sort).flatten()[-each_cell_number]
        # filter
        new_sc_atac = sc_atac_adata[sc_data_sum >= sc_data_sum_value, :]
        sc_atac_list.append(to_dense(new_sc_atac.X, is_array=True))
        sc_atac_obs = pd.concat((sc_atac_obs, new_sc_atac.obs))

    adata = AnnData(to_sparse(np.concatenate(sc_atac_list, axis=0)), obs=sc_atac_obs, var=sc_atac_var)
    to_meta(adata, output_path)
