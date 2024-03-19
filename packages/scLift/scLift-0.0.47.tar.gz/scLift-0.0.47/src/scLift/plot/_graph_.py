# -*- coding: UTF-8 -*-

import networkx as nx
import numpy as np
import seaborn as sns
from anndata import AnnData
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.gridspec import GridSpec
from matplotlib import pyplot as plt
from pandas import DataFrame

from scLift.model import adata_map_df
from scLift.util import matrix_data, collection, path, list_index, to_dense, classification_colors
from ykenan_log import Logger

log = Logger("scLift_plot_graph", is_form_file=False)


def graph(
    data: matrix_data,
    labels: collection = None,
    node_size: int = 50,
    is_font: bool = False,
    output: path = None,
    show: bool = True
) -> None:
    """
    plot graph from adjacency matrix
    :param data: input data
    :param labels: Label of data node
    :param node_size: Size of data node
    :param is_font: Is there a word on the data node
    :param output: Image output path
    :param show: Whether to display pictures
    :return: None
    """
    if output is None and not show:
        log.info(f"At least one of the `output` and `show` parameters is required")
    else:
        plt.figure(figsize=(8, 8), dpi=150)

        # Determine whether it is a square array
        if data.shape[0] != data.shape[1]:
            log.error("The input data must be a square matrix.")
            raise ValueError("The input data must be a square matrix.")

        # set labels
        labels_dict = {}

        if labels is not None:

            if data.shape[0] != np.asarray(labels).size:
                log.error(f"The number of input data nodes {data.shape[0]} and the number of labels {np.asarray(labels).size} must be consistent")
                raise ValueError(f"The number of input data nodes {data.shape[0]} and the number of labels {np.asarray(labels).size} must be consistent")

            labels_dict: dict = dict(zip(range(len(labels)), labels))

        rows, cols = np.where(data == 1)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph(name="Cell-cell graph")
        gr.add_edges_from(edges)
        pos = nx.spring_layout(gr, k=0.15, iterations=35, seed=2023)

        options: dict = {
            "node_color": "black",
            "node_size": node_size,
            "linewidths": 0,
            "width": 0.1
        }

        if is_font:
            if labels is not None:
                nx.draw(gr, pos=pos, labels=labels_dict, **options)
            else:
                nx.draw(gr, pos=pos, **options)
        else:
            nx.draw(gr, pos=pos, labels={}, **options)

        if show:
            plt.show()

        if output is not None:
            plt.savefig(output if output.endswith(".pdf") else f"{output}.pdf")

        plt.close()


def communities_graph(
    adata: AnnData,
    labels: collection,
    node_size: float = 2.0,
    linewidths: float = 0.001,
    right: float = 0.8,
    output: path = None,
    show: bool = True
):
    if output is None and not show:
        log.info(f"At least one of the `output` and `show` parameters is required")
    else:
        log.info("Start cell-cell network diagram")

        # Number of cell to cell connections
        adata_df: DataFrame = adata_map_df(adata, column="value")
        cell_cell_number: DataFrame = adata_df[["clusters_x", "value"]].groupby("clusters_x", as_index=False).sum()
        cell_number: DataFrame = adata.obs[['barcode', 'clusters']].groupby("clusters", as_index=False).size()
        cell_data = cell_number.merge(cell_cell_number, left_on="clusters", right_on="clusters_x")
        # Calculate ratio
        cell_data["cell_number_percentage"] = cell_data["value"] / cell_data["value"].sum() * 100
        cell_data["cell_degree_percentage"] = cell_data["size"] / cell_data["size"].sum() * 100

        # adjust matrix
        adj_matrix = to_dense(adata.X)
        communities, node_labels = list_index(labels)

        log.info("Get position")
        g = nx.from_numpy_array(adj_matrix)
        partition = [0 for _ in range(g.number_of_nodes())]
        for c_i, nodes in enumerate(communities):
            for i in nodes:
                partition[i] = classification_colors[c_i]

        pos = nx.spring_layout(g)

        pos1 = [p[0] for p in pos.values()]
        pos2 = [p[1] for p in pos.values()]
        adata.obs["pos1"] = pos1
        adata.obs["pos2"] = pos2

        fig = plt.figure(figsize=(18, 18))
        fig.subplots_adjust(left=0.09, right=right, top=0.95, bottom=0.1)
        plt.title('Display diagram of cell and cell interaction', fontsize=15)

        plt.axis("off")

        gs = GridSpec(36, 36)
        ax1 = fig.add_subplot(gs[1:18, :17])
        ax2 = fig.add_subplot(gs[1:18, 19:])
        ax3 = fig.add_subplot(gs[19:34, :])

        nx.draw_networkx_nodes(
            g,
            pos=pos,
            node_size=node_size,
            node_color=partition,
            linewidths=linewidths,
            ax=ax1
        )
        # nodes.set_edgecolor("b")
        nx.draw_networkx_edges(
            g,
            pos=pos,
            node_size=node_size,
            edge_color=(0, 0, 0, 0.3),
            width=linewidths,
            ax=ax1
        )

        sns.scatterplot(data=adata.obs, ax=ax2, color=classification_colors, x="pos1", y="pos2", hue="clusters", size=node_size)

        ax2.legend(
            loc="center right",
            bbox_to_anchor=(0.95, 0.5),
            bbox_transform=fig.transFigure,
            fontsize=15
        )

        x = np.arange(len(cell_data["clusters"]))

        ax3.bar(x - 0.15, cell_data["cell_number_percentage"], width=0.3, label="Cell number percentage")
        ax3.bar(x + 0.15, cell_data["cell_degree_percentage"], width=0.3, label="Cell degree percentage")

        ax3.legend()
        ax3.set_xlabel('Cell Types', fontsize=15)
        ax3.set_ylabel('Percentage occupied (%)', fontsize=15)
        ax3.set_xticks(x)
        ax3.set_xticklabels(labels=cell_data["clusters"], rotation=65, fontsize=15)

        # noinspection DuplicatedCode
        if output is not None:
            output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"
            # plt.savefig(output_pdf, dpi=300)
            with PdfPages(output_pdf) as pdf:
                pdf.savefig(fig)

        if show:
            plt.grid(True)
            plt.show()

        plt.close()
