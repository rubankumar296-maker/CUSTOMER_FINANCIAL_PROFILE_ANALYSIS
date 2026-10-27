# Data Dictionary — Customer Financial Profile

## Dataset Overview

| Property | Description |
|---|---|
| Dataset name | Customer Financial Profile |
| Expected records | 1,000, subject to local verification |
| Expected columns | 9 |
| Primary identifier | Customer_ID |
| Data type categories | Numeric and categorical |
| Intended use | Descriptive customer financial analysis |

## Column Definitions

| Column | Expected data type | Description | Analytical use |
|---|---|---|---|
| Customer_ID | Text | Unique identifier assigned to a customer | Counting and identifying customer records |
| Age | Integer | Customer age in years | Age distribution and segmentation |
| Gender | Text | Gender category supplied in the dataset | Customer demographic analysis |
| Annual_Income | Numeric | Recorded annual income | Income summaries and comparisons |
| Credit_Score | Integer | Recorded customer credit score | Credit score distribution and comparison |
| Loan_Amount | Numeric | Recorded loan amount | Loan amount analysis |
| Savings_Balance | Numeric | Recorded savings balance | Savings analysis |
| Employment_Status | Text | Recorded employment category | Employment-group comparisons |
| Risk_Level | Text | Supplied customer risk classification | Descriptive risk distribution and comparison |

## Categorical Values

The initial inspection identified these categories:

- **Gender:** Female, Male
- **Employment_Status:** Employed, Self-Employed, Unemployed
- **Risk_Level:** Low, Medium, High

Confirm that these remain the actual categories in the CSV used for the final analysis.

## Data Quality Rules

1. Customer_ID should be populated and unique for each customer.
2. Age should contain valid numeric ages.
3. Annual_Income, Credit_Score, Loan_Amount, and Savings_Balance should be numeric.
4. Gender, Employment_Status, and Risk_Level should contain documented category values.
5. Missing values, duplicates, invalid values, and unexpected categories should be investigated and documented.
6. The original source dataset should remain unchanged.

## Limitations

The dataset does not, by itself, establish loan repayment history, actual loan defaults, or the methodology used to assign risk classifications. These fields should not be interpreted beyond their documented definitions.

The meaning and currency of financial amounts should be confirmed from the source dataset documentation before presenting them as a specific currency.