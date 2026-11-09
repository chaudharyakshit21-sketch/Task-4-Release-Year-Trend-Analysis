"""Run this task:  python run.py"""
import subprocess, sys
from pathlib import Path
subprocess.run([sys.executable, "task4_trend_analysis.py"], cwd=Path(__file__).resolve().parent / "src", check=True)
