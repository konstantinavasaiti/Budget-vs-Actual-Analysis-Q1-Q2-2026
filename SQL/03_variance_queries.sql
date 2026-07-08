SELECT
    department_name,
    COUNT(*) AS months_tracked,
    SUM(CASE WHEN variance > 0 THEN 1 ELSE 0 END) AS months_over_budget,
    SUM(CASE WHEN variance < 0 THEN 1 ELSE 0 END) AS months_under_budget
FROM (
    SELECT
        d.department_name,
        b.month,
        SUM(a.actual_amount) - SUM(b.budget_amount) AS variance
    FROM budgets b
    JOIN actuals a
        ON b.department_id = a.department_id
        AND b.category_id = a.category_id
        AND b.month = a.month
    JOIN departments d ON d.department_id = b.department_id
    GROUP BY d.department_name, b.month
) monthly_variance
GROUP BY department_name
ORDER BY months_over_budget DESC;
