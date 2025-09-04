import matplotlib.pyplot as plt
import os
from .resource_path import superpos_equations

def gen_equations_combined():
    plt.rcParams['font.size'] = 8
    equations = [
        r"$1\text{ qubit system: } \quad \psi = \alpha|0\rangle + \beta|1\rangle$",
        r"$2\text{ qubit system: } \quad \psi = \alpha_0|00\rangle + \alpha_1|01\rangle + \alpha_2|10\rangle + \alpha_3|11\rangle$",
        r"$3\text{ qubit system: } \quad \psi = \alpha_0|000\rangle + \alpha_1|001\rangle + \alpha_2|010\rangle + \alpha_3|011\rangle + \cdots$"
    ]

    fig, ax = plt.subplots(figsize=(2.5, 1))
    ax.axis("off")

    for i, eq in enumerate(equations):
        ax.text(0.5, 0.85 - i * 0.3, eq, ha="center", va="center")

    # ✅ Resolve resource folder relative to this file
    out_path = superpos_equations()

    plt.savefig(out_path, bbox_inches="tight", dpi=150, transparent=True)
    plt.close()

    # return out_path
