# Data Cleaning and Validation Report

## 1. Objective

The objective of this phase was to validate the Customer Financial Profile dataset and prepare a reliable processed file for exploratory data analysis, SQL analysis, and Power BI.

## 2. Source and Output

| Item | Location |
|---|---|
| Original source | data/raw/Customer_Financial_Profile_Dataset.csv |
| Cleaned output | data/processed/Customer_Financial_Profile_Cleaned.csv |
| Cleaning notebook | notebooks/02_data_cleaning.ipynb |

The original source file should remain unchanged.

## 3. Validation Activities

The cleaning notebook was designed to check:

1. Expected column names and structure.
2. Column data types.
3. Missing values.
4. Exact duplicate rows.
5. Duplicate Customer_ID values.
6. Unexpected whitespace in text fields.
7. Customer ID format.
8. Numeric values and possible invalid ranges.
9. Expected categories in Gender, Employment_Status, and Risk_Level.
10. Successful saving and reloading of the processed CSV.

## 4. Initial Data Quality Findings

The initial dataset inspection reported no missing values, exact duplicate rows, duplicate customer IDs, negative numeric values, or leading/trailing whitespace in the inspected text fields.

These initial results were used to guide validation. Records should not be deleted merely to reduce the row count or make every check appear clean.

## 5. Cleaning Decisions

Only justified transformations should be documented here.

| Check | Required documentation |
|---|---|
| Missing values | Record actual count and any handling performed |
| Duplicate rows | Record actual count and any removal performed |
| Duplicate customer IDs | Record actual count and investigation |
| Text standardization | Record columns changed, if any |
| Data type correction | Record columns changed, if any |
| Invalid values | Record the issue and the justification for any correction |
| Category validation | Record unexpected values and their resolution |

If a check found no issue, document that no correction was required. Do not claim that data was changed when no transformation was needed.

## 6. Output Validation

The processed CSV should be reloaded and checked for:

- Expected column names.
- Expected data types.
- Correct row count.
- Unique customer IDs.
- Missing values.
- Successful file loading.

The final row count and quality-check results should match the actual output of notebooks/02_data_cleaning.ipynb.

## 7. Output File

Processed dataset:

data/processed/Customer_Financial_Profile_Cleaned.csv

## 8. Conclusion

The cleaning phase is complete when the validation checks pass, the processed CSV has been saved and reloaded successfully, and the final results are documented. The objective is data reliability, not unnecessary row removal.

## 9. Limitations

Data cleaning cannot establish the meaning or correctness of undocumented risk classifications. Any assumptions about the source data should be documented and verified.