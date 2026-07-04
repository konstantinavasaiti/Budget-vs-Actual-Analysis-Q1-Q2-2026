import sqlite3

conn = sqlite3.connect("data/processed/budget_actual.db")

with open("sql/03_variance_queries.sql", encoding="utf-8") as f:
    query = f.read()

for row in conn.execute(query):
    print(row)