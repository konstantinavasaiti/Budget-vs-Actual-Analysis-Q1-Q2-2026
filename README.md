Budget vs Actual Analysis Q1-Q2 2026
End-to-end FP&A analytics project — SQL data model, Python variance &
forecasting analysis, interactive Power BI dashboard, and an executive
PowerPoint summary for Board reporting. Built to simulate a real
corporate assignment: a CFO asks a Financial Data Analyst to explain
budget variances, identify department patterns, and forecast next
quarter.
> **Note:** all data in this repository is **synthetic**, generated to
> follow realistic patterns (see [`docs/assumptions.md`](docs/assumptions.md)).
> No real company data is used.
The brief
Company: mid-size retail/manufacturing (fictional)
Period: January–June 2026 (Q1 + Q2), 6 departments, 6 expense categories
Questions to answer:
Where did we go over/under budget, and why
Which departments are consistently over/under budget
Monthly trend, not just quarterly totals
Forecast for Q3 2026 based on current run-rate
Project structure
```
data/            raw & processed data, data dictionary
sql/             schema, seed data, variance analysis queries
python/          notebooks + scripts for variance analysis & forecasting
powerbi/         interactive dashboard (+ screenshots since GitHub can't render .pbix)
presentation/    8-10 slide executive summary for the Board
docs/            methodology & assumptions
```
Progress
[x] Milestone 1 — Data Foundation: SQL schema, realistic synthetic
budget & actuals data (Jan-Jun 2026), variance/ranking/running-total
queries. See `sql/` and `data/`.
[ ] Milestone 2 — Python variance analysis & forecast model
[ ] Milestone 3 — Power BI interactive dashboard
[ ] Milestone 4 — Executive summary (PowerPoint) for the Board
Milestone 1 — what's in it
`sql/01_schema.sql` — `departments`, `expense_categories`, `budget`,
`actuals` tables + a `v_budget_vs_actual` view that joins them and
pre-computes variance.
`python/src/generate_data.py` — generates the synthetic dataset
with intentional, realistic storylines (not random noise):
Marketing — a campaign that started on-plan and progressively
overspent through Q2 (up to +35% by June).
IT — a delayed project keeps Equipment/Software actuals
15-30% under budget for most of H1.
Sales — a June sales event drives a sharp one-month spike in
Travel & Other expenses.
Other department/category lines carry only small, unbiased noise.
`sql/03_variance_queries.sql` — variance by department, variance
by department+category, "consistently over/under" detection, monthly
trend, ranking (window function), running/cumulative totals, and a
top-5 worst-variance list.
`data/processed/budget_actual.db` — SQLite build of the above, for
quick local querying without extra setup.
Reproducing the data
```bash
cd python/src
python generate_data.py
```
This regenerates the CSVs, the SQL seed file, and the SQLite DB from the
same seed (42), so results are reproducible.
Tech stack
SQL (SQLite, portable to Postgres/MySQL) · Python (pandas, scikit-learn) ·
Power BI · PowerPoint
License
MIT — see `LICENSE`.
