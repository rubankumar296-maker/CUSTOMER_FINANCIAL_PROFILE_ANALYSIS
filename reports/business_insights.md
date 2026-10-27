# Business Insights and Recommendations
## Customer Financial Profile Analysis

## 1. Executive Summary

This project analyzes customer demographic and financial information using Python, SQL, and Power BI. The objective is to summarize customer characteristics, compare financial indicators, and explore patterns across the risk categories supplied in the dataset.

The findings in this report should be based on verified outputs from the processed CSV, Python analysis, SQL queries, and Power BI dashboard.

## 2. Key Findings

### Finding 1 — Customer Composition

**Evidence:** The initial inspection reported 1,000 customer records, including 523 Female and 477 Male customers.

**Interpretation:** The two gender categories have similar representation in the inspected dataset.

**Business relevance:** Understanding customer composition provides context for comparing financial indicators across groups.

### Finding 2 — Employment and Income

**Evidence:** The initial inspection reported average annual income of 84,546.04 for Self-Employed customers, 83,348.16 for Employed customers, and 78,566.71 for Unemployed customers.

**Interpretation:** Self-Employed customers had the highest average annual income among these categories in the initial inspection.

**Business relevance:** The differences provide a basis for further investigation of income patterns across employment groups. They do not establish the cause of those differences.

### Finding 3 — Risk Distribution

**Evidence:** The initial inspection reported 325 Low risk, 341 Medium risk, and 334 High risk customers.

**Interpretation:** The three supplied categories have relatively similar counts in the inspected dataset.

**Business relevance:** This provides a descriptive summary of how the supplied classifications are distributed.

### Finding 4 — Credit Scores and Financial Indicators

**Evidence:** The initial inspection reported average credit score of 576.08, average loan amount of 24,185.56, and average savings balance of 98,732.28.

**Interpretation:** These figures summarize the recorded customer financial indicators. Group-level differences should be documented using the final Power BI and SQL results.

**Business relevance:** Reviewing these indicators together can help describe customer financial profiles and identify questions for additional analysis.

## 3. Business Recommendations

### Recommendation 1 — Standardize Reporting

Maintain consistent definitions for customer counts, income, savings, loan amounts, credit scores, and risk categories across reports.

### Recommendation 2 — Investigate Group Differences

Use the dashboard to explore differences in financial indicators across employment categories and age groups. Validate meaningful patterns before making operational decisions.

### Recommendation 3 — Review Risk Definitions

Document how the supplied Low, Medium, and High risk labels were assigned. Do not treat them as verified default probabilities without supporting evidence.

### Recommendation 4 — Maintain Data Quality

Preserve the original source, document cleaning decisions, and repeat validation when the dataset changes.

### Recommendation 5 — Strengthen Analytical Validation

Compare Python, SQL, and Power BI results before publishing figures. Investigate discrepancies and record how they were resolved.

## 4. Limitations

- The dataset contains a limited set of customer attributes.
- Actual loan repayment history and default outcomes have not been established by this project.
- Observed relationships do not prove causation.
- The dataset's representativeness of a wider customer population has not been established.
- Financial currency and risk-label definitions should be confirmed from reliable source documentation.

## 5. Conclusion

The project combines data validation, exploratory analysis, SQL queries, and an interactive Power BI dashboard to describe the customer population and its recorded financial characteristics. The findings support descriptive reporting and further investigation, subject to the limitations of the source data.