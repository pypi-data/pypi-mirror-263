# -*- coding: UTF-8 -*-

from pathlib import Path
import h5py

from anndata import AnnData
import anndata as ad
from ykenan_log import Logger

from ._constant_ import path

log = Logger("scLift_util_matrix", is_form_file=False)


def read_adata(file: path) -> AnnData:
    """
    Read AnnData data
    :param file: file path
    :return: AnnData data
    """

    return ad.read(Path(file))


def read_h5(file: path, is_close: bool = False):
    """
    Read AnnData data
    :param file: file path
    :param is_close: file path
    :return: AnnData data
    """
    file = h5py.File(file, 'r')
    keys = file.keys()
    if is_close:
        file.close()
    return keys, file


def save_h5(data: dict, save_file: path, group_name: str = "matrix"):
    h5_dict = dict(data)

    file = h5py.File(f"{str(save_file)}", 'w')
    grp = file.create_group(group_name)

    for key, value in h5_dict.items():
        grp.create_dataset(key, data=value)

    file.close()
