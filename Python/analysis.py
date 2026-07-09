import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("data/processed/budget_actual.db")

# Read the SQL query from the file
query = """
SELECT
    d.department_name,
    c.category_name,
    b.month,
    b.budget_amount,
    a.actual_amount
FROM budgets b
JOIN actuals a
    ON b.department_id = a.department_id
    AND b.category_id = a.category_id
    AND b.month = a.month
JOIN departments d ON d.department_id = b.department_id
JOIN expense_categories c ON c.category_id = b.category_id
"""

# Execute the query and load the results into a pandas DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Analyze the data
print(df.shape)
print(df.head())

# Calculate variance and variance percentage
df["variance"] = df["actual_amount"] - df["budget_amount"]
df["variance_pct"] = (df["variance"] / df["budget_amount"]) * 100

# Group by department and category to summarize the data
category_summary = df.groupby(["department_name", "category_name"]).agg(
    total_budget=("budget_amount", "sum"),
    total_actual=("actual_amount", "sum"),
).reset_index()

# Calculate variance and variance percentage for the summary
category_summary["variance"] = category_summary["total_actual"] - category_summary["total_budget"]
category_summary["variance_pct"] = (category_summary["variance"] / category_summary["total_budget"]) * 100

# Sort the summary by variance percentage in descending order
category_summary = category_summary.sort_values("variance_pct", ascending=False)

print(category_summary.round(2).to_string(index=False))

# Flag significant variances
THRESHOLD_PCT = 5.0

# Flag significant variances based on the threshold
category_summary["flag"] = category_summary["variance_pct"].apply(
    lambda pct: "SIGNIFICANT" if pd.notna(pct) and abs(pct) >= THRESHOLD_PCT else "normal"
)

# Filter and display significant variances
significant = category_summary[category_summary["flag"] == "SIGNIFICANT"]

print(f"\n--- Αποκλίσεις πάνω από ±{THRESHOLD_PCT}% (χρειάζονται εξήγηση) ---")
print(significant[["department_name", "category_name", "variance_pct"]].round(2).to_string(index=False))
def forecast_department_category(data, department, category, months_ahead=3):
    """
    Παίρνει τα δεδομένα (data), ένα department και μια category,
    και επιστρέφει πρόβλεψη για τους επόμενους 'months_ahead' μήνες,
    βασισμένη σε linear trend πάνω στα ιστορικά actuals.
    """
    # Filter the data for the specified department and category, and sort by month
    subset = data[
        (data["department_name"] == department) & (data["category_name"] == category)
    ].sort_values("month")

    # Check if there are enough data points to perform linear regression
    if subset["actual_amount"].sum() == 0:
        return None

    x = np.arange(len(subset))
    y = subset["actual_amount"].values
    slope, intercept = np.polyfit(x, y, 1)

    future_x = np.arange(len(subset), len(subset) + months_ahead)
    predictions = slope * future_x + intercept

    return {
        "department": department,
        "category": category,
        "slope": slope,
        "forecast": predictions,
    }

import numpy as np

# Forecast Marketing Spend trend using linear regression
marketing_spend = df[
    (df["department_name"] == "Marketing") & (df["category_name"] == "Marketing Spend")
].sort_values("month")

print("\n--- Marketing / Marketing Spend, μηνιαία actuals ---")
print(marketing_spend[["month", "actual_amount"]].to_string(index=False))

# Prepare data for linear regression
x = np.arange(len(marketing_spend))  
y = marketing_spend["actual_amount"].values  

# Fit a linear trend line
slope, intercept = np.polyfit(x, y, 1)

print(f"\nΚλίση (slope): {slope:.2f} € / μήνα")
print(f"Intercept: {intercept:.2f} €")

# Forecast future months (July, August, September 2026)
future_months = np.array([6, 7, 8])
forecast = slope * future_months + intercept

print("\n--- Forecast Q3 2026 (Marketing / Marketing Spend) ---")
for month_num, predicted in zip(["2026-07", "2026-08", "2026-09"], forecast):
    print(f"{month_num}: {predicted:,.2f} €")

# --- Forecast for all department/category combinations ---
combos = df[["department_name", "category_name"]].drop_duplicates()

forecast_results = []

# Loop through each department/category combination and forecast
for _, row in combos.iterrows():
    result = forecast_department_category(df, row["department_name"], row["category_name"])
    if result is not None:
        forecast_results.append(result)

print(f"\n--- Forecast Q3 2026: {len(forecast_results)} από τα {len(combos)} combos ---")
print("(οι υπόλοιποι δεν είχαν καθόλου budget/actuals - π.χ. Marketing Spend σε μη-Marketing departments)\n")

for r in forecast_results:
    total_q3 = sum(r["forecast"])
    trend = "αύξηση" if r["slope"] > 0 else "μείωση"
    print(f"{r['department']:12} {r['category']:16} slope={r['slope']:8.1f} ({trend})   Q3 total: {total_q3:,.2f} €")

# Save the results to CSV files

# 1. Το category-level variance summary 
category_summary.to_csv("data/processed/category_variance_summary.csv", index=False)

# 2. The forecast results for Q3 2026
forecast_rows = []
forecast_month_labels = ["2026-07", "2026-08", "2026-09"]

for r in forecast_results:
    for month_label, predicted_amount in zip(forecast_month_labels, r["forecast"]):
        forecast_rows.append({
            "department": r["department"],
            "category": r["category"],
            "month": month_label,
            "forecast_amount": round(predicted_amount, 2),
            "monthly_slope": round(r["slope"], 2),
        })

forecast_df = pd.DataFrame(forecast_rows)
forecast_df.to_csv("data/processed/q3_forecast.csv", index=False)

print(f"\nΑποθηκεύτηκαν: category_variance_summary.csv ({len(category_summary)} γραμμές)")
print(f"Αποθηκεύτηκαν: q3_forecast.csv ({len(forecast_df)} γραμμές)")