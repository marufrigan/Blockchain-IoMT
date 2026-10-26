"""
Generate Section 5 assets: Fig. 4, Fig. 5, Table 3 (PNG) for IEEE-style manuscript.
Run: python generate_section5_figures.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parent
DPI = 300


def fig4_simulation_workflow():
    """Matches main.py: only Kyber is timed in a loop; ECC is a constant dict at chart time."""
    fig, ax = plt.subplots(figsize=(10, 7.4), dpi=DPI)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10.5)
    ax.axis("off")

    def box(x, y, w, h, text, fs=8.5, dashed=False):
        p = FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.15",
            linewidth=1.2, edgecolor="black", facecolor="#f0f4f8",
            linestyle="--" if dashed else "solid",
        )
        ax.add_patch(p)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, wrap=True)

    ax.text(
        5, 10.15, "Simulation workflow / system execution pipeline (aligned with main.py)",
        ha="center", fontsize=12, fontweight="bold",
    )

    box(0.2, 8.85, 2.3, 0.95, "Input:\nnum_iterations = 100\n(in main())", fs=8.5)
    box(2.75, 8.85, 4.5, 0.95, "main() calls\nsimulate_authentication_handshake()\nthen create_comparison_chart()", fs=7.8)
    box(7.55, 8.85, 2.25, 0.95, "If import oqs:\nliboqs Kyber512;\nelse KyberSimulator", fs=7.8)

    box(
        0.3, 6.5, 4.4, 1.95,
        "LOOP only here (N iterations)\nKyber-512: patient_kyber & server_kyber\nKeyEncapsulation('Kyber512') or simulator\nmeasure_keygen, encapsulate, decapsulate\n(bidirectional KEM messages)",
        fs=7.9,
    )
    box(
        5.1, 6.5, 4.6, 1.95,
        "NOT executed — literature constants\n ecc_metrics inside\ncreate_comparison_chart():\n0.5 ms KeyGen; 0.3 ms Encaps/Decaps;\n64 B public key; 64 B ciphertext\nUsed only for bar-chart labels.",
        fs=7.5,
        dashed=True,
    )

    box(
        1.0, 4.75, 8.0, 1.2,
        "Returns kyber_metrics: avg KeyGen/Encaps/Decaps, σ; pk & ciphertext byte sizes\n(from simulate_authentication_handshake)",
        fs=8.2,
    )

    box(
        0.8, 2.95, 8.4, 1.45,
        "create_comparison_chart(kyber_metrics):\nmatplotlib bars — Kyber from measured/simulated loop;\nECC from fixed ecc_metrics (no ECC cryptography run)",
        fs=8,
    )

    box(0.8, 1.05, 3.8, 1.15, "Stdout:\nPERFORMANCE METRICS\n(mean ± stdev)", fs=8.5)
    box(5.2, 1.05, 4.0, 1.15, "File:\npqc_mfa_performance_comparison.png\n(savefig dpi=300)", fs=8.2)

    arrows = [
        ((1.25, 8.85), (2.4, 8.45)),
        ((5.0, 8.85), (5.0, 8.45)),
        ((8.7, 8.85), (7.7, 8.45)),
        ((2.5, 6.5), (4.2, 5.95)),
        ((7.5, 6.5), (5.8, 5.95)),
        ((5.0, 6.5), (5.0, 5.95)),
        ((5.0, 4.75), (5.0, 4.4)),
        ((5.0, 2.95), (2.9, 2.2)),
        ((5.0, 2.95), (7.1, 2.2)),
    ]
    for (x1, y1), (x2, y2) in arrows:
        ax.annotate(
            "", xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", color="#333", lw=1.1),
        )

    fig.savefig(OUT / "figure4_simulation_workflow.png", dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", OUT / "figure4_simulation_workflow.png")


def fig5_implementation_modes():
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=DPI)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def panel(x0, title, lines, color):
        ax.add_patch(
            FancyBboxPatch(
                (x0, 1.2), 4.6, 5.8, boxstyle="round,pad=0.02,rounding_size=0.2",
                linewidth=1.5, edgecolor=color, facecolor="#fafafa",
            )
        )
        ax.text(x0 + 2.3, 6.7, title, ha="center", fontsize=11, fontweight="bold", color=color)
        y = 5.9
        for line in lines:
            ax.text(x0 + 0.25, y, line, fontsize=9, va="top")
            y -= 0.55

    panel(
        0.35,
        "Mode A: liboqs (real measurements)",
        [
            "• import oqs; Kyber512 via liboqs-python",
            "• KeyGen / Encaps / Decaps timed on this CPU",
            "• Byte sizes from live Kyber512 objects",
            "• Label: REAL (measured with liboqs)",
        ],
        "#1a5276",
    )
    panel(
        5.15,
        "Mode B: literature-based fallback",
        [
            "• oqs not installed → KyberSimulator class",
            "• NIST-accurate pk/ct sizes (800 / 768 B)",
            "• Timings from published CPU benchmarks",
            "• Label: LITERATURE-BASED",
        ],
        "#7d3c98",
    )
    ax.annotate(
        "main.py selects mode at import",
        xy=(5, 0.75), ha="center", fontsize=10, style="italic",
    )
    ax.text(5, 7.5, "Implementation modes for performance evaluation", ha="center", fontsize=12, fontweight="bold")

    fig.savefig(OUT / "figure5_implementation_modes.png", dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", OUT / "figure5_implementation_modes.png")


def table3_parameters():
    """Table 3 as a publication-style PNG (matches main.py behavior)."""
    fig, ax = plt.subplots(figsize=(9.8, 5.0), dpi=DPI)
    ax.axis("off")

    col_labels = [
        "Parameter",
        "Kyber-512\n(ML-KEM, sim.)",
        "ECC baseline\n(P-256 style, lit.)",
        "Notes",
    ]
    rows = [
        ["Security target λ (classical bits)", "≈128", "≈128", "Comparison narrative only"],
        ["KEM public key size (bytes)", "800", "64", "KyberSimulator / oqs; ecc_metrics in chart"],
        ["KEM private key size (bytes)", "1632", "32", "Simulator; ECC sk not used in code"],
        ["KEM ciphertext (bytes)", "768", "64", "Measured or simulator"],
        ["Shared secret (bytes)", "32", "32", "oqs / simulator output"],
        ["Timed handshake loop", "Yes (N = 100)", "No", "Only Kyber in simulate_…()"],
        ["ECC baseline timing", "—", "Hardcoded 0.5 / 0.3 ms", "ecc_metrics dict; not measured"],
        ["Digital signatures (ML-DSA / ECDSA)", "Not implemented", "Not implemented", "main.py is KEM-only"],
        ["Fig. 5 data mode", "liboqs or literature", "—", "Applies to Kyber path only"],
    ]

    table = ax.table(
        cellText=rows,
        colLabels=col_labels,
        loc="center",
        cellLoc="center",
        colWidths=[0.28, 0.2, 0.22, 0.28],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1.05, 1.75)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#333")
        if row == 0:
            cell.set_facecolor("#e8eef4")
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor("#ffffff")

    ax.text(0.5, 0.98, "TABLE III", transform=ax.transAxes, ha="center", fontsize=10, fontweight="bold")
    ax.text(
        0.5, 0.93,
        "Experimental parameters and cryptographic settings",
        transform=ax.transAxes, ha="center", fontsize=11, fontweight="bold",
    )
    ax.text(
        0.5, 0.04,
        "ECC column reflects constants in create_comparison_chart() for visualization; no elliptic-curve primitives are executed.",
        transform=ax.transAxes, ha="center", fontsize=7.5, style="italic",
    )

    fig.savefig(OUT / "table3_experimental_parameters.png", dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", OUT / "table3_experimental_parameters.png")


if __name__ == "__main__":
    fig4_simulation_workflow()
    fig5_implementation_modes()
    table3_parameters()
