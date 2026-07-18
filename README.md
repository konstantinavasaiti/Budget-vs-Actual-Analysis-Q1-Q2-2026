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
- [x] 🐍 Python variance analysis & forecast
- [x] 📊 Power BI interactive dashboard
- [ ] 📽️ Executive summary (PowerPoint) for the Board

## 🔎 Key findings so far
- **Marketing** is over budget in **6/6 months** tracked (+6.78% overall) — a campaign that progressively overspent.
- **IT** is under budget in **6/6 months** tracked (-5.75% overall) — a delayed project.
- Other departments (Sales, Operations, HR, R&D) show no consistent pattern.

## 🧹 Data quality note
All data in this project is synthetic, generated programmatically
(`Python/load_data.py` + the data generation script) to follow
realistic patterns rather than random noise. Because the data is
synthetic and clean by construction, no data-cleaning step was
required before loading it into the database — there are no missing
values, duplicate records, or inconsistent naming in the source CSVs.

This is called out explicitly (rather than left unstated) because in
a real engagement, the CFO/Board would rightly ask "how reliable are
these numbers?" — and the answer here is: fully reliable, because the
data is synthetic and was validated end-to-end (216 budget rows +
216 actuals rows, confirmed via `SELECT COUNT(*)` after loading — see
commit history).

## 🧹 Data Cleaning

The raw actuals export (`data/raw/actuals_2026_H1_raw.csv`) simulates a
real ERP export with intentional data quality issues. Diagnosed and
resolved in `Python/clean_data.py`, with each step counted and verified
before/after — including a raw-file recount after an initial mismatch
was flagged during review (see "Row count verification" below).

**Note on row count:** the raw export includes only the 32 valid
department×category combinations (6 departments × 6 categories, minus
the 4 combinations with zero base budget, e.g. HR/Marketing Spend,
which are omitted entirely rather than recorded as €0.00). 32 combos ×
6 months = 192 base rows + 1 duplicate = **193 raw rows**. Verified via
`wc -l` and `df.groupby(['department','category']).size()` directly on
the source file.

**1. Inconsistent department names**
6 unique values for department, but 3 were malformed: `'IT '` (trailing
space), `'operations'` (lowercase), `'Marketing '` (trailing space).
Fixed via an explicit mapping (not `.str.title()`, which incorrectly
turns acronyms like "HR"/"IT" into "Hr"/"It"). Verified via `repr()`
and `len()` checks on each unique value.

**2. Duplicate row**
One fully duplicated row was found via `.duplicated()` and removed —
kept the first occurrence only.

**3. Missing values**
4 rows had a blank `actual_amount` (unrecorded invoices at export time).
These were **dropped**, not imputed with 0 or an average — the true
value is unknown, and guessing it would misrepresent actual spend.

**4. Currency symbols**
Some amounts were stored as strings with a trailing `€` (e.g. `"44048.7€"`).
Stripped the symbol and converted to numeric via `pd.to_numeric(errors="coerce")`.

**Result:** 193 raw rows → **188 clean rows** used in the final analysis
(`data/processed/actuals_2026_H1_clean.csv`).

**Row count verification:** an initial cleaning pass was run against a
version of the raw file that included the 4 zero-budget combinations
explicitly (yielding 217 raw rows). This was flagged during review as
inconsistent with how the source file was actually built, re-verified
directly against the raw file (`wc -l`, `len(df)`,
`groupby(['department','category']).size()`), and corrected — the raw
file was regenerated to omit zero-budget combinations entirely (193
rows), and the full pipeline (cleaning → load → analysis) was re-run
against the corrected source.

**Impact on findings:** the significant deviations (±5% threshold) are
consistent across both versions of the cleaning pass — Marketing/Marketing
Spend (+20.45%), Sales/Travel (+12.01%), Operations/Equipment (+10.45%),
HR/Salaries (-5.74%), HR/Software (-6.51%), IT/Software (-18.13%), and
IT/Equipment (-18.17%). Two of these — HR/Salaries and HR/Software —
only became visible after proper cleaning; they were not flagged in the
earlier, uncleaned synthetic dataset.

## 🏢 Context
- Departments: Sales, Marketing, Operations, R&D, HR, IT
- Categories: Salaries, Marketing Spend, Travel, Software, Equipment, Other
- Period: January–June 2026
