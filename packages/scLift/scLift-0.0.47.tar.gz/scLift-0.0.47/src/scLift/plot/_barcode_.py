# -*- coding: UTF-8 -*-
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import ListedColormap
from matplotlib.gridspec import GridSpec
from pandas import DataFrame
from ykenan_log import Logger

from scLift.util import classification_colors, path

log = Logger("scLift_plot_barcode", is_form_file=False)


def barcode_base(
    df: DataFrame,
    cluster_list: list,
    sort_column: str = "value",
    column: str = "clusters",
    trait_column_name: str = "id",
    title: str = None,
    bar_label: str = "TRS",
    output: path = None,
    show: bool = True
):
    # sort
    df_sort = df.sort_values([trait_column_name, sort_column], ascending=False)

    # set index
    class_list = list(set(df_sort[column]))
    id_list = list(set(df_sort[trait_column_name]))
    df_sort["class_index"] = np.zeros(df_sort.shape[0])

    for i in class_list:
        df_sort.loc[df_sort[df_sort[column] == i].index, ["class_index"]] = cluster_list.index(i)

    class_index = np.array(df_sort["class_index"])

    # figure
    fig = plt.figure(figsize=(6, 10))
    fig.subplots_adjust(left=0.03, right=0.97, top=0.99, bottom=0.01)

    plt.axis("off")

    if title is not None:
        plt.title(title)

    gs = GridSpec(10, 10)
    ax1 = fig.add_subplot(gs[:, 1:4])
    ax2 = fig.add_subplot(gs[:, 5:9])

    # span the whole figure
    ax1.set_axis_off()
    ax1.imshow(np.array(class_index).reshape(int(df_sort.shape[0] / len(id_list)), -1), cmap=ListedColormap(classification_colors), aspect='auto', interpolation='nearest')
    # ax1.tick_params(axis='x', rotation=90)

    ax2.set_axis_off()
    im2 = ax2.imshow(np.array(df_sort[sort_column]).reshape(int(df_sort.shape[0] / len(id_list)), -1), cmap="Oranges", aspect='auto', interpolation='nearest')

    color_bar = plt.colorbar(im2, ax=ax2, label=bar_label)
    color_bar.set_label(bar_label, fontsize=15)

    if output is not None:
        output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"
        # plt.savefig(output_pdf, dpi=300)
        with PdfPages(output_pdf) as pdf:
            pdf.savefig(fig)

    if show:
        plt.show()

    plt.close()


def barcode_trait(
    trait_df: DataFrame,
    trait_name: str = "All",
    trait_column_name: str = "id",
    sort_column: str = "value",
    clusters: str = "clusters",
    title: str = None,
    output: path = None,
    show: bool = True
):
    data: DataFrame = trait_df.copy()
    cluster_list = list(set(trait_df[clusters]))

    def trait_plot(trait_: str, atac_cell_df_: DataFrame) -> None:
        """
        show plot
        :param trait_: trait name
        :param atac_cell_df_:
        :return: None
        """
        # get gene score
        trait_score = atac_cell_df_[atac_cell_df_[trait_column_name] == trait_]
        # Sort gene scores from small to large
        barcode_base(
            df=trait_score,
            cluster_list=cluster_list,
            sort_column=sort_column,
            trait_column_name=trait_column_name,
            column=clusters,
            title=f"{title} {trait_}" if title is not None else title,
            output=os.path.join(output, f"cell_{trait_}_score_rank.pdf") if output is not None else None,
            show=show
        )

    # noinspection DuplicatedCode
    trait_list = list(set(data['id']))
    # judge trait
    if trait_name != "All" and trait_name not in trait_list:
        log.error(f"The {trait_name} trait/disease is not in the trait/disease list {trait_list}, Suggest modifying the {trait_column_name} parameter information")
        raise ValueError(f"The {trait_name} trait/disease is not in the trait/disease list {trait_list}, Suggest modifying the {trait_column_name} parameter information")

    # plot
    if trait_name == "All":
        for trait in trait_list:
            trait_plot(trait, trait_df)
    else:
        trait_plot(trait_name, trait_df)
