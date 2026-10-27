
-- Customer Financial Profile Analysis
-- Database and table setup

CREATE DATABASE IF NOT EXISTS customer_financial_profile;

USE customer_financial_profile;

CREATE TABLE IF NOT EXISTS customers (
    Customer_ID VARCHAR(20) PRIMARY KEY,
    Age INT NOT NULL,
    Gender VARCHAR(30) NOT NULL,
    Annual_Income DECIMAL(12,2) NOT NULL,
    Credit_Score INT NOT NULL,
    Loan_Amount DECIMAL(12,2) NOT NULL,
    Savings_Balance DECIMAL(12,2) NOT NULL,
    Employment_Status VARCHAR(50) NOT NULL,
    Risk_Level VARCHAR(30) NOT NULL
);


-- Verify the database and table
SELECT DATABASE();

DESCRIBE customers;

USE customer_financial_profile;

SELECT COUNT(*) AS total_customers
FROM customers;

SELECT *
FROM customers
LIMIT 10;

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT Customer_ID) AS unique_customers,
    COUNT(*) - COUNT(DISTINCT Customer_ID) AS duplicate_ids
FROM customers;

SELECT
    SUM(Customer_ID IS NULL) AS missing_customer_id,
    SUM(Age IS NULL) AS missing_age,
    SUM(Annual_Income IS NULL) AS missing_income,
    SUM(Credit_Score IS NULL) AS missing_credit_score,
    SUM(Loan_Amount IS NULL) AS missing_loan,
    SUM(Savings_Balance IS NULL) AS missing_savings
FROM customers;
