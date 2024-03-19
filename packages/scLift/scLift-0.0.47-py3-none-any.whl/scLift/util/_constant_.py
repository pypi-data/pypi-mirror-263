# -*- coding: UTF-8 -*-

import os
from typing import Union, Tuple
from pathlib import Path

from numpy import ndarray, matrix
from pandas import CategoricalDtype
from scipy.sparse import coo_matrix, csr_matrix, csc_matrix, dok_matrix, lil_matrix, bsr_matrix, dia_matrix, spmatrix, coo_array, csr_array, csc_array, dok_array, lil_array, bsr_array, dia_array, sparray

project_version = "0.0.1"
project_name = "scLift"

user_path = os.path.expanduser("~")
project_cache_path: str = os.path.join(user_path, ".cache", project_name)

path = Union[str, Path]
number = Union[int, float]
collection = Union[list, set, Tuple, ndarray]

sparse_array = Union[coo_array, csr_array, csc_array, dok_array, lil_array, bsr_array, dia_array, sparray]
sparse_matrix = Union[coo_matrix, csr_matrix, csc_matrix, dok_matrix, lil_matrix, bsr_matrix, dia_matrix, spmatrix]

sparse_data = Union[sparse_array, sparse_matrix]
dense_data = Union[ndarray, matrix, list]

matrix_data = Union[sparse_data, dense_data]

classification_colors: list = [
    (0.2081, 0.1663, 0.5292),
    (0.212252381, 0.2137714286, 0.6269714286),
    (0.1959047619, 0.2644571429, 0.7279),
    (0.1252714286, 0.3242428571, 0.8302714286),
    (0.0116952381, 0.3875095238, 0.8819571429),
    (0.0165142857, 0.4266, 0.8786333333),
    (0.0498142857, 0.4585714286, 0.8640571429),
    (0.0722666667, 0.4886666667, 0.8467),
    (0.079347619, 0.5200238095, 0.8311809524),
    (0.0640571429, 0.5569857143, 0.8239571429),
    (0.0265, 0.6137, 0.8135),
    (0.0230904762, 0.6417857143, 0.7912666667),
    (0.0266619048, 0.6641952381, 0.7607190476),
    (0.0589714286, 0.6837571429, 0.7253857143),
    (0.1132952381, 0.7015, 0.6858571429),
    (0.1801333333, 0.7176571429, 0.6424333333),
    (0.2586428571, 0.7317142857, 0.5954285714),
    (0.3481666667, 0.7424333333, 0.5472666667),
    (0.4420095238, 0.7480809524, 0.5033142857),
    (0.5300285714, 0.7491142857, 0.4661142857),
    (0.609852381, 0.7473142857, 0.4336857143),
    (0.6834190476, 0.7434761905, 0.4044333333),
    (0.7524857143, 0.7384, 0.3768142857),
    (0.8185047619, 0.7327333333, 0.3497904762),
    (0.8824333333, 0.7274333333, 0.3217),
    (0.9449571429, 0.7261142857, 0.2886428571),
    (0.9937714286, 0.7454571429, 0.240347619),
    (0.9955333333, 0.7860571429, 0.196652381),
    (0.9788571429, 0.8271428571, 0.1633142857),
    (0.9625857143, 0.8705142857, 0.1309),
    (0.9598238095, 0.9218333333, 0.0948380952),
    (0.9763, 0.9831, 0.0538)
]

chrtype = CategoricalDtype(
    [
        "chr1",
        "chr2",
        "chr3",
        "chr4",
        "chr5",
        "chr6",
        "chr7",
        "chr8",
        "chr9",
        "chr10",
        "chr11",
        "chr12",
        "chr13",
        "chr14",
        "chr15",
        "chr16",
        "chr17",
        "chr18",
        "chr19",
        "chr20",
        "chr21",
        "chr22",
        "chrX",
        "chrY"
    ],
    ordered=True
)
