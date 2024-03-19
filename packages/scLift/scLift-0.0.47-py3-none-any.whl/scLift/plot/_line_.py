# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

from ykenan_log import Logger

from scLift.util import path, collection

log = Logger("scLift_plot_line", is_form_file=False)


def loss_line(
    values: collection,
    is_log: bool = True,
    output: path = None,
    show: bool = True
) -> None:
    if output is None and not show:
        log.info(f"At least one of the `output` and `show` parameters is required")
    else:

        # data
        times = range(1, len(values) + 1)
        data = pd.DataFrame()
        data["Loss value"] = np.log1p(values) if is_log else values
        data.index = times

        fig, ax = plt.subplots(figsize=(16, 8))
        plt.xlabel('Iterations')
        plt.ylabel('log1p(Loss value)')

        sns.set_theme(style="whitegrid")

        sns.lineplot(data=data, palette="tab10", linewidth=2.5)

        if output is not None:
            output_pdf = output if output.endswith(".pdf") else f"{output}.pdf"
            # plt.savefig(output_pdf, dpi=300)
            with PdfPages(output_pdf) as pdf:
                pdf.savefig(fig)

        if show:
            plt.show()

        plt.close()
