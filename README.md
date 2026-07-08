# 📊 Budget vs Actual Analysis Q1-Q2 2026

End-to-end FP&A analytics project: SQL data model, Python analysis,
Power BI dashboard, and executive PowerPoint summary — simulating a
real Budget vs Actual assignment for a mid-size retail/manufacturing
company (Jan-Jun 2026, 6 departments).

> ⚠️ **Note:** all data is synthetic, built to follow realistic patterns
> (not random). No real company data is used.

## 🚧 Status
Milestone 1 (Data Foundation) complete. Starting Milestone 2 (Python analysis & forecast).

## 📁 Structure so far

data/raw/budget_2026.csv         → budgeted amount per department/category/month
data/raw/actuals_2026.csv        → actual amount per department/category/month
data/processed/budget_actual.db  → SQLite database with loaded data
SQL/01_schema.sql                → database schema (departments, categories, budgets, actuals)
SQL/02_seed_data.sql             → departments & categories reference data
SQL/03_variance_queries.sql      → variance analysis queries
Python/load_data.py              → loads CSV data into the database
Python/run_queries.py            → runs SQL queries against the database

## 🗺️ Roadmap
- [x] 📥 Raw data (budget + actuals, Jan-Jun 2026)
- [x] 🗄️ SQL schema & variance queries
  - [x] Overall variance per department
  - [x] Monthly trend per department
  - [x] Consistently over/under budget detection
  - [x] Variance ranking (%)
- [ ] 🐍 Python variance analysis & forecast
- [ ] 📊 Power BI interactive dashboard
- [ ] 📽️ Executive summary (PowerPoint) for the Board

## 🔎 Key findings so far
- **Marketing** is over budget in **6/6 months** tracked (+6.78% overall) — a campaign that progressively overspent.
- **IT** is under budget in **6/6 months** tracked (-5.75% overall) — a delayed project.
- Other departments (Sales, Operations, HR, R&D) show no consistent pattern.

## 🏢 Context
- Departments: Sales, Marketing, Operations, R&D, HR, IT
- Categories: Salaries, Marketing Spend, Travel, Software, Equipment, Other
- Period: January–June 2026
