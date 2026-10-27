# SQL Analysis and Validation Report

## 1. Objective

The objective of SQL analysis was to examine customer demographics, financial indicators, employment categories, and supplied risk classifications using MySQL, then compare important results with the Python analysis.

## 2. SQL Scripts

| Script | Purpose |
|---|---|
| sql/01_schema.sql | Create the database and customers table |
| sql/02_basic_analysis.sql | Basic customer and financial summaries |
| sql/03_risk_analysis.sql | Risk counts and financial comparisons by risk |
| sql/04_advanced_analysis.sql | Advanced grouping, ranking, and comparisons |

## 3. Database Validation

Record the actual results of these checks:

| Check | Expected condition |
|---|---|
| Total records | Matches the processed CSV |
| Unique Customer_ID values | Matches the total customer count |
| Required columns | All nine expected columns are present |
| Duplicate customer IDs | None, if the source validation is unchanged |
| Unexpected missing values | Investigated and documented |

## 4. Cross-Tool Validation

Fill in the SQL and Python result columns after executing the corresponding queries and notebook cells.

| Metric | Python result | SQL result | Match? |
|---|---|---|---|
| Total customers | [Enter result] | [Enter result] | [Yes/No] |
| Unique customer IDs | [Enter result] | [Enter result] | [Yes/No] |
| Average annual income | [Enter result] | [Enter result] | [Yes/No] |
| Average credit score | [Enter result] | [Enter result] | [Yes/No] |
| Average loan amount | [Enter result] | [Enter result] | [Yes/No] |
| Average savings balance | [Enter result] | [Enter result] | [Yes/No] |
| Low risk customers | [Enter result] | [Enter result] | [Yes/No] |
| Medium risk customers | [Enter result] | [Enter result] | [Yes/No] |
| High risk customers | [Enter result] | [Enter result] | [Yes/No] |

## 5. Validation Procedure

1. Execute the SQL scripts in MySQL Workbench.
2. Record the result of each relevant query.
3. Obtain the corresponding metric from the Python analysis.
4. Compare results using the same source data and equivalent filters.
5. Check numeric precision and rounding before marking a result as different.
6. Investigate discrepancies before documenting a match.

## 6. Discrepancy Investigation

If results differ, check:

- Whether SQL and Python use the same CSV data.
- Whether the SQL table contains duplicate imports.
- Whether filters are active.
- Whether null values are handled consistently.
- Whether the same averaging or counting method was used.
- Whether rounding explains the difference.

Record the issue, cause, correction, and retest result if a discrepancy occurs.

## 7. Conclusion

SQL validation is complete when the relevant queries have executed successfully, results have been compared with Python, and discrepancies have been resolved or documented.

Do not mark unexecuted queries or unverified comparisons as successful. 