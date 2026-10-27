# Exploratory Data Analysis Findings

## 1. Objective

Exploratory Data Analysis (EDA) was performed to understand customer demographics, income, credit scores, loan amounts, savings balances, employment categories, and supplied risk classifications.

## 2. Dataset Used

- Source for analysis: data/processed/Customer_Financial_Profile_Cleaned.csv
- Notebook: notebooks/03_eda.ipynb
- Visualization directory: visualizations/

The dataset dimensions should be verified against the final processed CSV.

## 3. Customer Demographics

### Gender Distribution

The initial inspection reported 523 Female and 477 Male customers.

**Interpretation:** The two gender categories have similar representation in the inspected dataset.

### Age Distribution

The inspected ages ranged from 18 to 69, with an average age of approximately 43.62 years.

**Interpretation:** Age-group comparisons can help describe how customer records are distributed across different age ranges.

The final EDA chart should be used to identify the largest age group.

## 4. Income and Employment

The initial inspection reported the following average annual incomes:

| Employment status | Average annual income |
|---|---:|
| Self-Employed | 84,546.04 |
| Employed | 83,348.16 |
| Unemployed | 78,566.71 |

**Interpretation:** Self-Employed customers had the highest average annual income among the three categories in the initial inspection. Unemployed customers had the lowest average.

These differences are descriptive. They do not establish why the income differences exist.

## 5. Savings and Loan Amounts

The initial inspection reported:

- Average loan amount: approximately 24,185.56.
- Average savings balance: approximately 98,732.28.

The EDA charts compare the distribution of loan amounts and savings balances and explore their relationship.

**Interpretation:** The average values summarize the inspected customer records, but averages alone do not show how individual customer balances are distributed.

## 6. Credit Scores

The initial inspection reported an average credit score of approximately 576.08, with values ranging from 302 to 850.

**Interpretation:** The credit score distribution helps describe the range and concentration of recorded scores. Comparisons across supplied risk categories should be confirmed using the EDA outputs.

## 7. Supplied Risk Categories

The initial inspection reported the following counts:

| Risk level | Customers | Percentage |
|---|---:|---:|
| Low | 325 | 32.5% |
| Medium | 341 | 34.1% |
| High | 334 | 33.4% |

**Interpretation:** The three supplied risk categories have relatively similar customer counts in the inspected dataset.

The labels should not be interpreted as actual default probabilities unless their definitions and validation are established independently.

## 8. Relationships Explored

The EDA included:

- Annual income versus savings balance.
- Loan amount versus savings balance.
- Correlations between numeric variables.
- Risk distribution by employment status.
- Risk distribution by age group.
- Financial indicators by supplied risk category.

Describe the direction and strength of any relationships only after reviewing the actual charts and calculated statistics.

## 9. Business Relevance

The EDA provides a descriptive foundation for customer reporting and segmentation. It helps identify group differences and questions that may deserve additional analysis.

## 10. Limitations

- Observed associations do not prove causation.
- The supplied risk labels do not establish actual loan defaults.
- The dataset may not represent a wider customer population.
- Financial currency and source definitions should be confirmed before operational use.

## 11. Next Steps

1. Validate EDA metrics against SQL.
2. Build and review the Power BI dashboard.
3. Document verified findings and recommendations.
4. Preserve the raw source and document any future changes.