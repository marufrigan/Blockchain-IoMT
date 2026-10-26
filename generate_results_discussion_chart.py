"""
Consolidated results figure for Section VIII (discussion): KEM time + size in one view.
Uses same representative values as main.py comparison chart.
Run: python generate_results_discussion_chart.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
DPI = 300

KYBER_MS = (0.04, 0.05, 0.06)
ECC_MS = (0.50, 0.30, 0.30)
KYBER_BYTES = (800, 768)
ECC_BYTES = (64, 64)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2), dpi=DPI)
    w = 0.35
    ops = ["KeyGen", "Encaps", "Decaps"]
    x = np.arange(len(ops))
    axes[0].bar(x - w / 2, KYBER_MS, w, label="PQC-MFA (Kyber-512)", color="#2E86AB", alpha=0.9)
    axes[0].bar(x + w / 2, ECC_MS, w, label="Standard ECC", color="#A23B72", alpha=0.85)
    axes[0].set_ylabel("Time (ms)")
    axes[0].set_xlabel("Operation")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(ops)
    axes[0].set_title("(a) Computational cost")
    axes[0].legend(fontsize=8)
    axes[0].grid(axis="y", alpha=0.3, linestyle="--")

    labels = ["Public key", "Ciphertext"]
    x2 = np.arange(2)
    axes[1].bar(x2 - w / 2, KYBER_BYTES, w, label="PQC-MFA (Kyber-512)", color="#2E86AB", alpha=0.9)
    axes[1].bar(x2 + w / 2, ECC_BYTES, w, label="Standard ECC", color="#A23B72", alpha=0.85)
    axes[1].set_ylabel("Size (bytes)")
    axes[1].set_xlabel("Component")
    axes[1].set_xticks(x2)
    axes[1].set_xticklabels(labels)
    axes[1].set_title("(b) Communication cost")
    axes[1].legend(fontsize=8)
    axes[1].grid(axis="y", alpha=0.3, linestyle="--")

    fig.suptitle(
        "Results snapshot: operational efficiency vs bandwidth trade-off",
        fontsize=12,
        fontweight="bold",
        y=1.02,
    )
    fig.text(
        0.5,
        -0.02,
        "Representative baseline aligned with the evaluation harness; interpret alongside formal verification (Section VI).",
        ha="center",
        fontsize=8.5,
        style="italic",
        color="#444",
    )

    out = OUT / "figure_results_discussion_summary.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", out)


if __name__ == "__main__":
    main()
