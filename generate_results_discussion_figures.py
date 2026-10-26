"""
Generate Section VIII discussion figures (not duplicates of Section VII bar charts):
  - figure10_kyber_timing_distribution.png  — box plots of per-iteration operation times
  - figure11_pqc_ecc_tradeoff_scatter.png   — time vs. handshake bytes (Kyber vs ECC baseline)

Requires: same environment as main.py (matplotlib, numpy; optional oqs).

Run: python generate_results_discussion_figures.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Import simulator (does not run main())
from main import simulate_authentication_handshake

OUT = Path(__file__).resolve().parent
DPI = 300
NUM_ITER = 100

# ECC baseline constants — must match create_comparison_chart() in main.py
ECC_MS = {"keygen": 0.5, "encaps": 0.3, "decaps": 0.3}
ECC_PK = 64
ECC_CT = 64


def ecc_handshake_total_ms() -> float:
    """Six timed steps: 2x KeyGen, 2x Encaps, 2x Decaps (literature baseline)."""
    return 2 * ECC_MS["keygen"] + 2 * ECC_MS["encaps"] + 2 * ECC_MS["decaps"]


def ecc_total_handshake_bytes() -> int:
    return 2 * ECC_PK + 2 * ECC_CT


def plot_box(metrics: dict) -> None:
    s = metrics["series"]
    data = [s["keygen_ms"], s["encaps_ms"], s["decaps_ms"]]
    labels = ["KeyGen (avg P/S)", "Encaps (avg P/S)", "Decaps (avg P/S)"]

    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=DPI)
    try:
        bp = ax.boxplot(data, tick_labels=labels, patch_artist=True)
    except TypeError:
        bp = ax.boxplot(data, labels=labels, patch_artist=True)
    for patch in bp["boxes"]:
        patch.set_facecolor("#cfe8f3")
        patch.set_edgecolor("#2E86AB")
    ax.set_ylabel("Time (ms)")
    ax.set_title("Distribution of Kyber-512 operation times over repeated handshakes")
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    fig.text(
        0.5,
        0.01,
        f"N = {NUM_ITER} iterations; paired patient/server averages per operation.",
        ha="center",
        fontsize=8.5,
        style="italic",
        color="#444",
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    path = OUT / "figure10_kyber_timing_distribution.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", path)


def plot_tradeoff(metrics: dict) -> None:
    pk = metrics["public_key_size"]
    ct = metrics["ciphertext_size"]
    bytes_kyber = 2 * pk + 2 * ct
    tot = metrics["series"]["handshake_total_ms"]
    bytes_ecc = ecc_total_handshake_bytes()
    t_ecc = ecc_handshake_total_ms()

    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=DPI)

    # Kyber: show all runs (same x) + mean marker
    xk = np.full(len(tot), bytes_kyber)
    ax.scatter(xk, tot, alpha=0.35, s=28, color="#2E86AB", label="PQC-MFA (Kyber-512), per run", zorder=2)
    ax.scatter(
        [bytes_kyber],
        [float(np.mean(tot))],
        s=120,
        color="#1a5f7a",
        marker="D",
        edgecolors="white",
        linewidths=1.2,
        label="PQC-MFA mean",
        zorder=4,
    )

    ax.scatter(
        [bytes_ecc],
        [t_ecc],
        s=140,
        color="#A23B72",
        marker="o",
        edgecolors="white",
        linewidths=1.2,
        label="ECC baseline (literature)",
        zorder=4,
    )

    ax.set_xlabel("Handshake artifacts (public keys + ciphertexts, bytes)")
    ax.set_ylabel("Total handshake time (ms)")
    ax.set_title("Trade-off: communication size vs. total asymmetric time")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.35)
    fig.text(
        0.5,
        0.02,
        "ECC baseline uses fixed literature timings and compact sizes (not executed in main.py loop).",
        ha="center",
        fontsize=8,
        style="italic",
        color="#555",
    )
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    path = OUT / "figure11_pqc_ecc_tradeoff_scatter.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Wrote", path)


def main():
    print("Running handshake collection (quiet)...")
    m = simulate_authentication_handshake(NUM_ITER, verbose=False)
    if "series" not in m:
        raise RuntimeError("main.simulate_authentication_handshake must return 'series'")
    plot_box(m)
    plot_tradeoff(m)
    print("Done.")


if __name__ == "__main__":
    main()
