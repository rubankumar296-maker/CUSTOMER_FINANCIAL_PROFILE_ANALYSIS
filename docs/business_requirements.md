# Customer Financial Profile Analysis

## 1. Business Problem

Financial services companies need to understand their customers' financial profiles to evaluate portfolio composition, understand customer financial behavior, and monitor recorded risk categories.

The available dataset contains customer demographic information, annual income, credit scores, loan amounts, savings balances, employment status, and risk levels.

The business needs a structured analysis of these attributes to understand customer distributions, identify financial patterns, compare customer segments, and communicate findings through an interactive dashboard.

## 2. Project Purpose

The purpose of this project is to transform customer financial data into meaningful business insights using Python, MySQL, and Power BI.

## 3. Primary Business Objective

Analyze customer financial profiles and identify patterns in income, savings, credit scores, loan amounts, employment status, and recorded risk levels.

## 4. Specific Objectives

1. Understand the demographic composition of the customer portfolio.
2. Analyze annual income and savings balance distributions.
3. Examine credit score patterns across customer segments.
4. Compare loan amounts across employment and risk categories.
5. Understand the distribution of recorded financial risk levels.
6. Compare financial indicators across age groups and employment categories.
7. Build an interactive Power BI dashboard.
8. Present evidence-based findings and recommendations.

## 5. Business Questions

### Customer Overview
1. How many unique customers are in the dataset?
2. What is the average age of customers?
3. What is the distribution of customers by gender?
4. How are customers distributed across employment categories?

### Income and Savings
5. What are the average, median, minimum, and maximum annual incomes?
6. Which employment categories have the highest average income?
7. What is the average savings balance across customers?
8. How do savings balances vary across age groups?

### Credit and Loans
9. What is the average credit score?
10. How do credit scores vary across recorded risk levels?
11. What is the average loan amount?
12. How do loan amounts vary by employment status?
13. How do loan amounts compare with savings balances across customer segments?

### Risk Analysis
14. How many customers belong to each recorded risk category?
15. What percentage of customers belongs to each risk category?
16. How do average income, savings, credit score, and loan amount vary across risk categories?
17. How does the distribution of recorded risk levels vary by age group and employment status?

## 6. Project Scope

### Included
- Dataset inspection and data quality validation
- Data cleaning and preparation
- Exploratory data analysis using Python
- Business analysis using MySQL
- Power BI data modeling and DAX measures
- Interactive dashboard development
- Business insights and recommendations
- Project documentation and GitHub publication

### Excluded
- Predicting future loan defaults
- Approving or rejecting loan applications
- Assigning new risk scores to individual customers
- Making causal claims about financial behavior
- Providing individual financial advice

## 7. Tools and Technologies

- Python: Pandas, NumPy, Matplotlib, Seaborn
- MySQL: Data storage and business queries
- Power BI: Data modeling, DAX and dashboards
- Jupyter Notebook: Analysis documentation
- Git and GitHub: Version control and portfolio publishing

## 8. Expected Deliverables

1. Original and cleaned datasets
2. Python analysis notebooks
3. SQL scripts
4. Power BI dashboard
5. Exported visualizations
6. Business insights report
7. Data dictionary
8. Project README and GitHub repository

## 9. Success Criteria

- Dataset columns and data types are documented.
- Data quality issues are investigated and handled appropriately.
- Analytical results are reproducible.
- Python and SQL results agree for equivalent calculations.
- Dashboard KPIs and charts are validated against the underlying data.
- Business conclusions are supported by actual results.
- Project files and instructions are organized for review.

## 10. Assumptions and Limitations

The analysis assumes that the supplied dataset is suitable for descriptive analysis after validation. The meaning and definitions of the recorded risk categories must be confirmed where documentation is available.

Observed relationships do not establish causation. A customer's recorded risk category is not proof of a future default, and the findings should not be treated as a validated credit decision model.

## 11. Final Outcome

Deliver a documented customer financial profile analysis project that demonstrates data cleaning, exploratory analysis, SQL business analysis, dashboard development, and business communication.

## 12. Stakeholders and Their Needs

| Stakeholder | Information Needed |
|---|---|
| Business Manager | Overall customer portfolio and financial patterns |
| Risk Analyst | Distribution of recorded risk categories and associated financial indicators |
| Finance Team | Income, savings, and loan portfolio summaries |
| Data Analyst | Data quality, customer segments, and reproducible calculations |
| Management | Concise KPIs, trends, comparisons, and evidence-based findings |

### Intended Use

The analysis is intended for descriptive reporting, portfolio understanding, and exploratory business analysis. It is not intended to automate credit decisions.

## 14. Dashboard Requirements

### Page 1: Customer Overview
Display customer totals, financial KPIs, customer demographics, employment distribution, and age-group summaries.

### Page 2: Financial Analysis
Display income, savings, credit score, and loan amount comparisons across relevant customer segments.

### Page 3: Risk Analysis
Display the distribution of recorded risk categories and comparisons of available financial indicators across those categories.

### Interactivity
Include appropriate slicers for employment status, gender, age group, and recorded risk level, subject to data quality and business relevance.

### Validation
Verify dashboard measures against equivalent calculations from the cleaned dataset and SQL analysis.