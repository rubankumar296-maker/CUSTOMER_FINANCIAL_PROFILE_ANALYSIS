USE customer_financial_profile;

-- Query 1: Total and unique customers
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT Customer_ID) AS unique_customers
FROM customers;

-- Query 2: Average customer age
SELECT
    ROUND(AVG(Age), 2) AS average_age,
    MIN(Age) AS minimum_age,
    MAX(Age) AS maximum_age
FROM customers;

-- Query 3: Customer distribution by gender
SELECT
    Gender,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2)
        AS percentage
FROM customers
GROUP BY Gender
ORDER BY customer_count DESC;

-- Query 4: Customer distribution by employment status
SELECT
    Employment_Status,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2)
        AS percentage
FROM customers
GROUP BY Employment_Status
ORDER BY customer_count DESC;

-- Query 5: Financial summary statistics
SELECT
    ROUND(AVG(Annual_Income), 2) AS average_annual_income,
    ROUND(AVG(Credit_Score), 2) AS average_credit_score,
    ROUND(AVG(Loan_Amount), 2) AS average_loan_amount,
    ROUND(AVG(Savings_Balance), 2) AS average_savings_balance
FROM customers;

-- Query 6: Median income (MySQL 8.0.2+)
WITH ranked_income AS (
    SELECT
        Annual_Income,
        ROW_NUMBER() OVER (ORDER BY Annual_Income) AS row_num,
        COUNT(*) OVER () AS total_rows
    FROM customers
)
SELECT
    AVG(Annual_Income) AS median_annual_income
FROM ranked_income
WHERE row_num IN (
    FLOOR((total_rows + 1) / 2),
    FLOOR((total_rows + 2) / 2)
);

-- Query 7: Average income by employment status
SELECT
    Employment_Status,
    COUNT(*) AS customer_count,
    ROUND(AVG(Annual_Income), 2) AS average_income,
    ROUND(AVG(Savings_Balance), 2) AS average_savings
FROM customers
GROUP BY Employment_Status
ORDER BY average_income DESC;
