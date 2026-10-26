"""
Scyther formal verification results as an IEEE-style table figure (PNG).
Run: python generate_scyther_verification_table.py

Outputs:
  - scyther_verification_table.png
  - scyther_verification_table.csv (same data, for Word/Excel)
"""
from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
DPI = 300

ROWS = [
    ("1", "Patient", "Alive_Patient1", "Ok", "[proof of correctness]"),
    ("2", "Patient", "Weakagree_Patient2", "Ok", "[proof of correctness]"),
    ("3", "Patient", "Niagree_Patient3", "Ok", "[proof of correctness]"),
    ("4", "Patient", "Nisynch_Patient4", "Ok", "[proof of correctness]"),
    ("5", "Server", "Alive_Server1", "Ok", "[proof of correctness]"),
    ("6", "Server", "Weakagree_Server2", "Ok", "[proof of correctness]"),
    ("7", "Server", "Niagree_Server3", "Ok", "[proof of correctness]"),
    ("8", "Server", "Nisynch_Server4", "Ok", "[proof of correctness]"),
]


def main():
    fig, ax = plt.subplots(figsize=(9.2, 4.8), dpi=DPI)
    ax.axis("off")

    col_labels = ["#", "Role", "Scyther claim", "Result", "Note"]

    cell_text = [[r[0], r[1], r[2], r[3], r[4]] for r in ROWS]

    table = ax.table(
        cellText=cell_text,
        colLabels=col_labels,
        loc="center",
        cellLoc="center",
        colWidths=[0.06, 0.12, 0.38, 0.1, 0.28],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.05, 2.05)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#2c3e50")
        cell.set_linewidth(0.8)
        if row == 0:
            cell.set_facecolor("#1b5e56")
            cell.get_text().set_color("white")
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor("#f8fafb" if row % 2 == 1 else "#ffffff")

    ax.text(0.5, 0.97, "TABLE — Scyther Formal Verification (Protocol: PQC-MFA)", transform=ax.transAxes, ha="center", fontsize=11, fontweight="bold")
    ax.text(
        0.5, 0.03,
        "Model: Dolev–Yao adversary.  Summary: all 8 claims verified; no attacks found within state-space bounds.",
        transform=ax.transAxes, ha="center", fontsize=8.5, style="italic", color="#444",
    )

    out = OUT / "scyther_verification_table.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", out)

    csv_path = OUT / "scyther_verification_table.csv"
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("#,Role,Scyther claim,Result,Note\n")
        for r in ROWS:
            f.write(",".join(r) + "\n")
    print("Wrote", csv_path)


if __name__ == "__main__":
    main()
