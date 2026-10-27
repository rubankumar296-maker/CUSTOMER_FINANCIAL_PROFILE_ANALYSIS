USE customer_financial_profile;

-- Query 1: Customers with income above the overall average
SELECT
    Customer_ID,
    Employment_Status,
    Annual_Income,
    Savings_Balance,
    Risk_Level
FROM customers
WHERE Annual_Income > (
    SELECT AVG(Annual_Income)
    FROM customers
)
ORDER BY Annual_Income DESC;

-- Query 2: Employment categories ranked by average income
WITH employment_income AS (
    SELECT
        Employment_Status,
        COUNT(*) AS customer_count,
        AVG(Annual_Income) AS average_income
    FROM customers
    GROUP BY Employment_Status
)
SELECT
    Employment_Status,
    customer_count,
    ROUND(average_income, 2) AS average_income,
    DENSE_RANK() OVER (
        ORDER BY average_income DESC
    ) AS income_rank
FROM employment_income
ORDER BY income_rank;

-- Query 3: Top 10 customers by loan amount
SELECT
    Customer_ID,
    Annual_Income,
    Loan_Amount,
    Savings_Balance,
    Risk_Level
FROM customers
ORDER BY Loan_Amount DESC, Customer_ID
LIMIT 10;

-- Query 4: Average financial indicators by age group
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 29 THEN '18-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        WHEN Age >= 60 THEN '60+'
        ELSE 'Outside expected age groups'
    END AS age_group,
    COUNT(*) AS customer_count,
    ROUND(AVG(Annual_Income), 2) AS average_income,
    ROUND(AVG(Credit_Score), 2) AS average_credit_score,
    ROUND(AVG(Loan_Amount), 2) AS average_loan_amount,
    ROUND(AVG(Savings_Balance), 2) AS average_savings
FROM customers
GROUP BY age_group
ORDER BY age_group;

-- Query 5: Customers with loan amounts above their
-- employment category's average
SELECT
    c.Customer_ID,
    c.Employment_Status,
    c.Loan_Amount,
    ROUND(e.average_loan, 2) AS employment_average_loan
FROM customers AS c
JOIN (
    SELECT
        Employment_Status,
        AVG(Loan_Amount) AS average_loan
    FROM customers
    GROUP BY Employment_Status
) AS e
    ON c.Employment_Status = e.Employment_Status
WHERE c.Loan_Amount > e.average_loan
ORDER BY c.Loan_Amount DESC;
