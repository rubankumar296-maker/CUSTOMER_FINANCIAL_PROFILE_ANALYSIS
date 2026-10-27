USE customer_financial_profile;

-- Query 1: Count customers by recorded risk level
SELECT
    Risk_Level,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2)
        AS percentage
FROM customers
GROUP BY Risk_Level
ORDER BY
    CASE Risk_Level
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3
        ELSE 4
    END;

-- Query 2: Average financial indicators by risk level
SELECT
    Risk_Level,
    COUNT(*) AS customer_count,
    ROUND(AVG(Annual_Income), 2) AS average_income,
    ROUND(AVG(Credit_Score), 2) AS average_credit_score,
    ROUND(AVG(Loan_Amount), 2) AS average_loan_amount,
    ROUND(AVG(Savings_Balance), 2) AS average_savings
FROM customers
GROUP BY Risk_Level
ORDER BY average_credit_score DESC;

-- Query 3: Risk distribution by employment status
SELECT
    Employment_Status,
    Risk_Level,
    COUNT(*) AS customer_count
FROM customers
GROUP BY Employment_Status, Risk_Level
ORDER BY Employment_Status, Risk_Level;

-- Query 4: Risk distribution by age group
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 29 THEN '18-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        WHEN Age >= 60 THEN '60+'
        ELSE 'Outside expected age groups'
    END AS age_group,
    Risk_Level,
    COUNT(*) AS customer_count
FROM customers
GROUP BY age_group, Risk_Level
ORDER BY age_group, Risk_Level;

-- Query 5: Loan and savings comparison by risk level
SELECT
    Risk_Level,
    ROUND(AVG(Loan_Amount), 2) AS average_loan_amount,
    ROUND(AVG(Savings_Balance), 2) AS average_savings,
    ROUND(AVG(Loan_Amount - Savings_Balance), 2)
        AS average_loan_minus_savings
FROM customers
GROUP BY Risk_Level
ORDER BY Risk_Level;
