"""
Shared helpers for the Auspify Netflix Data Analysis project.
Paths, plotting style, cleaned-data loader, and small utilities used by Tasks 1-6.
"""
from pathlib import Path
import json
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")

# ----------------------------------------------------------------- paths
ROOT = Path(__file__).resolve().parent.parent
RAW_CSV = ROOT / "data" / "raw" / "Dataset.csv"
CLEAN_CSV = ROOT / "data" / "processed" / "netflix_cleaned.csv"
CHARTS = ROOT / "outputs" / "charts"
DASH = ROOT / "outputs" / "dashboards"
REPORTS = ROOT / "outputs" / "reports"
METRICS = ROOT / "outputs" / "metrics"
SHOTS = ROOT / "outputs" / "screenshots"
for _p in (CHARTS, DASH, REPORTS, METRICS, SHOTS, CLEAN_CSV.parent):
    _p.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------- style
RED, DARK, GREY, LIGHT = "#E50914", "#221F1F", "#6B6B6B", "#F5F5F1"
PALETTE = {"Movie": RED, "TV Show": DARK}
SEQ = ["#E50914", "#B20710", "#831010", "#564D4D", "#221F1F"]


def set_style():
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update({
        "figure.dpi": 110, "savefig.dpi": 160, "savefig.bbox": "tight",
        "axes.titlesize": 13, "axes.titleweight": "bold", "axes.labelsize": 10.5,
        "axes.spines.top": False, "axes.spines.right": False,
        "font.family": "DejaVu Sans", "axes.edgecolor": "#BBBBBB",
    })


set_style()


def save_fig(fig, name, folder=CHARTS):
    """Save a matplotlib figure to outputs/charts (or given folder) and close it."""
    path = folder / f"{name}.png"
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    print(f"  saved -> {path.relative_to(ROOT)}")
    try:                                    # inside Jupyter: also show the chart inline
        from IPython import get_ipython
        if get_ipython() is not None:
            from IPython.display import Image, display
            display(Image(filename=str(path), width=900))
    except Exception:
        pass
    return path


def label_bars(ax, fmt="{:,.0f}", pad=3, size=9):
    for c in ax.containers:
        labels = [fmt.format(v) if v else "" for v in c.datavalues]
        ax.bar_label(c, labels=labels, padding=pad, fontsize=size, color="#333")


def save_metrics(task, data):
    path = METRICS / f"{task}_metrics.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))
    return path


def load_metrics(task):
    with open(METRICS / f"{task}_metrics.json") as f:
        return json.load(f)


def write_report(name, text):
    path = REPORTS / name
    path.write_text(text, encoding="utf-8")
    print(f"  report -> {path.relative_to(ROOT)}")
    return path


# ------------------------------------------------------------ data loader
def load_clean():
    """Load the cleaned dataset produced by Task 1 with correct dtypes."""
    if not CLEAN_CSV.exists():
        raise FileNotFoundError("Run Task 1 first (src/task1_data_cleaning.py) to create the cleaned dataset.")
    return pd.read_csv(CLEAN_CSV, parse_dates=["date_added"])


def explode_multi(df, col, new=None):
    """Split a comma separated column into one row per value."""
    new = new or col
    out = df.assign(**{new: df[col].str.split(",")}).explode(new)
    out[new] = out[new].str.strip()
    return out


def pct(n, d, nd=1):
    return round(100 * n / d, nd) if d else 0.0
