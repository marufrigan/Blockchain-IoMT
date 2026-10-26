"""
Generate a stylized Fig. 6 style graphic for Scyther verification results (IEEE-friendly).
Output: figure6_scyther_verification_stylish.png
Run: python generate_scyther_figure_stylish.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent
DPI = 300

# IEEE-friendly palette: mostly grayscale + one accent
BG = "#fafbfc"
CARD = "#ffffff"
ACCENT = "#0d6e5c"
ACCENT_LIGHT = "#e8f4f1"
TEXT = "#1a1a1a"
MUTED = "#5c6370"
BORDER = "#d8dee9"


def main():
    fig = plt.figure(figsize=(8.2, 6.2), dpi=DPI, facecolor=BG)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Outer card
    fig.patches.append(
        FancyBboxPatch(
            (0.06, 0.06), 0.88, 0.88, boxstyle="round,pad=0.008,rounding_size=0.02",
            transform=ax.transAxes, facecolor=CARD, edgecolor=BORDER, linewidth=1.2,
        )
    )

    # Header strip
    fig.patches.append(
        FancyBboxPatch(
            (0.06, 0.82), 0.88, 0.12, boxstyle="round,pad=0.008,rounding_size=0.02",
            transform=ax.transAxes, facecolor=ACCENT, edgecolor="none",
        )
    )
    ax.text(0.5, 0.905, "Scyther Formal Verification Results", transform=ax.transAxes,
            ha="center", va="center", fontsize=14, fontweight="bold", color="white")
    ax.text(0.5, 0.865, "Protocol: PQC-MFA", transform=ax.transAxes,
            ha="center", va="center", fontsize=10.5, color="#e8fff8")

    # Two role cards
    def role_card(x0, title, claims):
        w, h = 0.38, 0.52
        fig.patches.append(
            FancyBboxPatch(
                (x0, 0.22), w, h, boxstyle="round,pad=0.006,rounding_size=0.015",
                transform=ax.transAxes, facecolor=ACCENT_LIGHT, edgecolor=ACCENT, linewidth=1.0,
            )
        )
        ax.text(x0 + w / 2, 0.69, title, transform=ax.transAxes, ha="center", va="center",
                fontsize=11, fontweight="bold", color=ACCENT)
        y = 0.635
        for line in claims:
            ax.text(x0 + 0.04, y, "✓", transform=ax.transAxes, fontsize=11, color=ACCENT, va="top")
            ax.text(x0 + 0.085, y, line, transform=ax.transAxes, fontsize=9.2, color=TEXT, va="top",
                    family="monospace")
            y -= 0.055

    role_card(
        0.12,
        "Patient role",
        [
            "Alive_Patient1  [proof of correctness]",
            "Weakagree_Patient2  [proof of correctness]",
            "Niagree_Patient3  [proof of correctness]",
            "Nisynch_Patient4  [proof of correctness]",
        ],
    )
    role_card(
        0.50,
        "Server role",
        [
            "Alive_Server1  [proof of correctness]",
            "Weakagree_Server2  [proof of correctness]",
            "Niagree_Server3  [proof of correctness]",
            "Nisynch_Server4  [proof of correctness]",
        ],
    )

    # Footer summary box
    fig.patches.append(
        FancyBboxPatch(
            (0.12, 0.08), 0.76, 0.10, boxstyle="round,pad=0.006,rounding_size=0.012",
            transform=ax.transAxes, facecolor="#f0f7f5", edgecolor=ACCENT, linewidth=0.9,
        )
    )
    ax.text(
        0.5, 0.135,
        "RESULT: All 8 security claims verified  ·  No attacks found (within state-space bounds)",
        transform=ax.transAxes, ha="center", va="center", fontsize=9.5, color=TEXT, fontweight="bold",
    )
    ax.text(
        0.5, 0.098,
        "Symbolic model: Dolev–Yao adversary  ·  Claims include aliveness, agreement, and synchronization",
        transform=ax.transAxes, ha="center", va="center", fontsize=8.2, color=MUTED, style="italic",
    )

    out = OUT / "figure6_scyther_verification_stylish.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print("Wrote", out)


if __name__ == "__main__":
    main()
