SELECT
    d.department_name,
    b.month,
    ROUND(SUM(b.budget_amount), 2) AS total_budget,
    ROUND(SUM(a.actual_amount), 2) AS total_actual,
    ROUND(SUM(a.actual_amount) - SUM(b.budget_amount), 2) AS variance
FROM budgets b
JOIN actuals a
    ON b.department_id = a.department_id
    AND b.category_id = a.category_id
    AND b.month = a.month
JOIN departments d ON d.department_id = b.department_id
GROUP BY d.department_name, b.month
ORDER BY d.department_name, b.month;
