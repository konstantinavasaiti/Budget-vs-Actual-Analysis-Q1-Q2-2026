SELECT
    department_name,
    category_name,
    ROUND(total_budget, 2) AS total_budget,
    ROUND(total_actual, 2) AS total_actual,
    ROUND(variance, 2) AS variance,
    ROUND(100.0 * variance / NULLIF(total_budget, 0), 2) AS variance_pct
FROM (
    SELECT
        d.department_name,
        c.category_name,
        SUM(b.budget_amount) AS total_budget,
        SUM(a.actual_amount) AS total_actual,
        SUM(a.actual_amount) - SUM(b.budget_amount) AS variance
    FROM budgets b
    JOIN actuals a
        ON b.department_id = a.department_id
        AND b.category_id = a.category_id
        AND b.month = a.month
    JOIN departments d ON d.department_id = b.department_id
    JOIN expense_categories c ON c.category_id = b.category_id
    GROUP BY d.department_name, c.category_name
) dept_totals
ORDER BY variance_pct DESC;
