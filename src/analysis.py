
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "Customer_Financial_Profile_Cleaned.csv"
)

REPORTS_DIR = PROJECT_ROOT / "reports"
VISUALIZATIONS_DIR = PROJECT_ROOT / "visualizations"

REQUIRED_COLUMNS = [
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

NUMERIC_COLUMNS = [
    "Age",
    "Annual_Income",
    "Credit_Score",
    "Loan_Amount",
    "Savings_Balance",
]


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {INPUT_FILE}\n"
            "Run src/data_cleaning.py first."
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATIONS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if df.empty:
        raise ValueError("The cleaned dataset contains no rows.")

    print("Dataset shape:", df.shape)
    print("\nFirst five rows:")
    print(df.head())

    # 1. Overall customer and financial summary
    summary = pd.DataFrame({
        "Metric": [
            "Total customer records",
            "Unique customer IDs",
            "Average age",
            "Average annual income",
            "Average credit score",
            "Average loan amount",
            "Average savings balance",
        ],
        "Value": [
            len(df),
            df["Customer_ID"].nunique(),
            df["Age"].mean(),
            df["Annual_Income"].mean(),
            df["Credit_Score"].mean(),
            df["Loan_Amount"].mean(),
            df["Savings_Balance"].mean(),
        ],
    })

    summary.to_csv(REPORTS_DIR / "script_customer_summary.csv", index=False)
    print("\nOverall summary:")
    print(summary.to_string(index=False))

    # 2. Counts and percentages by category
    for column in ["Gender", "Employment_Status", "Risk_Level"]:
        counts = df[column].value_counts(dropna=False).rename_axis(
            column
        ).reset_index(name="Customer_Count")

        counts["Percentage"] = (
            counts["Customer_Count"] / len(df) * 100
        ).round(2)

        counts.to_csv(
            REPORTS_DIR / f"script_{column.lower()}_distribution.csv",
            index=False,
        )


    # 3. Financial metrics by employment category
    employment_summary = (
        df.groupby("Employment_Status", dropna=False)[NUMERIC_COLUMNS[1:]]
        .mean()
        .reset_index()
    )

    employment_summary.to_csv(
        REPORTS_DIR / "script_financials_by_employment.csv",
        index=False,
    )
            
    
    # 4. Financial metrics by supplied risk category
    risk_summary = (
        df.groupby("Risk_Level", dropna=False)[NUMERIC_COLUMNS[1:]]
        .mean()
        .reset_index()
    )

    risk_summary.to_csv(
    REPORTS_DIR / "script_financials_by_risk.csv",
    index=False,
)


    # 5. Risk counts by employment
    risk_by_employment = pd.crosstab(
        df["Employment_Status"],
        df["Risk_Level"],
    )

    risk_by_employment.to_csv(
        REPORTS_DIR / "script_risk_by_employment.csv"
    )

    # 6. Risk counts by age group
    age_bins = [17, 29, 39, 49, 59, 120]
    age_labels = ["18-29", "30-39", "40-49", "50-59", "60+"]

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=age_bins,
        labels=age_labels,
        include_lowest=True,
    )

    risk_by_age = pd.crosstab(
        df["Age_Group"],
        df["Risk_Level"],
        dropna=False,
    )

    risk_by_age.to_csv(REPORTS_DIR / "script_risk_by_age_group.csv")

    # 7. Additional visualizations with distinct filenames
    sns.set_theme(style="whitegrid")

    charts = [
        ("Annual_Income", "Annual Income Distribution",
         "script_annual_income_distribution.png"),
        ("Credit_Score", "Credit Score Distribution",
         "script_credit_score_distribution.png"),
        ("Loan_Amount", "Loan Amount Distribution",
         "script_loan_amount_distribution.png"),
        ("Savings_Balance", "Savings Balance Distribution",
         "script_savings_balance_distribution.png"),
    ]

    for column, title, filename in charts:
        fig, ax = plt.subplots(figsize=(9, 5))
        sns.histplot(data=df, x=column, kde=True, ax=ax)
        ax.set_title(title)
        fig.tight_layout()
        fig.savefig(VISUALIZATIONS_DIR / filename, dpi=150)
        plt.close(fig)

    # 8. Income versus savings
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.scatterplot(
        data=df,
        x="Annual_Income",
        y="Savings_Balance",
        hue="Risk_Level",
        ax=ax,
    )
    ax.set_title("Annual Income vs Savings Balance")
    fig.tight_layout()
    fig.savefig(
        VISUALIZATIONS_DIR / "script_income_vs_savings.png",
        dpi=150,
    )
    plt.close(fig)

    # 9. Correlation matrix
    correlation = df[NUMERIC_COLUMNS].corr()
    correlation.to_csv(REPORTS_DIR / "script_numeric_correlation.csv")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        ax=ax,
    )
    ax.set_title("Numeric Variable Correlation Matrix")
    fig.tight_layout()
    fig.savefig(
        VISUALIZATIONS_DIR / "script_correlation_matrix.png",
        dpi=150,
    )
    plt.close(fig)

    print("\nAnalysis completed.")
    print("Summary tables saved in:", REPORTS_DIR)
    print("Additional charts saved in:", VISUALIZATIONS_DIR)


if __name__ == "__main__":
    main()
