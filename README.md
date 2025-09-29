# Student Retention Dashboard (Python + Plotly)

Generates a 2x2 interactive dashboard from CSV/JSON data:
- KPI + composition bar (top-left)
- Retention by school (top-right)
- Top withdrawal reasons (pie) (bottom-left)
- District withdrawals (stacked bars) (bottom-right)

Tech: Python 3.10+, Pandas, Plotly

## Quickstart
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/viz.py
open outputs/retention_dashboard_preview.html  # macOS

## Project layout
data/      input CSV/JSON
scripts/   viz.py (builds dashboard)
outputs/   generated HTML
