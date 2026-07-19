# 📊 Budget vs Actual Analysis Q1–Q2 2026

End-to-end FP&A analytics project simulating a real-world **Budget vs Actual** analysis for a mid-size retail/manufacturing company.

The project covers the complete analytics workflow—from data generation and cleaning to SQL modeling, Python analysis, and an interactive Power BI dashboard.

> ⚠️ **Note:** All data is synthetic, designed to follow realistic business patterns. No real company data is used.

---

# 🚧 Project Status

- ✅ Data generation
- ✅ SQL database & variance queries
- ✅ Data cleaning & validation
- ✅ Python variance analysis
- ✅ Power BI interactive dashboard
- 🔄 Executive PowerPoint presentation (in progress)

---

# 📁 Project Structure

```text
data/
├── raw/
│   ├── budget_2026.csv
│   ├── actuals_2026.csv
│   └── actuals_2026_H1_raw.csv
│
├── processed/
│   ├── actuals_2026_H1_clean.csv
│   └── budget_actual.db

SQL/
├── 01_schema.sql
├── 02_seed_data.sql
└── 03_variance_queries.sql

Python/
├── clean_data.py
├── load_data.py
└── run_queries.py

Power BI/
└── Budget_Performance_Dashboard.pbix
```

---

# 📊 Power BI Dashboard

The interactive dashboard was built using a **star schema** data model and includes:

- Executive KPI cards
- Department variance analysis
- Monthly variance trends
- Department & category drill-down
- Threshold alert report (±5%)
- Interactive filtering and drill-through navigation

> *(Dashboard screenshot here)*

---

# 🗺️ Project Roadmap

- ✅ Raw data generation
- ✅ SQL data model
- ✅ Data cleaning & validation
- ✅ Python analysis
- ✅ Power BI dashboard
- 🔄 Executive PowerPoint presentation

---

# 🔎 Key Findings

- Marketing remained over budget throughout the six-month period (+6.78% overall), indicating sustained campaign overspending.
- IT remained under budget (-5.75% overall), primarily due to delayed software and equipment investments.
- Seven department-category combinations exceeded the ±5% variance threshold.
- Sales, Operations, HR, and R&D remained broadly aligned with planned spending, with only isolated category-level deviations.

---

# 🧹 Data Cleaning

The raw ERP export (`actuals_2026_H1_raw.csv`) intentionally contains realistic data quality issues to simulate a production environment.

Cleaning steps included:

- Standardizing inconsistent department names
- Removing duplicate records
- Dropping incomplete transactions
- Converting currency-formatted text into numeric values

Result:

**193 raw rows → 188 clean rows**

used throughout the final SQL, Python and Power BI analysis.

---

# ✅ Row Count Verification

The raw dataset was independently verified before cleaning using multiple validation methods (`wc -l`, `len(df)` and grouped record counts).

After cleaning:

- Duplicate records removed
- Missing actual values excluded
- Final dataset validated before loading into SQLite and Power BI

This audit trail mirrors the validation process expected in real FP&A projects.

---

# 🏗️ Data Model

The Power BI report follows a **star schema** consisting of:

### Fact Tables

- Budget
- Actual

### Dimension Tables

- Department
- Category
- Date

Relationships are configured as **many-to-one** to support efficient filtering and reporting.

---

# ⚠️ Power BI Implementation Note

During dashboard development, imported numeric values were initially interpreted using an incorrect locale, resulting in financial amounts approximately ten times larger than expected.

The issue was identified by validating imported values against the cleaned CSV source and resolved using the correct import locale.

This reinforces the importance of validating imported financial data before performing analysis.

---

# 🛠️ Tools & Technologies

- Python
- Pandas
- SQLite
- SQL
- Power BI
- DAX
- Git
- GitHub

---

# 🏢 Business Context

**Departments**

- Sales
- Marketing
- Operations
- R&D
- HR
- IT

**Categories**

- Salaries
- Marketing Spend
- Travel
- Software
- Equipment
- Other

**Reporting Period**

January – June 2026

---

# 📚 Lessons Learned

This project strengthened practical FP&A and analytics skills, including:

- Data validation before analysis
- Documenting data-cleaning decisions
- Building reusable SQL queries
- Designing a star schema
- Developing DAX measures
- Creating interactive executive dashboards
- Communicating financial insights through business-oriented reporting
