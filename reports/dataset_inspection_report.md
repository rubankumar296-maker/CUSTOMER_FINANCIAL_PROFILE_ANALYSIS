# Dataset Inspection Report

## 1. Purpose

The purpose of this inspection was to understand the structure, data types, distributions, and initial data quality of the Customer Financial Profile dataset before performing cleaning and analysis.

## 2. Dataset Overview

| Property | Initial inspection result |
|---|---|
| Dataset | Customer Financial Profile |
| Rows | 1,000 |
| Columns | 9 |
| Identifier | Customer_ID |
| Missing values | 0 reported |
| Exact duplicate rows | 0 reported |
| Duplicate customer IDs | 0 reported |

These figures are from the initial inspection and should be checked against the original CSV used in the project.

## 3. Column Structure

The dataset contains the following fields:

- Customer_ID
- Age
- Gender
- Annual_Income
- Credit_Score
- Loan_Amount
- Savings_Balance
- Employment_Status
- Risk_Level

The dataset combines customer demographics, financial measurements, employment categories, and supplied risk classifications.

## 4. Initial Numeric Ranges

| Column | Minimum | Maximum |
|---|---:|---:|
| Age | 18 | 69 |
| Annual_Income | 15,012 | 149,971 |
| Credit_Score | 302 | 850 |
| Loan_Amount | 198 | 49,839 |
| Savings_Balance | 153 | 199,822 |

These ranges describe the inspected data. They do not independently establish whether every value is appropriate for a real-world financial institution.

## 5. Initial Category Distribution

### Gender

| Category | Customers |
|---|---:|
| Female | 523 |
| Male | 477 |

### Employment Status

| Category | Customers |
|---|---:|
| Employed | 334 |
| Self-Employed | 330 |
| Unemployed | 336 |

### Risk Level

| Category | Customers |
|---|---:|
| Low | 325 |
| Medium | 341 |
| High | 334 |

## 6. Initial Descriptive Statistics

| Metric | Mean | Median |
|---|---:|---:|
| Age | 43.617 | 43 |
| Annual Income | 82,136.893 | 82,367.5 |
| Credit Score | 576.083 | 569 |
| Loan Amount | 24,185.562 | 23,943.5 |
| Savings Balance | 98,732.278 | 100,097 |

## 7. Initial Data Quality Checks

The initial inspection reported:

- No missing values.
- No exact duplicate rows.
- No duplicate customer identifiers.
- No duplicate column names.
- No negative values in the inspected numeric fields.
- No leading or trailing whitespace in the inspected text values.

These checks should be rerun if the source file changes.

## 8. Business Relevance

The initial inspection established that the dataset contains the fields needed for descriptive analysis of customer demographics, income, credit scores, loan amounts, savings, employment, and supplied risk categories.

## 9. Next Steps

1. Validate the original dataset.
2. Perform justified cleaning and transformation.
3. Save the processed dataset separately from the raw source.
4. Perform exploratory data analysis.
5. Compare findings using SQL and Power BI.

## 10. Limitations

This report documents the initial dataset inspection. It does not establish that the risk labels predict actual defaults or that the dataset represents a wider customer population.