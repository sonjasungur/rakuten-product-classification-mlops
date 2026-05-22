import os
import pandas as pd

REFERENCE_DATA = "data/sample/rakuten_sample.csv"
CURRENT_DATA = "data/sample/rakuten_sample_current.csv"
REPORT_PATH = "reports/evidently_report.html"

os.makedirs("reports", exist_ok=True)

reference_df = pd.read_csv(REFERENCE_DATA)
current_df = pd.read_csv(CURRENT_DATA)

ref_counts = reference_df["category"].value_counts(normalize=True).round(3)
cur_counts = current_df["category"].value_counts(normalize=True).round(3)

all_categories = sorted(set(ref_counts.index).union(set(cur_counts.index)))

rows = ""
for category in all_categories:
    ref_value = ref_counts.get(category, 0)
    cur_value = cur_counts.get(category, 0)
    drift = round(abs(cur_value - ref_value), 3)

    rows += f"""
    <tr>
        <td>{category}</td>
        <td>{ref_value}</td>
        <td>{cur_value}</td>
        <td>{drift}</td>
    </tr>
    """

html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Rakuten Data Drift Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e5e7eb;
            padding: 40px;
        }}
        .card {{
            background: #111827;
            border: 1px solid #334155;
            border-radius: 18px;
            padding: 28px;
            max-width: 1000px;
            margin: auto;
        }}
        h1 {{
            color: #38bdf8;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 24px;
        }}
        th, td {{
            border-bottom: 1px solid #334155;
            padding: 14px;
            text-align: left;
        }}
        th {{
            color: #93c5fd;
        }}
        .badge {{
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            background: #0f766e;
            color: white;
            font-size: 13px;
        }}
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">MLOps Monitoring</span>
        <h1>Rakuten Data Drift Report</h1>
        <p>
            This report compares reference and current product category distributions
            to identify potential data drift in the classification pipeline.
        </p>

        <h2>Dataset Summary</h2>
        <ul>
            <li>Reference rows: {len(reference_df)}</li>
            <li>Current rows: {len(current_df)}</li>
            <li>Compared feature: category</li>
        </ul>

        <h2>Category Distribution Drift</h2>
        <table>
            <thead>
                <tr>
                    <th>Category</th>
                    <th>Reference Share</th>
                    <th>Current Share</th>
                    <th>Absolute Drift</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>

        <p style="margin-top: 30px; color: #94a3b8;">
            Demo report generated for a production-oriented MLOps monitoring workflow.
        </p>
    </div>
</body>
</html>
"""

with open(REPORT_PATH, "w") as f:
    f.write(html)

print(f"Drift report saved to {REPORT_PATH}")