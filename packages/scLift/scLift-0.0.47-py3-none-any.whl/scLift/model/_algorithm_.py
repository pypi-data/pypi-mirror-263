# -*- coding: UTF-8 -*-

import itertools
from typing import Union, Tuple, Literal, Optional

import numpy as np
import pandas as pd
# noinspection PyPackageRequirements
import umap
from anndata import AnnData
from mudata import MuData
from pandas import DataFrame

from ykenan_log import Logger

from sklearn.manifold import TSNE, SpectralEmbedding
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import calinski_harabasz_score, adjusted_mutual_info_score, silhouette_score, davies_bouldin_score
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import kneighbors_graph
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import adjusted_rand_score, accuracy_score, recall_score, f1_score

from scipy import special, stats

from scLift.util import matrix_data, to_sparse, to_dense, sparse_matrix, dense_data, number, collection, check_adata_get

log = Logger("scLift_model_algorithm", is_form_file=False)


def tf_idf(data: matrix_data, ri_sparse: bool = True) -> matrix_data:
    """
    TF-IDF transformer
    :param data: Matrix data that needs to be converted
    :param ri_sparse: (return_is_sparse) Whether to return sparse matrix
    :return: matrix
    """
    log.info("TF-IDF transformer")
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(to_dense(data, is_array=True))
    return to_sparse(tfidf) if ri_sparse else to_dense(tfidf)


def adjustment_tf_idf(data: matrix_data, ri_sparse: bool = True) -> matrix_data:
    """
    adjustment TF-IDF transformer
    :param data: Matrix data that needs to be converted
    :param ri_sparse: (return_is_sparse) Whether to return sparse matrix
    :return: matrix
    """
    log.info("Start adjustment TF-IDF transformer")
    data = to_dense(data, is_array=True)
    data_abs = np.abs(data)

    # TF
    row_sum = data_abs.sum(axis=1)
    row_sum[row_sum == 0] = 1
    tf = data / np.array(row_sum).flatten()[:, np.newaxis]

    # DF
    col_sum = data_abs.sum(axis=0)
    col_sum[col_sum == 0] = 1
    df = data_abs / np.array(col_sum).flatten()

    # IDF
    idf = np.log(data.shape[0] / (df + 1))

    # TF_IDF
    tfidf = np.multiply(tf, idf)
    log.info("End adjustment TF-IDF transformer")
    return to_sparse(tfidf) if ri_sparse else to_dense(tfidf)


def z_score_normalize(data: matrix_data, with_mean: bool = True, ri_sparse: bool = True) -> Union[dense_data, sparse_matrix]:
    """
    Matrix standardization
    :param data: Standardized data matrix
    :param with_mean: Standardized data matrix
    :param ri_sparse: (return_is_sparse) Whether to return sparse matrix
    :return: Standardized matrix
    """
    log.info("Matrix z-score standardization")
    scaler = StandardScaler(with_mean=with_mean)

    if with_mean:
        dense_data_ = to_dense(data, is_array=True)
    else:
        dense_data_ = data

    transform_data = scaler.fit_transform(np.array(dense_data_))
    return to_sparse(transform_data) if ri_sparse else to_dense(transform_data)


def z_score_marginal(matrix: matrix_data, axis: Literal[0, 1] = 0) -> Tuple[matrix_data, matrix_data]:
    log.info("Start marginal z-score")
    matrix = np.matrix(to_dense(matrix))
    # Separate z-score for each element
    __mean__ = np.mean(matrix, axis=axis)
    __std__ = np.std(matrix, axis=axis)
    # Control denominator is not zero
    __std__[__std__ == 0] = 1
    z_score = (matrix - __mean__) / __std__
    return z_score, __mean__


def marginal_normalize(matrix: matrix_data, axis: Literal[0, 1] = 0, default: float = 1e-50) -> matrix_data:
    matrix = np.matrix(to_dense(matrix))
    __sum__ = np.sum(matrix, axis=axis)
    return matrix / (__sum__ + default)


def is_asc_sort(positions_list: list) -> bool:
    """
    Judge whether the site is in ascending order
    :param positions_list: positions list
    :return: Is it in ascending order
    """
    length: int = len(positions_list)

    if length <= 1:
        return True

    tmp = positions_list[0]

    for i in range(1, length):
        if positions_list[i] < tmp:
            return False
        tmp = positions_list[i]

    return True


def lsi(data: matrix_data, n_components: int = 50) -> dense_data:
    """
    SVD LSI
    :param data: input cell feature data
    :param n_components: Dimensions that need to be reduced to
    :return:
    """

    if data.shape[1] <= n_components:
        log.info("The features of the data are less than or equal to the `n_components` parameter, ignoring LSI")
        return to_dense(data, is_array=True)
    else:
        log.info("Start LSI")
        svd = TruncatedSVD(n_components=n_components)
        svd_data = svd.fit_transform(to_dense(data, is_array=True))
        log.info("End LSI")
        return svd_data


def pca(data: matrix_data, n_components: int = 50) -> dense_data:
    """
    PCA
    :param data: input cell feature data
    :param n_components: Dimensions that need to be reduced to
    :return:
    """
    if data.shape[1] <= n_components:
        log.info("The features of the data are less than or equal to the `n_components` parameter, ignoring PCA")
        return to_dense(data, is_array=True)
    else:
        log.info("Start PCA")
        data = to_dense(data, is_array=True)
        pca_n = PCA(n_components=n_components)
        pca_n.fit_transform(data)
        pca_data = pca_n.transform(data)
        log.info("End PCA")
        return pca_data


def laplacian_eigenmaps(data: matrix_data, n_components: int = 2) -> dense_data:
    """
    Laplacian Eigenmaps
    :param data: input cell feature data
    :param n_components: Dimensions that need to be reduced to
    :return:
    """
    if data.shape[1] <= n_components:
        log.info("The features of the data are less than or equal to the `n_components` parameter, ignoring Laplacian Eigenmaps")
        return to_dense(data, is_array=True)
    else:
        log.info("Start Laplacian Eigenmaps")
        data = to_dense(data, is_array=True)
        se = SpectralEmbedding(n_components=n_components)
        se_data = se.fit_transform(data)
        log.info("End Laplacian Eigenmaps")
        return se_data


def sample_data(data: matrix_data, sample_number: int = 1000000) -> list:
    """
    down-sampling
    :param data:
    :param sample_number:
    :return:
    """
    # Judge data size
    if data.shape[0] * data.shape[1] <= sample_number:
        return list(to_dense(data, is_array=True).flatten())

    data = to_dense(data, is_array=True)
    row_count = data.shape[0]
    col_count = data.shape[1]

    if row_count < 0:
        log.error("The number of rows of data must be greater than zero")
        raise ValueError("The number of rows of data must be greater than zero")

    log.info(f"Kernel density estimation plot down-sampling data from {row_count * col_count} to {sample_number}")

    # get count
    count = row_count * col_count
    iter_number: int = count // sample_number
    iter_sample_number: int = sample_number // iter_number
    iter_sample_number_final: int = sample_number % iter_number

    if iter_sample_number < 1:
        log.error("The sampling data is too small, increase the `sample_number` parameter value")
        raise ValueError("The sampling data is too small, increase the `sample_number` parameter value")

    log.info(f"Divide and conquer {iter_number} chunks")

    # Create index container
    return_data: list = []

    for i in range(iter_number):

        if iter_number < 50:
            log.info(f"Start {i + 1}th chunk, {(i + 1) / iter_number * 100}%")
        elif iter_number >= 50 and i % 50 == 0:
            log.info(f"Start {i + 1}th chunk, {(i + 1) / iter_number * 100}%")

        # Determine if it is the last cycle
        end_count: int = count if i == iter_number - 1 else (i + 1) * sample_number

        if iter_sample_number_final == 0:
            index = np.random.choice(range(i * sample_number, end_count), iter_sample_number, replace=False)
        else:
            per_iter_sample_number: int = iter_sample_number_final if i == iter_number - 1 else iter_sample_number
            index = np.random.choice(range(i * sample_number, end_count), per_iter_sample_number, replace=False)

        # Add index
        for j in index:
            # row
            row_index = j // col_count
            # column
            col_index = j % col_count

            if row_index >= row_count:
                log.error(f"index ({row_index}) out of range ({row_count})")
                raise IndexError(f"index ({row_index}) out of range ({row_count})")

            if col_index >= col_count:
                log.error(f"index ({col_index}) out of range ({col_count})")
                raise IndexError(f"index ({col_index}) out of range ({col_count})")

            return_data.append(data[row_index, col_index])

    return return_data


def mutual_knn_network(
    data: matrix_data,
    n_neighbors: int = 30
) -> matrix_data:
    cell_cell_knn: matrix_data = to_dense(data).copy()
    cell_cell_knn_copy: matrix_data = cell_cell_knn.copy()

    for j in range(cell_cell_knn.shape[0]):
        cell_cell_knn[j, j] = 0
        cell_cell_knn_copy[j, j] = 0

    # Obtain numerical values for constructing a k-neighbor network
    cell_cell_affinity_sort = np.sort(cell_cell_knn, axis=1)
    cell_cell_value = cell_cell_affinity_sort[:, -(n_neighbors + 1)]
    cell_cell_knn[cell_cell_knn_copy > cell_cell_value] = 1
    cell_cell_knn[cell_cell_knn_copy <= cell_cell_value] = 0
    # Obtain symmetric adjacency matrix, using mutual kNN algorithm
    adjacency_matrix = np.minimum(cell_cell_knn, cell_cell_knn.T)
    return adjacency_matrix


def mutual_knn(
    data: matrix_data,
    n_neighbors: int = 30,
    p: int = 2,
    is_max_one: bool = False
) -> matrix_data:
    """
    :param data: matrix data
    :param n_neighbors: n_neighbors
    :param p: Loss distance
    :param is_max_one: Is the value greater than zero 1
    :return: matrix data
    """
    log.info("Start mutual KNN")
    data = to_dense(data, is_array=True)
    k_neighbors = kneighbors_graph(data, n_neighbors=n_neighbors, p=p)
    k_neighbors = to_dense(k_neighbors)

    if is_max_one:
        # Change the weight greater than 0 to 1
        k_neighbors[k_neighbors > 1] = 1

    # Obtain symmetric adjacency matrix, using mutual kNN algorithm
    k_neighbors_t = k_neighbors.transpose()
    adjacency_matrix = np.minimum(k_neighbors, k_neighbors_t)
    log.info("End mutual KNN")
    return adjacency_matrix


def k_means(
    data: matrix_data,
    n_clusters: int = 2
):
    log.info("Start K-means cluster")
    model = KMeans(n_clusters=n_clusters, n_init="auto")
    model.fit(to_dense(data, is_array=True))
    labels = model.labels_
    log.info("End K-means cluster")
    return labels


def spectral_clustering(data: matrix_data, n_clusters: int = 2) -> collection:
    """
    Spectral clustering
    :param data: input cell feature data
    :param n_clusters: cluster number
    :return:
    """
    log.info("Start spectral clustering")
    data = to_dense(data, is_array=True)
    model = SpectralClustering(n_clusters=n_clusters)
    clusters_types = model.fit_predict(data)
    log.info("End spectral clustering")
    return clusters_types


def regression_network_both(data1: matrix_data, data2: matrix_data) -> Tuple[matrix_data, collection]:
    log.info("Start network regression")
    data1 = to_dense(data1, is_array=True)
    data2 = to_dense(data2, is_array=True)
    # Obtain sample size
    sample_size = data1.shape[0]

    if sample_size != data2.shape[0]:
        log.info("")
        raise ValueError("")

    a_list: list = []
    k_network: matrix_data = np.zeros((sample_size, sample_size))

    for i in range(sample_size):
        if i >= 50 and i % 50 == 0:
            log.info(f"Started executing the {i}-th sample, completed {i / sample_size * 100}%")

        y_index: list = list(range(sample_size))
        y_index.remove(i)

        # Obtain dependent and independent variables
        y = data1[i, :]
        x = data2[y_index, :]

        # Linear Regression
        regression = LinearRegression()
        regression.fit(x.T, y.T)

        # get result
        a_list.append(regression.intercept_)
        intercept = list(regression.coef_)
        intercept.insert(i, 0)
        k_network[i, :] = intercept

    log.info("End network regression")
    return k_network, np.array(a_list)


def regression_network_self(data1: matrix_data, data2: matrix_data) -> Tuple[collection, collection]:
    log.info("Start network regression")
    data1 = to_dense(data1, is_array=True)
    data2 = to_dense(data2, is_array=True)
    # Obtain sample size
    sample_size = data1.shape[0]

    a_list: list = []
    k_network: list = []

    for i in range(sample_size):
        if i >= 50 and i % 50 == 0:
            log.info(f"Started executing the {i}-th sample, completed {i / sample_size * 100}%")

        # Obtain dependent and independent variables
        y = data1[i, :]
        x = data2[i, :][:, np.newaxis]
        # Linear Regression
        regression = LinearRegression()
        regression.fit(x, y.T)

        # get result
        a_list.append(regression.intercept_)
        k_network.append(list(regression.coef_)[0])

    log.info("End network regression")
    return np.array(k_network), np.array(a_list)


def regression_network(data: matrix_data) -> Tuple[matrix_data, collection]:
    return regression_network_both(data, data)


def tsne_data(
    data: matrix_data,
    p: int = 2
) -> matrix_data:
    data = to_dense(data, is_array=True)
    tsne = TSNE(n_components=p)
    tsne.fit(data)
    data_tsne = tsne.fit_transform(data)
    return data_tsne


def umap_data(
    data: matrix_data,
    n_neighbors: int = 15
) -> matrix_data:
    data = to_dense(data, is_array=True)
    embedding = umap.UMAP(n_neighbors=n_neighbors).fit_transform(data)
    return embedding


def kl_divergence(data1: matrix_data, data2: matrix_data) -> float:
    data1 = to_dense(data1, is_array=True).flatten()
    data2 = to_dense(data2, is_array=True).flatten()
    return stats.entropy(data1, data2)


# noinspection SpellCheckingInspection
def calinski_harabasz(data: matrix_data, labels: collection) -> float:
    """
    The Calinski-Harabasz index is also one of the indicators used to evaluate the quality of clustering models.
    It measures the compactness within the cluster and the separation between clusters in the clustering results. The larger the value, the better the clustering effect
    :param data: data
    :param labels: label
    :return: index
    """
    return calinski_harabasz_score(to_dense(data, is_array=True), labels)


def silhouette(data: matrix_data, labels: collection) -> float:
    """
    silhouette
    :param data: data
    :param labels: label
    :return: index
    """
    return silhouette_score(to_dense(data, is_array=True), labels)


def davies_bouldin(data: matrix_data, labels: collection) -> float:
    """
    Davies-Bouldin index (DBI)
    :param data: data
    :param labels: label
    :return: index
    """
    return davies_bouldin_score(to_dense(data, is_array=True), labels)


def ari(labels_pred: collection, labels_true: collection) -> float:
    """
    ARI (-1, 1)
    :param labels_pred: Predictive labels for clustering
    :param labels_true: Real labels for clustering
    :return: index
    """
    return adjusted_rand_score(labels_true, labels_pred)


def ami(labels_pred: collection, labels_true: collection) -> float:
    """
    AMI (0, 1)
    :param labels_pred: Predictive labels for clustering
    :param labels_true: Real labels for clustering
    :return: index
    """
    return adjusted_mutual_info_score(labels_true, labels_pred)


def accuracy_recall_f1(labels_pred: collection, labels_true: collection) -> Tuple[float, float, float]:
    """
    accuracy_score, recall_score, f1_score
    :param labels_pred: Predictive labels for clustering
    :param labels_true: Real labels for clustering
    :return: index
    """
    a_s = accuracy_score(labels_true, labels_pred)
    r_s = recall_score(labels_true, labels_pred)
    f1_s = f1_score(labels_true, labels_pred)
    return a_s, r_s, f1_s


def symmetric_scale(data: matrix_data, scale: Union[number, collection] = 2.0, axis: Literal[0, 1, -1] = -1) -> matrix_data:
    """
    Expanse Sigmoid Function
    Customized function with a range of (-1, 1), obtained from sigmoid deformation
    :param axis:
    :param data: matrix data
    :param scale:
    :return:
    """
    log.info("Start expanse sigmoid function")

    # Non negative data
    if axis == -1:
        scale = 1 if scale == 0 else scale
        x_data = to_dense(data) / scale
    elif axis == 0:
        scale = to_dense(scale, is_array=True).flatten()
        scale[scale == 0] = 1
        x_data = to_dense(data) / scale
    elif axis == 1:
        scale = to_dense(scale, is_array=True).flatten()
        scale[scale == 0] = 1
        x_data = to_dense(data) / scale[:, np.newaxis]
    else:
        log.warn("The `axis` parameter supports only -1, 0, and 1, while other values will make the `scale` parameter value equal to 1.")
        x_data = to_dense(data)

    # Record symbol information
    symbol = to_dense(x_data).copy()
    symbol[symbol > 0] = 1
    symbol[symbol < 0] = -1

    # Log1p standardized data
    y_data = np.multiply(x_data, symbol)
    y_data = special.log1p(y_data)
    # Return symbols and make changes and sigmoid mapped data
    z_data = np.multiply(y_data, symbol)
    log.info("End expanse sigmoid function")
    return z_data


def deviation_z_score(data: matrix_data, data_bg: matrix_data, axis: Literal[-1, 0, 1] = -1, scale: int = 1):
    if data.shape != data_bg.shape:
        log.error(f"The two matrices inputted are not of the same size and must remain consistent. {data.shape} != {data_bg.shape}")

    data = to_dense(data)
    data_bg = to_dense(data_bg)

    if axis == -1:
        __std__ = data_bg.std()
        __mean__ = data_bg.mean()

        if __std__ == 0:
            __std__ = 1

        z = (data - __mean__ / scale) / __std__
    else:
        __std__ = data_bg.std(axis=axis)
        __mean__ = data_bg.mean(axis=axis)

        __std__[__std__ == 0] = 1
        z = (data - __mean__ / scale) / __std__

    return z


class RandomWalk:

    def __init__(
        self,
        cc_adata: AnnData,
        init_status: AnnData,
        gamma: float = 0.05,
        stationary_cutoff: float = 1e-05,
        p: int = 2
    ):
        """
        Perform random walk steps
        :param cc_adata: Cell features
        :param init_status: For cell scores under each trait
        :param gamma: weight
        :param stationary_cutoff: stationary cutoff
        :param p: Distance used for loss {1: Manhattan distance, 2: Euclidean distance}
        :return: Stable distribution score
        """
        # judge length
        if cc_adata.shape[0] != init_status.shape[0]:
            log.error(f"The number of rows {cc_adata.shape[0]} in the data is not equal to the initialization state length {np.array(init_status).size}")
            raise ValueError(f"The number of rows {cc_adata.shape[0]} in the data is not equal to the initialization state length {np.array(init_status).size}")

        if p <= 0:
            log.error("The value of `p` must be greater than zero. Distance used for loss {1: Manhattan distance, 2: Euclidean distance}")
            raise ValueError("The value of `p` must be greater than zero. Distance used for loss {1: Manhattan distance, 2: Euclidean distance}")

        init_status.obs["k_clusters"] = init_status.obs["k_clusters"].astype(str)
        self.cc_adata = cc_adata
        self.init_status = init_status
        self.gamma = gamma
        self.stationary_cutoff = stationary_cutoff
        self.enrichment_threshold = cc_adata.uns["DBI"]
        self.p = p

        self.cell_affinity = to_dense(cc_adata.layers["cell_affinity"])
        self.trs_data: AnnData = init_status.copy()
        self.trs_data.X = to_sparse(init_status.X)
        self.trs_data.obsm["cell_affinity"] = to_sparse(self.cell_affinity)

        self.trait_info: list = list(init_status.var["id"])

        # set seed cells
        self.trait_cell_source = np.zeros(init_status.shape)
        self.trait_cell_scale = np.zeros(init_status.shape)
        self.random_cell_matrix = np.zeros(init_status.shape)
        # ablation stype
        self.none_study = np.zeros(init_status.shape)

        # trait
        self.trait_list: list = list(self.trs_data.var_names)
        self.trait_range = range(len(self.trait_list))

        # Transition Probability Matrix
        self.weight, self.cell_weight = self._get_weight_()
        self.trs_data.obsm["cell_weight"] = to_sparse(self.cell_weight)
        # get seed value
        self.seed_cell_size, self.seed_cell_threshold, self.seed_cell_matrix, self.seed_cell_weight = self._get_seed_cell_()

    def _random_walk_core_(self, seed_cell_vector: collection, weight: matrix_data = None) -> matrix_data:
        """
        Perform a random walk
        :param seed_cell_vector: seed cells
        :return:
        """

        if weight is None:
            w = to_dense(self.weight).copy()
        else:
            w = to_dense(weight).copy()

        # Random walk
        p0 = seed_cell_vector.copy()[:, np.newaxis]
        pt: matrix_data = seed_cell_vector.copy()[:, np.newaxis]
        k = 0
        delta = 1

        # iteration
        while delta > self.stationary_cutoff:
            p1 = (1 - self.gamma) * np.dot(w, pt) + self.gamma * p0

            # 1 and 2, It would be faster alone
            if self.p == 1:
                delta = np.abs(pt - p1).sum()
            elif self.p == 2:
                delta = np.sqrt(np.square(np.abs(pt - p1)).sum())
            else:
                delta = np.float_power(np.float_power(np.abs(pt - p1), self.p).sum(), 1.0 / self.p)

            pt = p1
            k += 1

        log.info(f"Stationary step: {k}, delta: {delta}")
        return pt.flatten()

    def _get_weight_(self) -> Tuple[matrix_data, matrix_data]:
        data = to_dense(self.cc_adata.X, is_array=True)
        cell_sum = data.sum(axis=1)[:, np.newaxis]
        cell_sum[cell_sum == 0] = 1
        cell_weight = np.multiply(data, self.cell_affinity)
        return data / cell_sum, cell_weight

    def _get_seed_cell_(self) -> Tuple[collection, collection, matrix_data, matrix_data]:

        # seed cell threshold
        seed_cell_size: collection = np.zeros(len(self.trait_list))
        seed_cell_threshold: collection = np.zeros(len(self.trait_list))
        seed_cell_matrix: matrix_data = np.zeros(self.trs_data.shape)
        seed_cell_weight: matrix_data = np.zeros(self.trs_data.shape)

        size = self.trs_data.shape[0]

        # cluster size
        cluster_types = list(set(self.trs_data.obs["k_clusters"]))
        cluster_types.sort()

        clusters = list(self.trs_data.obs["k_clusters"])
        cluster_size: dict = {}
        cluster_size_list = []
        for cluster in cluster_types:
            count = clusters.count(cluster)
            cluster_size.update({cluster: clusters.count(cluster), "rate": count / size})
            cluster_size_list.append(clusters.count(cluster))

        cluster_type_size = np.array(cluster_size_list)
        start_size = np.min(cluster_type_size).astype(int)
        end_size = np.ceil(size / len(cluster_types)).astype(int)

        matrix_rate_dict: dict = {}

        for i in self.trait_range:
            log.info(f"Handler {self.trait_list[i]} trait")
            # Obtain all cell score values in a trait
            trait_adata = self.init_status[:, i]
            trait_value = to_dense(trait_adata.X, is_array=True).flatten()

            # Obtain the maximum initial score
            trait_value_max = np.max(trait_value)
            if trait_value_max <= 0:
                log.warn(f"There is no possibility of enrichment between scATAC-seq and {self.trait_list[i]} trait obtained from the initialization score.")
            else:
                trait_value_sort_index = np.argsort(trait_value).astype(int)
                trait_value_sort_index = trait_value_sort_index[::-1]

                # Get the sorted cell type after initial value sorting
                trait_adata_sort = trait_adata[trait_value_sort_index, :]
                k_clusters = trait_adata_sort.obs["k_clusters"]

                # Filter seed threshold information
                matrix = np.zeros((len(cluster_types), (end_size - start_size)))
                vector = np.zeros(len(cluster_types))

                for j in range(end_size):
                    vector[cluster_types.index(k_clusters[j])] += 1

                    if j >= start_size:
                        matrix[:, j - start_size] = vector.copy()

                matrix_rate: matrix_data = matrix / cluster_type_size[:, np.newaxis]
                matrix_rate_dict.update({self.trait_list[i]: matrix_rate})
                # get max rate
                size_max = np.array(matrix_rate.max(axis=0)).flatten()
                size_max_index = np.argsort(size_max)
                seed_size = range(start_size, end_size)[size_max_index[-1]]
                seed_cell_size[i] = int(seed_size)
                seed_cell_threshold[i] = size_max[seed_size - start_size]

                # Remove noise seed cells and set seed cell values
                log.info("Set seed cells weight")
                seed_cell_index = trait_value_sort_index[0:seed_size + 1]
                seed_cell_mutual_knn = np.array(self.cell_weight[seed_cell_index, :][:, seed_cell_index])
                seed_weight_threshold: collection = seed_cell_mutual_knn.sum(axis=0)
                seed_weight_threshold /= (1 if seed_weight_threshold.sum() == 0 else seed_weight_threshold.sum())
                seed_cell_weight[:, i][seed_cell_index] = seed_weight_threshold

                # add threshold
                seed_cell_value = np.zeros(size)
                seed_cell_value[seed_cell_index] = 1
                seed_cell_matrix[:, i] = seed_cell_value / (1 if seed_cell_value.sum() == 0 else seed_cell_value.sum())

        self.trs_data.uns["cluster_info"] = {
            "cluster_size": cluster_size,
            "range_size": (start_size, end_size),
            "matrix_rate": matrix_rate_dict
        }
        return seed_cell_size.astype(int), seed_cell_threshold, seed_cell_matrix, seed_cell_weight

    def _run_base_(self, data_vector: collection, i: int, info: str = None):
        # information output
        log.info(f"Start random walk on trait {self.trait_info[i]} {'' if info is None else info}")
        log.info(f"Random walk on trait {self.trait_info[i]} ==> Threshold value: {self.seed_cell_threshold[i]} {'' if info is None else info}")

        # Random walk
        cell_value = self._random_walk_core_(data_vector)
        return cell_value

    def _run_random_(self, i: int, is_disturbance: bool = False):
        if not is_disturbance:
            log.info(f"Start random cell (Random walk)")

        # Set random seed information
        random_seed_cell = np.zeros(self.cell_weight.shape[0])
        random_seed_index = np.random.choice(np.arange(0, self.cell_weight.shape[0]), size=self.seed_cell_size[i], replace=False)
        random_seed_cell[random_seed_index] = 1

        # Remove noise seed cells and set seed cell values
        seed_weight_threshold: collection = np.array(self.cell_weight[random_seed_index, :][:, random_seed_index]).sum(axis=0)
        seed_weight_threshold /= (1 if seed_weight_threshold.sum() == 0 else seed_weight_threshold.sum())
        random_seed_cell[random_seed_index] = seed_weight_threshold

        # Random walk
        cell_value = self._random_walk_core_(random_seed_cell)

        # Remove the influence of background
        cell_value = symmetric_scale(cell_value, scale=cell_value.mean(), axis=-1)
        self.random_cell_matrix[:, i] = cell_value

    def run_random(self):

        for i in self.trait_range:
            self._run_random_(i)

        cell_value = symmetric_scale(self.random_cell_matrix, scale=np.abs(self.random_cell_matrix).mean(axis=0), axis=0)
        self.trs_data.layers["trait_cell_random"] = to_sparse(cell_value)

    def run_none(self):

        for i in self.trait_range:
            self.none_study[:, i] = self._run_base_(self.seed_cell_matrix[:, i], i, "none")

        cell_value = symmetric_scale(self.none_study, scale=np.abs(self.none_study).mean(axis=0), axis=0)
        self.trs_data.layers["trait_cell_none"] = to_sparse(cell_value)

    def run_core(self):

        for i in self.trait_range:
            self.trait_cell_source[:, i] = self._run_base_(self.seed_cell_weight[:, i], i)

        # add value
        self.trs_data.var["seed_cell_size"] = self.seed_cell_size
        self.trs_data.var["seed_cell_threshold"] = self.seed_cell_threshold

        # add result
        self.trs_data.layers["seed_cell_matrix"] = to_sparse(self.seed_cell_matrix)
        self.trs_data.layers["seed_cell_weight"] = to_sparse(self.seed_cell_weight)
        self.trs_data.layers["trait_cell_source"] = to_sparse(self.trait_cell_source)

        # Scaling the original cell score information
        cell_value = symmetric_scale(self.trait_cell_source, scale=np.abs(self.trait_cell_source).mean(axis=0), axis=0)
        self.trs_data.layers["trait_cell_scale"] = to_sparse(cell_value)
        self.trait_cell_scale = cell_value

    def run_enrichment(self):
        # Initialize enriched container
        trait_cell_enrichment = np.zeros(self.trs_data.shape)

        for i in self.trait_range:
            # Only retain seed information in traits
            seed_cell_weight: matrix_data = self.seed_cell_weight[:, i].copy()

            # Obtain the sorting of seed size
            sort_index = seed_cell_weight.argsort()
            seed_cell_weight_sort = np.sort(seed_cell_weight)
            sort_index_reserve = sort_index[::-1]

            new_seed_cell_weight = np.zeros(self.trs_data.shape[0])
            new_seed_cell_weight[sort_index_reserve] = seed_cell_weight_sort

            # Random walk
            cell_value = self._run_base_(new_seed_cell_weight, i, "enrichment")
            cell_value = np.array(cell_value).flatten()
            trait_cell_enrichment[:, i][self.trait_cell_source[:, i] >= cell_value] = 1
            trait_cell_enrichment[:, i][self.trait_cell_scale[:, i] < self.enrichment_threshold] = 0
            trait_cell_enrichment[:, i][self.trait_cell_scale[:, i] >= self.enrichment_threshold] = 1

        self.trs_data.layers["trait_cell_enrichment"] = to_sparse(trait_cell_enrichment)


def adata_group(
    adata: AnnData,
    column: str,
    axis: Literal[0, 1] = 0,
    layer: str = None,
    method: Tuple[str] = ("mean", "sum", "max", "min")
) -> AnnData:
    """
    Group x types to obtain relevant information
    :param adata: data
    :param column: grouping columns
    :param axis: {0: adata.obs, 1: adata.var}
    :param layer:
    :param method: Sum or average or two total
    :return: AnnData
    """
    # judge input data
    if adata.shape[0] == 0:
        log.warn("Input data is empty")
        return adata

    # judge axis
    if not isinstance(axis, number) or axis not in range(2):
        log.error("The `axis` parameter must be either 0 or 1")
        raise ValueError("The `axis` parameter must be either 0 or 1")

    # get data
    data: AnnData = adata.copy() if axis == 0 else adata.T.copy()

    # judge layers
    if layer is not None:
        if layer not in list(data.layers):
            log.error("The `layer` parameter needs to include in `adata.layers`")
            raise ValueError("The `layer` parameter needs to include in `adata.layers`")
        data.X = data.layers[layer]

    # judge method
    if len(method) == 0 or method[0] not in ("sum", "mean") or (len(method) == 2 and method[1] not in ("sum", "mean")):
        log.error("The `method` parameter is a tuple type and needs to contain one or both of `sum` or `mean`")
        raise ValueError("The `method` parameter is a tuple type and needs to contain one or both of `sum` or `mean`")

    # get group information
    data_obs: DataFrame = data.obs
    if column not in data_obs.columns:
        log.error(f"The grouped column {column} are not in the corresponding columns {data_obs.columns}")
        raise ValueError(f"The grouped column {column} are not in the corresponding columns {data_obs.columns}")

    # handle group information
    column_group: list = list(set(data_obs[column]))
    column_size = len(column_group)
    obs = pd.DataFrame(column_group, columns=[column])
    obs.index = np.array(column_group).astype(str)

    # create container
    matrix_sum: matrix_data = np.zeros((column_size, data.shape[1]))
    matrix_mean: matrix_data = np.zeros((column_size, data.shape[1]))
    matrix_max: matrix_data = np.zeros((column_size, data.shape[1]))
    matrix_min: matrix_data = np.zeros((column_size, data.shape[1]))

    # add data
    for i in range(column_size):
        # 获取 data_obs 下的索引信息
        data_obs_column: DataFrame = data_obs[data_obs[column] == column_group[i]]
        # sum value
        overlap_variant = data[list(data_obs_column.index), :]

        if "mean" in method:
            matrix_mean[i] = overlap_variant.X.mean(axis=0)

        if "sum" in method:
            matrix_sum[i] = overlap_variant.X.sum(axis=0)

        if "max" in method:
            matrix_max[i] = np.amax(to_dense(overlap_variant.X, is_array=True), axis=0)

        if "min" in method:
            matrix_min[i] = np.amin(to_dense(overlap_variant.X, is_array=True), axis=0)

    # create result
    ann_data = AnnData(matrix_mean, obs=obs, var=data.var)

    if "sum" in method:
        ann_data.layers["matrix_sum"] = matrix_sum

    if "max" in method:
        ann_data.layers["matrix_max"] = matrix_max

    if "min" in method:
        ann_data.layers["matrix_min"] = matrix_min

    return ann_data if axis == 0 else ann_data.T


def adata_map_df(
    adata: AnnData,
    column: str = "value",
    layer: str = None
) -> DataFrame:
    # judge input data
    data: AnnData = check_adata_get(adata, layer=layer)

    # get group information
    data_obs: DataFrame = data.obs.copy()
    data_var: DataFrame = data.var.copy()

    if column in data_obs.columns or column in data_var.columns:
        log.error(f"The newly generated column cannot be within the existing column name")
        raise ValueError(f"The newly generated column cannot be within the existing column name")

    # rename index
    __on__: str = "on_5645465353221"
    data_var.rename_axis("y_index", inplace=True)
    data_var.reset_index(inplace=True)
    data_var["on_"] = __on__
    data_obs.rename_axis("x_index", inplace=True)
    data_obs.reset_index(inplace=True)
    data_obs["on_"] = __on__

    # create data
    log.info("Create Table")
    data_df: DataFrame = data_var.merge(data_obs, on="on_", how="outer")
    data_df.drop(["on_"], axis=1, inplace=True)
    data_df[column] = to_dense(data.X.T, is_array=True).flatten()
    return data_df


def euclidean_distances(data1: matrix_data, data2: matrix_data = None) -> matrix_data:
    """
    Calculate the Euclidean distance between two matrices
    :param data1:
    :param data2:
    :return:
    """
    log.info("Start euclidean distances")

    if data2 is None:
        data2 = data1.copy()

    data1 = to_dense(data1)
    data2 = to_dense(data2)
    __data1_sum_sq__ = np.power(data1, 2).sum(axis=1)
    data1_sum_sq = __data1_sum_sq__.reshape((-1, 1))
    data2_sum_sq = __data1_sum_sq__ if data2 is None else np.power(data2, 2).sum(axis=1)

    distances = data1_sum_sq + data2_sum_sq - 2 * data1.dot(data2.transpose())
    distances[distances < 0] = 0.0
    distances = np.sqrt(distances)
    return distances


def cluster_score(matrix: matrix_data, true_labels: collection, method: str = "k_means", cycle_number: int = 1) -> Tuple[float, float, float]:
    ari_score = 0
    ami_score = 0

    for i in range(cycle_number):
        # cluster method
        if method == "k_means":
            cluster_types = k_means(matrix, len(set(true_labels)))
        elif method == "spectral":
            cluster_types = spectral_clustering(matrix, len(set(true_labels)))
        else:
            log.warn("The parameter `method` only supports two types of inputs: `spectral` and `k_means`")
            raise ValueError("The parameter `method` only supports two types of inputs: `spectral` and `k_means`")

        ari_score += ari(cluster_types, true_labels)
        ami_score += ami(cluster_types, true_labels)

    # cluster score
    ch_score = calinski_harabasz(matrix, true_labels)
    return ch_score, ari_score / cycle_number, ami_score / cycle_number


class SNI:

    def __init__(
        self,
        data: MuData,
        alpha: float = 1,
        beta: float = 1,
        n_components: int = 30,
        layer: Optional[str] = None
    ):
        """
        Standardized network integration
        :param beta:
        :param n_components:
        :param data: The datas of affinity matrices
        :param alpha: hyperparameter, usually
        :return: The output is a unified similarity graph. It contains both complementary information and common structures from all individual network.
        """

        self.data = data
        self.alpha = alpha

        if self.alpha > 1 or self.alpha <= 0:
            log.error("The parameter `alpha` must not be greater than zero and less than or equal to 1, and the Gamma distribution must be monotonically decreasing")
            raise ValueError("The parameter `alpha` must not be greater than zero and less than or equal to 1, and the Gamma distribution must be monotonically decreasing")

        self.beta = beta
        self.n_components = n_components

        self.keys: list = self.data.uns["keys"]

        self.affinity_list = []
        self.scores: dict = {}
        self.input_data: dict = {}

        for key in self.keys:
            if layer is not None:
                self.input_data.update({key: self.data[key].layers[layer]})
            else:
                self.input_data.update({key: self.data[key].X})

        # cell count
        self.sample_count = self.input_data[self.keys[0]].shape[0]

        self.affinity = np.zeros((self.sample_count, self.sample_count))

    def _dimension_reduction_(self, input_data: matrix_data, method: str = "lsi") -> matrix_data:
        if method == "lsi":
            return lsi(input_data, n_components=self.n_components)
        elif method == "pca":
            return pca(input_data, n_components=self.n_components)
        elif method == "le":
            return laplacian_eigenmaps(input_data, n_components=self.n_components)
        else:
            log.warn("The parameter `method` only supports two types of inputs: `lsi`, `le` and `pca`")
            raise ValueError("The parameter `method` only supports two types of inputs: `lsi`, `le` and `pca`")

    @staticmethod
    def _distances_(input_data: matrix_data) -> Tuple[matrix_data, matrix_data]:
        ed_data = euclidean_distances(input_data)
        ed_scale_data = symmetric_scale(ed_data, ed_data.mean(axis=1), axis=1)
        return ed_data, ed_scale_data

    def _affinity_(self, input_data: matrix_data) -> matrix_data:
        """
        This function constructs similarity networks
        :param input_data:
        :return:
        """
        log.info("Start affinity matrix")

        distances = to_dense(input_data, is_array=True)

        # Fitting Gaussian distribution
        # affinity_data = stats.norm.pdf(distances, scale=self.beta)
        # a: alpha, scale: beta
        affinity_data = stats.gamma.pdf(distances, a=self.alpha, scale=self.beta)
        return affinity_data

    def core(self) -> matrix_data:

        self.affinity = np.zeros((self.sample_count, self.sample_count))

        for i in range(len(self.keys)):
            data_type: str = self.keys[i]
            log.info(f"Start `{data_type}` data type dimension reduction, distances, affinity.")

            # Dimension reduction
            dimension_reduction_data = self._dimension_reduction_(self.input_data[data_type])
            self.data[data_type].obsm["dimension_reduction"] = dimension_reduction_data
            # Distances
            distances_data, distances_scale_data = self._distances_(dimension_reduction_data)
            self.data[data_type].obsm["distances"] = distances_data
            self.data[data_type].obsm["distances_scale"] = distances_scale_data
            # Affinity
            affinity_data = self._affinity_(distances_scale_data)
            # Global affinity
            self.affinity_list.append(affinity_data)
            self.data[data_type].obsm["affinity"] = affinity_data
            self.affinity += affinity_data

        self.affinity /= len(self.keys)
        self.affinity = symmetric_scale(self.affinity, self.affinity.mean(axis=1), axis=1)

        # calculate KL divergence
        data_type_two = list(itertools.permutations(range(len(self.keys)), len(self.keys) - 1))

        for i, j in data_type_two:
            name = f"{self.keys[i]}-{self.keys[j]}"

            affinity_score = kl_divergence(self.affinity_list[i], self.affinity_list[j])
            self.scores.update({name: affinity_score})

        return self.affinity
