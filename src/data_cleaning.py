
from pathlib import Path
import pandas as pd

# Project folders
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "Customer_Financial_Profile_Dataset.csv"
OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "Customer_Financial_Profile_Cleaned.csv"
)

EXPECTED_COLUMNS = [
    "Customer_ID",
    "Age",
    "Gender",
    "Annual_Income",
    "Credit_Score",
    "Loan_Amount",
    "Savings_Balance",
    "Employment_Status",
    "Risk_Level",
]

TEXT_COLUMNS = [
    "Customer_ID",
    "Gender",
    "Employment_Status",
    "Risk_Level",
]

NUMERIC_COLUMNS = [
    "Age",
    "Annual_Income",
    "Credit_Score",
    "Loan_Amount",
    "Savings_Balance",
]


def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw CSV not found: {RAW_FILE}\n"
            "Check the filename in data/raw and update RAW_FILE if needed."
        )

    # Read the source file; never overwrite it.
    source_df = pd.read_csv(RAW_FILE)
    df = source_df.copy(deep=True)

    print("Original dataset shape:", df.shape)

    # Validate the expected schema before changing data.
    missing_columns = set(EXPECTED_COLUMNS) - set(df.columns)
    unexpected_columns = set(df.columns) - set(EXPECTED_COLUMNS)

    if missing_columns:
        raise ValueError(f"Missing expected columns: {sorted(missing_columns)}")

    if unexpected_columns:
        print("Unexpected columns found:", sorted(unexpected_columns))
        print("Review these columns before deciding whether to retain them.")

    if df.columns.duplicated().any():
        raise ValueError("Duplicate column names detected. Investigate before cleaning.")

    # Standardize whitespace in text columns.
    for column in TEXT_COLUMNS:
        df[column] = df[column].astype("string").str.strip()

    # Convert numeric columns carefully; invalid text becomes an error.
    for column in NUMERIC_COLUMNS:
        converted = pd.to_numeric(df[column], errors="coerce")
        invalid_mask = converted.isna() & df[column].notna()

        if invalid_mask.any():
            examples = df.loc[invalid_mask, column].head(5).tolist()
            raise ValueError(
                f"Non-numeric values found in {column}: {examples}"
            )

        df[column] = converted

    # Report quality checks instead of silently deleting records.
    print("\nMissing values by column:")
    print(df.isna().sum())

    print("\nExact duplicate rows:", int(df.duplicated().sum()))
    print(
        "Duplicate Customer_ID values:",
        int(df["Customer_ID"].duplicated().sum()),
    )

    if df["Customer_ID"].isna().any() or (df["Customer_ID"] == "").any():
        raise ValueError("Missing or blank Customer_ID values detected.")

    if df["Customer_ID"].duplicated().any():
        raise ValueError(
            "Duplicate Customer_ID values detected. Investigate them before proceeding."
        )

    if df.isna().any().any():
        raise ValueError(
            "Missing values detected. Review them and choose a justified handling method."
        )

    if df["Customer_ID"].str.fullmatch(r"CUST\d{5}").eq(False).any():
        raise ValueError("Some Customer_ID values do not match CUST followed by 5 digits.")

    # Validate expected categories without silently changing their meaning.
    expected_categories = {
        "Gender": {"Female", "Male"},
        "Employment_Status": {"Employed", "Self-Employed", "Unemployed"},
        "Risk_Level": {"Low", "Medium", "High"},
    }

    for column, allowed_values in expected_categories.items():
        observed = set(df[column].dropna().unique())
        unexpected = observed - allowed_values

        if unexpected:
            raise ValueError(
                f"Unexpected values in {column}: {sorted(unexpected)}"
            )

    # Check reasonable data bounds based on the inspected dataset.
    # Investigate any violations instead of deleting those rows.
    bounds = {
        "Age": (18, 120),
        "Annual_Income": (0, None),
        "Credit_Score": (0, None),
        "Loan_Amount": (0, None),
        "Savings_Balance": (0, None),
    }

    for column, (lower, upper) in bounds.items():
        invalid = df[column].lt(lower)

        if upper is not None:
            invalid |= df[column].gt(upper)

        if invalid.any():
            raise ValueError(
                f"Values outside the configured validation bounds in {column}: "
                f"{int(invalid.sum())} record(s). Investigate before proceeding."
            )

    # Preserve the original number of records unless a documented decision
    # explicitly justifies a change.
    if len(df) != len(source_df):
        raise RuntimeError("Unexpected row-count change detected.")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    # Reload the saved file and validate the output.
    saved_df = pd.read_csv(OUTPUT_FILE)

    if saved_df.shape != df.shape:
        raise RuntimeError("Saved dataset dimensions do not match the cleaned dataset.")

    if saved_df.columns.tolist() != df.columns.tolist():
        raise RuntimeError("Saved dataset columns do not match the cleaned dataset.")

    print("\nCleaning and validation completed.")
    print("Final dataset shape:", saved_df.shape)
    print("Saved file:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
