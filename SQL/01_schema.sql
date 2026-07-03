CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE expense_categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE budgets (
    budget_id INT PRIMARY KEY,
    departments_id INT NOT NULL REFERENCES departments(department_id),
    category_id INT NOT NULL REFERENCES expense_categories(category_id),
    month DATE NOT NULL,
    budget_amount NUMERIC(12, 2) NOT NULL,
    UNIQUE(departments_id, category_id, month)
);

CREATE TABLE actuals (
    actual_id INT PRIMARY KEY,
    departments_id INT NOT NULL REFERENCES departments(department_id),
    category_id INT NOT NULL REFERENCES expense_categories(category_id),
    month DATE NOT NULL,
    actual_amount NUMERIC(12, 2) NOT NULL,
    UNIQUE(departments_id, category_id, month)
);
