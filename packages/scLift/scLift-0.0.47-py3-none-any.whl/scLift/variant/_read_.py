# -*- coding: UTF-8 -*-

from typing import Optional, Tuple

import numpy as np
import pandas as pd
from anndata import AnnData
from pandas import DataFrame

from ykenan_log import Logger
from ykenan_file import StaticMethod

from scLift.util import path, collection, to_sparse, list_duplicate_set

log = Logger("scLift_variant_read", is_form_file=False)


def read_variants(
    base_path: Optional[path] = None,
    files: Optional[collection] = None,
    labels: Optional[dict] = None
) -> Tuple[dict, DataFrame]:
    """
    Read variant file set
    :param base_path: Path for storing mutation trait data
    :param files: Collection of mutation trait data
    :param labels:
    :return: AnnData
    """
    log.info("Read variants file information")
    variant_columns: list = ["id", "chr", "position", "rsId", "pp"]

    results: dict = {}

    # get files
    static_method = StaticMethod("read_variants", is_form_log_file=False)
    file_size: int = 0

    if files is not None:
        file_size: int = len(list(files))

    if base_path is None and file_size == 0:
        log.error("At least one of the `base_path` and `files` parameters has a parameter")
        raise ValueError("At least one of the `base_path` and `files` parameters has a parameter")

    new_files = []

    if isinstance(base_path, path):
        new_files = static_method.get_files_path(base_path)

    # read file
    for variant_file in new_files:
        variant = pd.read_table(variant_file, header=0, index_col=None)
        columns = variant.columns

        if not set(variant_columns).issubset(set(columns)):
            log.error(f"The column name of the {variant_file} file needs to include {variant_columns}")
            raise ValueError(f"The column name of the {variant_file} file needs to include {variant_columns}")

        key: str = str(list(variant["id"])[0])
        results.update({key: variant[variant_columns]})

    log.info("Read variants file finish")
    log.info("handle variants file")
    # concat files
    results_info = pd.concat(list(results.values()), axis=0)
    results_info.reset_index()

    # format trait information
    pp_sum: DataFrame = results_info.groupby("id", as_index=False)["pp"].sum()
    pp_sum.columns = ["id", "pp_sum"]
    pp_mean = results_info.groupby("id", as_index=False)["pp"].mean()
    pp_mean.columns = ["id", "pp_mean"]
    pp_size = results_info.groupby("id", as_index=False)["rsId"].count()
    pp_size.columns = ["id", "count"]

    merge_info = pp_sum.merge(pp_mean, on="id", how="inner")
    trait_info: DataFrame = merge_info.merge(pp_size, on="id", how="inner")
    trait_info.index = trait_info["id"].astype(str)

    # format variant data
    variant_mdata_dict: dict = {}

    for key in trait_info.index:
        variant_content: DataFrame = results[key]
        # format variant information
        variant_content["variant_id"] = variant_content["chr"].astype(str) + ":" + variant_content["position"].astype(str) + ":" + variant_content["rsId"].astype(str)
        variant_info = variant_content[["variant_id", "chr", "position", "rsId"]]
        variant_info_index = list(variant_info["variant_id"].astype(str))
        # set index
        variant_content["variant_id_index"] = list_duplicate_set(variant_info_index)
        variant_info.index = variant_content["variant_id_index"]
        # format trait-variant data
        variant_list: list = list(variant_content["variant_id_index"])
        trait_name = variant_content["id"][0]
        trait: DataFrame = trait_info[trait_info["id"] == trait_name]
        log.info(f"{len(variant_mdata_dict) + 1}: Trait/Disease {trait_name}")

        # format dict
        variant_dict: dict = dict(zip(variant_list, range(len(variant_list))))

        shape = (len(variant_list), 1)

        log.info(f"Create trait-variant matrix shape is {shape}")
        matrix = np.zeros(shape)

        for variant_id_index, pp in zip(variant_content["variant_id_index"], variant_content["pp"]):
            matrix[variant_dict[variant_id_index], 0] = pp

        # format AnnData
        variant_adata = AnnData(to_sparse(matrix), var=trait, obs=variant_info)
        variant_mdata_dict.update({trait_name: variant_adata})

    if labels is not None:
        trait_info["labels"] = labels
    else:
        trait_info["labels"] = trait_info["id"]

    return variant_mdata_dict, trait_info
