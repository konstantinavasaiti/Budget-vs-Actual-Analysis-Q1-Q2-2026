# 📊 Budget vs Actual Analysis (H1 2026)

An end-to-end FP&A analytics project simulating a real-world **Budget vs Actual** analysis for a mid-size retail/manufacturing company.

The project demonstrates the complete analytics workflow—from synthetic data generation and validation to SQL modeling, Python analysis, interactive Power BI reporting, and an executive PowerPoint presentation.

> ⚠️ **Note:** All data used in this project is synthetic and was generated to follow realistic business patterns. No real company data is included.

---

# 📸 Dashboard Preview

## Overview Dashboard

![Overview Dashboard](screenshots/overview.png)

---

# 🚧 Project Status

- ✅ Data generation
- ✅ SQL database & variance queries
- ✅ Data cleaning & validation
- ✅ Python variance analysis
- ✅ Power BI interactive dashboard
- ✅ Executive PowerPoint presentation

---

# 📁 Project Structure

```text
data/
├── raw/
│   ├── budget_2026.csv
│   ├── actuals_2026_H1_raw.csv
│   └── actuals_2026.csv
│
├── processed/
│   ├── actuals_2026_H1_clean.csv
│   └── budget_actual.db
│
SQL/
├── 01_schema.sql
├── 02_seed_data.sql
└── 03_variance_queries.sql
│
Python/
├── clean_data.py
├── load_data.py
└── run_queries.py
│
Power BI/
└── Budget_Analysis_Dashboard.pbix
│
PowerPoint/
└── Budget_vs_Actual_Executive_Presentation.pptx
│
screenshots/
├── overview.png
├── trend.png
├── threshold.png
└── presentation_cover.png
│
README.md
```

---

# 📊 Power BI Dashboard

The interactive dashboard was developed using a **star schema** model and includes:

- Executive KPI cards
- Monthly trend analysis
- Department & category analysis
- Threshold alerts (±5% variance)
- Interactive filtering
- Custom tooltips

## Trend Analysis

![Trend Analysis](screenshots/trend.png)

## Threshold Alerts

![Threshold Alerts](screenshots/threshold.png)

---

# 📽️ Executive Presentation

The project includes an executive PowerPoint presentation designed for senior management.

Presentation contents:

- Business Objective
- Executive Summary
- Trend Analysis
- Threshold Alerts
- Business Recommendations
- Lessons Learned

## Presentation Preview

![Executive Presentation](screenshots/presentation_cover.png)

---

# 🏗️ Data Model

The Power BI report follows a **star schema** consisting of:

### Fact Tables

- Fact Budget
- Fact Actuals

### Dimension Tables

- Department
- Category
- Date

Relationships are configured as **many-to-one** to support efficient filtering and reporting.

---

# 🔎 Key Findings

The analysis identified several significant Budget vs Actual variances during H1 2026.

Highlights include:

- Marketing consistently exceeded budget due to campaign spending.
- IT remained below budget because of delayed software and equipment investments.
- Multiple department-category combinations exceeded the predefined ±5% management threshold.
- Overall company spending remained close to the planned budget despite isolated exceptions.

---

# 🧹 Data Cleaning & Validation

The raw ERP export intentionally included realistic data-quality issues to simulate a production environment.

Cleaning activities included:

- Standardizing inconsistent department names
- Removing duplicate records
- Removing incomplete transactions
- Converting currency-formatted text into numeric values

Final result:

**193 raw records → 188 validated records**

used throughout SQL, Python, Power BI, and the executive presentation.

---

# ✅ Data Validation

To ensure data integrity, validation was performed before analysis.

Verification included:

- Raw row-count verification
- Duplicate detection
- Missing-value validation
- SQLite row-count confirmation
- Cross-checking imported Power BI values against the cleaned dataset

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
- Microsoft PowerPoint

---

# 🏢 Business Context

### Departments

- Sales
- Marketing
- Operations
- R&D
- HR
- IT

### Categories

- Salaries
- Marketing Spend
- Travel
- Software
- Equipment
- Other

### Reporting Period

**January – June 2026**

---

# 📚 Lessons Learned

This project strengthened practical FP&A and Business Intelligence skills, including:

- Building an end-to-end financial analytics workflow
- Validating financial datasets before reporting
- Designing a star schema for analytical reporting
- Writing reusable SQL queries
- Developing DAX measures
- Creating interactive Power BI dashboards
- Translating analytical findings into business recommendations
- Presenting results in an executive-friendly format

---

# 🎯 Project Outcome

This portfolio project demonstrates the complete FP&A reporting lifecycle:

**Raw Data → Data Cleaning → SQL → Python → Power BI → Executive Presentation**

It showcases both technical implementation and business communication skills commonly required in Financial Planning & Analysis (FP&A) and Business Intelligence roles.
