# -*- coding: UTF-8 -*-

import os
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pandas import DataFrame

from ykenan_log import Logger

from scLift.util import path, collection

log = Logger("scLift_plot_bar", is_form_file=False)


def bar(
    ax_x: collection,
    ax_y: collection,
    x_name: str = None,
    y_name: str = None,
    title: str = None,
    width: float = 8,
    output: path = None,
    show: bool = True
):
    fig, ax = plt.subplots(figsize=(width, 8))
    fig.subplots_adjust(bottom=0.3)

    if title is not None:
        plt.title(title, fontsize=15)

    ax.bar(ax_x, ax_y)

    if x_name is not None:
        ax.set_xlabel(x_name, fontsize=15)

    if y_name is not None:
        ax.set_ylabel(y_name, fontsize=15)

    ax.set_xticklabels(labels=list(ax_x), rotation=65, fontsize=15)

    # Draw numerical values
    for i, v in enumerate(list(ax_y)):
        plt.text(x=i - 0.1, y=v / 2, s=str(round(v, 4)), rotation=90, color='#FFF', fontsize=15)

    if output is not None:
        output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"
        # plt.savefig(output_pdf, dpi=300)
        with PdfPages(output_pdf) as pdf:
            pdf.savefig(fig)

    if show:
        plt.show()

    plt.close()


def two_bar(
    ax_x: collection,
    ax_y: Tuple,
    x_name: str = None,
    y_name: str = None,
    legend: Tuple = ("1", "2"),
    width: float = 8,
    title: str = None,
    output: path = None,
    show: bool = True
):
    fig, ax = plt.subplots(figsize=(width, 8))
    fig.subplots_adjust(bottom=0.3)

    if title is not None:
        plt.title(title, fontsize=15)

    ax.bar(ax_x, ax_y[0], label=legend[0], color='b')
    ax.bar(ax_x, ax_y[1], bottom=ax_y[0], label=legend[1])

    ax.legend()

    if x_name is not None:
        ax.set_xlabel(x_name, fontsize=15)

    if y_name is not None:
        ax.set_ylabel(y_name, fontsize=15)

    ax.set_xticklabels(labels=list(ax_x), rotation=65, fontsize=15)

    # Draw numerical values
    for i, v in enumerate(list(ax_y[0])):
        plt.text(x=i - 0.2, y=v / 2, s=str(round(v, 5)), rotation=90, color='#FFF', fontsize=15)

    if output is not None:
        output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"
        # plt.savefig(output_pdf, dpi=300)
        with PdfPages(output_pdf) as pdf:
            pdf.savefig(fig)

    if show:
        plt.show()

    plt.close()


def three_bar(
    ax_x: collection,
    ax_y: Tuple,
    x_name: str = None,
    y_name: str = None,
    legend: Tuple = ("1", "2", "3"),
    title: str = None,
    width: float = 8,
    output: path = None,
    show: bool = True
):
    fig, ax = plt.subplots(figsize=(width, 8))

    if title is not None:
        plt.title(title, fontsize=15)

    x = np.arange(len(ax_x))

    ax.bar(x - 0.3, ax_y[0], width=0.3, color="#2ca02c", label=legend[0])
    ax.bar(x, ax_y[1], width=0.3, color="#ff7f0e", label=legend[1])
    ax.bar(x + 0.3, ax_y[2], width=0.3, color="#9467bd", label=legend[2])

    ax.legend()

    if x_name is not None:
        ax.set_xlabel(x_name, fontsize=15)

    if y_name is not None:
        ax.set_ylabel(y_name, fontsize=15)

    ax.set_xticks(x)
    ax.set_xticklabels(labels=list(ax_x), fontsize=15, rotation=65)

    # Draw numerical values
    for i, v in enumerate(list(ax_y[0])):
        plt.text(x=i - 0.35, y=v / 2, s=str(round(v, 5)), rotation=90, color='#111', fontsize=15)

    for i, v in enumerate(list(ax_y[1])):
        plt.text(x=i - 0.05, y=v / 2, s=str(round(v, 5)), rotation=90, color='#111', fontsize=15)

    for i, v in enumerate(list(ax_y[2])):
        plt.text(x=i + 0.25, y=v / 2, s=str(round(v, 5)), rotation=90, color='#111', fontsize=15)

    if output is not None:
        output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"
        # plt.savefig(output_pdf, dpi=300)
        with PdfPages(output_pdf) as pdf:
            pdf.savefig(fig)

    if show:
        plt.show()

    plt.close()


def cluster_method_bar(
    scores: dict,
    width: float = 10,
    plot_output: path = None
):
    data_types: list = list(scores.keys())
    cluster_types: list = list(scores[data_types[0]].keys())

    for cluster_type in cluster_types:
        three_bar(
            ax_x=list(scores.keys()),
            ax_y=(
                [
                    scores[data_types[0]][cluster_type][1],
                    scores[data_types[1]][cluster_type][1],
                    scores[data_types[2]][cluster_type][1],
                    scores[data_types[3]][cluster_type][1]
                ],
                [
                    scores[data_types[0]][cluster_type][2],
                    scores[data_types[1]][cluster_type][2],
                    scores[data_types[2]][cluster_type][2],
                    scores[data_types[3]][cluster_type][2]
                ],
                [
                    scores[data_types[0]][cluster_type][0] / 1000,
                    scores[data_types[1]][cluster_type][0] / 1000,
                    scores[data_types[2]][cluster_type][0] / 1000,
                    scores[data_types[3]][cluster_type][0] / 1000
                ]
            ),
            x_name='Data types',
            y_name='Cluster score',
            legend=("ARI", "AMI", "Calinski harabasz / 1000"),
            title=f"Cluster comparison ({'K-means' if cluster_type == 'k_means' else 'Spectral'})",
            width=width,
            output=os.path.join(plot_output, f"cluster_comparison_{cluster_type}") if plot_output is not None else None,
            show=True
        )


def kl_method_bar(
    scores: dict,
    width: float = 6,
    plot_output: path = None
):
    bar(
        ax_x=list(scores.keys()),
        ax_y=list(scores.values()),
        x_name='Types',
        y_name='KL divergence score',
        title="SNI KL divergence comparison",
        width=width,
        output=os.path.join(plot_output, "sni_kl_divergence_comparison") if plot_output is not None else None,
        show=True
    )


def class_bar(
    df: DataFrame,
    value: str = "rate",
    by: str = "value",
    clusters: str = "clusters",
    width: float = 8,
    title: str = None,
    output: path = None,
    show: bool = True
):
    if output is None and not show:
        log.info(f"At least one of the `output` and `show` parameters is required")
    else:

        df1 = df[df[by] == 1]
        df2 = df[df[by] == 0]

        # Sort
        df1 = df1.sort_values([value], ascending=False)
        df2 = df2.sort_values([value])

        two_bar(
            ax_x=df1[clusters],
            ax_y=(df1[value], df2[value]),
            x_name='Cell Types',
            y_name='Enrichment ratio',
            legend=("Enrichment", "conservative"),
            width=width,
            title=title,
            output=output,
            show=True
        )


def bar_trait(
    trait_df: DataFrame,
    trait_name: str = "All",
    trait_column_name: str = "id",
    value: str = "rate",
    clusters: str = "clusters",
    width: float = 16,
    title: str = None,
    output: path = None,
    show: bool = True
):
    def trait_plot(trait_: str, cell_df_: DataFrame) -> None:
        """
        show plot
        :param trait_: trait name
        :param cell_df_:
        :return: None
        """
        # get gene score
        trait_score = cell_df_[cell_df_[trait_column_name] == trait_]
        # Sort gene scores from small to large
        class_bar(
            df=trait_score,
            value=value,
            clusters=clusters,
            title=f"{title} {trait_}" if title is not None else title,
            width=width,
            output=os.path.join(output, f"cell_{trait_}_enrichment_bar.pdf") if output is not None else None,
            show=show
        )

    trait_list = list(set(trait_df[trait_column_name]))
    # judge trait
    if trait_name != "All" and trait_name not in trait_list:
        log.error(f"The {trait_name} trait/disease is not in the trait/disease list {trait_list}, Suggest modifying the {trait_column_name} parameter information")
        raise ValueError(f"The {trait_name} trait/disease is not in the trait/disease list {trait_list}, Suggest modifying the {trait_column_name} parameter information")

    # plot
    if trait_name == "All":
        for trait in trait_list:
            trait_plot(trait_=trait, cell_df_=trait_df)
    else:
        trait_plot(trait_name, trait_df)
