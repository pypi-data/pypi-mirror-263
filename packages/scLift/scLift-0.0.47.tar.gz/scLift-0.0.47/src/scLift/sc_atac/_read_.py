# -*- coding: UTF-8 -*-

import os
from typing import Tuple

import h5py
import numpy as np
import pandas as pd
from anndata import AnnData
from pandas import DataFrame
from scipy.io import mmread
from ykenan_log import Logger

from scLift.util import path, to_sparse
from scanpy import read_10x_h5

log = Logger("scLift_scATAC_read", is_form_file=False)


def handle_file_data_cell(
    file: path,
    barcode_split_character: str = '-',
    on_barcode_split_character: str = None,
    is_transpose: bool = True,
    cluster_anno_file: path = None
) -> Tuple[DataFrame, DataFrame]:
    if file is None:
        log.error("File cannot be empty")
        raise ValueError("File cannot be empty")

    if on_barcode_split_character is None:
        on_barcode_split_character = barcode_split_character

    data = pd.read_table(file, header=0)
    data = data.T if is_transpose else data
    # format barcodes information
    log.info("handle cells information")
    cell_annot = pd.DataFrame(data=np.matrix(data.index).T, columns=["barcodes"])
    content_split_size = len(str(list(data.index)[0]).split(barcode_split_character))

    if content_split_size == 1:
        log.info(f"Barcode does not contain a separator `{barcode_split_character}`")
        cell_annot["barcode"] = cell_annot["barcodes"]
    else:
        cell_annot: DataFrame = cell_annot["barcodes"].astype('str').str.split(barcode_split_character, expand=True)
        cell_annot.columns = ["barcode", "batch_id"]
        cell_annot["barcodes"] = cell_annot["barcode"].astype(str) + on_barcode_split_character + cell_annot["batch_id"].astype(str)

    # add annotation file
    if cluster_anno_file is not None:
        cell_annot = barcodes_add_anno(cluster_anno_file, cell_annot)

    cell_annot.index = cell_annot["barcode"].astype(str)
    return cell_annot, data


def read_info_by_matrix(
    file: path,
    cluster_anno_file: path = None,
    column_name: str = "feature",
    is_transpose: bool = True,
    barcode_split_character: str = '-',
    on_barcode_split_character: str = None
) -> AnnData:
    """
    Read the feature matrix file
    :param cluster_anno_file:
    :param on_barcode_split_character:
    :param file: Feature score file with row and column names
    :param column_name: feature
    :param is_transpose: Whether transpose is required to read the matrix file, default to True
    :param barcode_split_character: A barcode separated character symbol
    :return: AnnData
    """

    # cells information
    cell_annot, data = handle_file_data_cell(
        file=file,
        barcode_split_character=barcode_split_character,
        on_barcode_split_character=on_barcode_split_character,
        is_transpose=is_transpose,
        cluster_anno_file=cluster_anno_file
    )

    # format gene information
    log.info("handle features information")
    features = pd.DataFrame(data=np.matrix(data.columns).T, columns=[column_name])
    features.index = features[column_name].astype(str)

    return AnnData(to_sparse(data.values), var=features, obs=cell_annot)


def barcodes_add_anno(annotation_file: path, cell_annot: DataFrame) -> DataFrame:
    log.info("Add annotation file")
    # add annotation file
    cell_annotation_file: DataFrame = pd.read_table(annotation_file, sep="\t", header=0, index_col=None)

    # judge column
    if "clusters" not in list(cell_annotation_file.columns):
        log.error("The comment file must contain a column name with `clusters`")
        raise ValueError("The comment file must contain a column name with `clusters`")

    if "barcodes" not in list(cell_annotation_file.columns):
        log.error("The comment file must contain a column name with `barcodes`")
        raise ValueError("The comment file must contain a column name with `barcodes`")

    if "barcodes" not in list(cell_annot.columns):
        log.error("The cell_annot must contain a column name with `barcodes`")
        raise SyntaxError("The cell_annot must contain a column name with `barcodes`")

    cell_annot = cell_annot.merge(cell_annotation_file, on="barcodes", how="inner")

    if "clusters" not in list(cell_annot.columns):
        cell_annot = cell_annot.rename(columns={"clusters_y": "barcode"})

    # nan set unknown
    cell_annot.loc[cell_annot["clusters"].isna(), 'clusters'] = "unknown"

    if "barcode" not in list(cell_annot.columns):
        cell_annot = cell_annot.rename(columns={"barcode_x": "barcode"})

    cell_annot.index = cell_annot["barcode"].astype(str)
    return cell_annot


def read_barcodes_file(
    barcodes_path: path,
    barcode_split_character: str = '-',
    annotation_file: path = None,
) -> DataFrame:
    log.info("handle cells information")
    # read file
    cell_annot = pd.read_csv(barcodes_path, header=None, index_col=None)
    content_split_size = len(str(cell_annot[0][1]).split(barcode_split_character))

    if content_split_size == 1:
        log.info(f"Barcode does not contain a separator `{barcode_split_character}`")

    # judge
    if cell_annot.shape[0] != np.unique(cell_annot[0]).size:
        log.error("Barcodes cannot have duplicate barcodes in the barcodes file")
        raise ValueError("Barcodes cannot have duplicate barcodes in the barcodes file")

    if barcode_split_character is None or content_split_size == 1:
        cell_annot.rename({0: "barcode"}, axis="columns", inplace=True)
        cell_annot["barcodes"] = cell_annot["barcode"].astype(str)
    else:
        __cell_annot__ = pd.read_csv(barcodes_path, sep=barcode_split_character, header=None, index_col=None)

        __is_with__ = True

        # judge
        if len(__cell_annot__.columns) == 1:
            log.warn("Parameter `barcode_split_character` is `-`, but it is not working, ignore.")
            __is_with__ = False

        if __cell_annot__.shape[0] != np.unique(__cell_annot__[0]).size:
            log.info("After extracting `batch_id`, there are duplicate barcodes, so `batch_id` is not extracted.")
            __is_with__ = False

        if __is_with__:
            cell_annot = __cell_annot__
            cell_annot.rename({0: "barcode", 1: "batch_id"}, axis="columns", inplace=True)
            cell_annot["barcodes"] = cell_annot["barcode"].astype(str) + "-" + cell_annot["batch_id"].astype(str)
        else:
            cell_annot.rename({0: "barcode"}, axis="columns", inplace=True)
            cell_annot["barcodes"] = cell_annot["barcode"].astype(str)

    # add annotation file
    if annotation_file is not None:
        cell_annot = barcodes_add_anno(annotation_file, cell_annot)

    cell_annot.set_index("barcode", inplace=True, drop=False)
    cell_annot.index = cell_annot.index.astype(str)
    return cell_annot


def read_info_by_metadata(
    base_path: path,
    feature_file_name: str,
    is_transpose: bool = True,
    barcode_split_character: str = '-',
    annotation_file: path = None,
):
    """
    Read metadata outputted by 10x Genomics software
    :param base_path: Path to directory with matrix, bed file, etc.
    :param feature_file_name: feature file name
    :param is_transpose: Whether transpose is required to read the matrix file, default to True
    :param barcode_split_character: A barcode separated character symbol
    :param annotation_file: The file that adds information about cells must contain the column name `barcodes`
    :return: AnnData
    """
    # read features file
    log.info("handle features information")
    coords = pd.read_table(os.path.join(base_path, feature_file_name), header=None, index_col=None)
    coords.rename({0: "chr", 1: "start", 2: "end"}, axis="columns", inplace=True)
    coords.set_index(
        coords.chr.astype(str) + ":" + coords.start.astype(str) + "-" + coords.end.astype(str),
        inplace=True
    )
    coords.index = coords.index.astype(str)

    # read barcodes file
    cell_annot = read_barcodes_file(os.path.join(base_path, "barcodes.tsv"), barcode_split_character, annotation_file)

    # read matrix file
    log.info("read `matrix.mtx` file")
    data = mmread(os.path.join(base_path, "matrix.mtx")).transpose() if is_transpose else mmread(os.path.join(base_path, "matrix.mtx"))

    return AnnData(data.tocsr(), var=coords, obs=cell_annot)


def read_sc_atac(
    base_path: path = None,
    is_transpose: bool = True,
    barcode_split_character: str = '-',
    on_barcode_split_character: str = None,
    annotation_file: path = None,
    file: path = None,
    file_peak_split_character: Tuple = (":", "-"),
    is_metadata: bool = True
) -> AnnData:
    """
    Read scATAC-seq data outputted by 10x Genomics software
    :param on_barcode_split_character:
    :param base_path: Path to directory with matrix, bed file, etc.
    :param is_transpose: Whether transpose is required to read the matrix file, default to True
    :param barcode_split_character: A barcode separated character symbol
    :param annotation_file: The file that adds information about cells must contain the column name `barcodes`
    :param file: scATAC-seq counts file with row and column names
    :param file_peak_split_character:
    :param is_metadata: Whether to use metadata to read information, default to True
    :return: AnnData
    """
    log.info("Read scATAC-seq data")

    if base_path is None and file is not None:
        is_metadata = False
    elif base_path is not None and file is None:
        is_metadata = True
    elif base_path is None and file is None:
        log.error("At least one of the `base_path` and `file` parameters has a value")
        raise ValueError("At least one of the `base_path` and `file` parameters has a value")

    if is_metadata:

        return read_info_by_metadata(
            base_path=base_path,
            feature_file_name="peaks.bed",
            is_transpose=is_transpose,
            barcode_split_character=barcode_split_character,
            annotation_file=annotation_file
        )

    if len(file_peak_split_character) != 2:
        log.error("The peak feature is used to obtain the segmentation character of `chr` `start` `end`, which requires two characters. The first character is used to segment `chr` and `start`, and the second character is used to segment `start` and `end`")
        raise ValueError("The peak feature is used to obtain the segmentation character of `chr` `start` `end`, which requires two characters. The first character is used to segment `chr` and `start`, and the second character is used to segment `start` and `end`")

    cell_annot, data = handle_file_data_cell(
        file=file,
        barcode_split_character=barcode_split_character,
        on_barcode_split_character=on_barcode_split_character,
        is_transpose=is_transpose
    )

    # add annotation file
    if annotation_file is not None:
        cell_annot = barcodes_add_anno(annotation_file, cell_annot)

    # format peaks information
    log.info("handle peaks information")
    features = pd.DataFrame(columns=["chr", "start", "end"])
    chr_list: list = []
    start_list: list = []
    end_list: list = []

    if file_peak_split_character[0] == file_peak_split_character[1]:
        character_ = file_peak_split_character[0]

        for col in data.columns:
            col: str
            split: list = col.split(character_)
            chr_list.append(split[0])
            start_list.append(int(split[1]))
            end_list.append(int(split[2]))
    else:

        for col in data.columns:
            col: str
            split: list = col.split(file_peak_split_character[0])
            chr_list.append(split[0])
            split2: list = split[1].split(file_peak_split_character[1])
            start_list.append(int(split2[0]))
            end_list.append(int(split2[1]))

    features["chr"] = chr_list
    features["start"] = start_list
    features["end"] = end_list
    features.set_index(
        features.chr.astype(str) + ":" + features.start.astype(str) + "-" + features.end.astype(str),
        inplace=True
    )
    features.index = features.index.astype(str)

    return AnnData(to_sparse(data.values), var=features, obs=cell_annot)


def collect_datasets(dsets: dict, group: h5py.Group):
    for k, v in group.items():
        if isinstance(v, h5py.Dataset):
            dsets[k] = v[()]
        else:
            collect_datasets(dsets, v)


def read_v3_10x_h5(filename):
    """
    Read hdf5 file from Cell Ranger v3 or later versions.
    """
    log.info('Start read hdf5 file')
    with h5py.File(str(filename), 'r') as f:
        try:
            dsets = {}
            collect_datasets(dsets, f["matrix"])

            from scipy.sparse import csr_matrix

            m, n = dsets['shape']
            data = dsets['data']
            if dsets['data'].dtype == np.dtype('int32'):
                data = dsets['data'].view('float32')
                data[:] = dsets['data']
            matrix = csr_matrix(
                (data, dsets['indices'], dsets['indptr']),
                shape=(n, m),
            )
            adata = AnnData(
                matrix,
                obs=dict(obs_names=dsets['barcodes'].astype(str)),
                var=dict(
                    var_names=dsets['name'].astype(str),
                    peak_ids=dsets['id'].astype(str),
                    feature_types=dsets['feature_type'].astype(str),
                    genome=dsets['genome'].astype(str),
                ),
            )
            return adata
        except KeyError:
            raise Exception('File is missing one or more required datasets.')


def read_sc_atac_10x_h5(file: path) -> AnnData:
    return read_v3_10x_h5(file)


def read_gene_10x_h5(file: path) -> AnnData:
    """
    Read gene 10x hdf5 file
    :param file: Path to a 10x hdf5 file
    :return:
    """
    return read_10x_h5(file)


def read_cicero_gene(
    base_path: path = None,
    file: path = None,
    is_transpose: bool = True,
    cluster_anno_file: path = None,
    barcode_split_character: str = '.',
    on_barcode_split_character: str = None,
    is_metadata: bool = True
) -> AnnData:
    """
    Read the gene activity matrix file processed by Cicero
    :param cluster_anno_file:
    :param base_path:
    :param is_metadata:
    :param on_barcode_split_character:
    :param file: Gene activity score file with row and column names
    :param is_transpose: Whether transpose is required to read the matrix file, default to True
    :param barcode_split_character: A barcode separated character symbol
    :return: AnnData
    """
    log.info("Read gene activity data")

    if base_path is None and file is not None:
        is_metadata = False
    elif base_path is not None and file is None:
        is_metadata = True
    elif base_path is None and file is None:
        log.error("At least one of the `base_path` and `file` parameters has a value")
        raise ValueError("At least one of the `base_path` and `file` parameters has a value")

    if not is_metadata:

        return read_info_by_matrix(
            file=file,
            cluster_anno_file=cluster_anno_file,
            is_transpose=is_transpose,
            barcode_split_character=barcode_split_character,
            on_barcode_split_character=on_barcode_split_character
        )

    # read matrix file
    data = mmread(os.path.join(base_path, "matrix.mtx")).transpose() if is_transpose else mmread(os.path.join(base_path, "matrix.mtx"))

    column_name: str = "feature"
    # read features file
    log.info("handle features information")
    coords = pd.read_table(os.path.join(base_path, "gene.tsv"), header=None, index_col=None, )
    coords.columns = [column_name]
    coords.index = coords[column_name].astype(str)

    # read barcodes file
    log.info("handle cells information")
    cell_annot = read_barcodes_file(os.path.join(base_path, "barcodes.tsv"), barcode_split_character, cluster_anno_file)

    return AnnData(data.tocsr(), var=coords, obs=cell_annot)


def read_tf(
    file: path,
    is_transpose: bool = True,
    cluster_anno_file: path = None,
    barcode_split_character: str = '.'
) -> AnnData:
    """
    Read the TF activity matrix file processed by ChromVAR
    :param cluster_anno_file:
    :param file: TF activity score file with row and column names
    :param is_transpose: Whether transpose is required to read the matrix file, default to True
    :param barcode_split_character: A barcode separated character symbol
    :return: AnnData
    """
    log.info("Read TF activity data")

    return read_info_by_matrix(
        file=file,
        is_transpose=is_transpose,
        barcode_split_character=barcode_split_character,
        cluster_anno_file=cluster_anno_file
    )
