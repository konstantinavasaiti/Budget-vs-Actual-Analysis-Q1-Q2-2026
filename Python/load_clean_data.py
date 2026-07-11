import csv
import sqlite3

conn = sqlite3.connect("data/processed/budget_actual.db")

# Load the budget data into the database
with open("data/raw/budget_2026_H1.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dept_id = conn.execute(
            "SELECT department_id FROM departments WHERE department_name = ?",
            (row["department"],)
        ).fetchone()[0]

        cat_id = conn.execute(
            "SELECT category_id FROM expense_categories WHERE category_name = ?",
            (row["category"],)
        ).fetchone()[0]

        conn.execute(
            "INSERT INTO budgets (department_id, category_id, month, budget_amount) VALUES (?, ?, ?, ?)",
            (dept_id, cat_id, row["month"], row["budgeted_amount"])
        )

conn.commit()
print("Budget data loaded!")

# Load the cleaned actuals data into the database
with open("data/processed/actuals_2026_H1_clean.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dept_id = conn.execute(
            "SELECT department_id FROM departments WHERE department_name = ?",
            (row["department"],)
        ).fetchone()[0]

        cat_id = conn.execute(
            "SELECT category_id FROM expense_categories WHERE category_name = ?",
            (row["category"],)
        ).fetchone()[0]

        conn.execute(
            "INSERT INTO actuals (department_id, category_id, month, actual_amount) VALUES (?, ?, ?, ?)",
            (dept_id, cat_id, row["month"], row["actual_amount"])
        )

conn.commit()
print("Cleaned actuals data loaded!")