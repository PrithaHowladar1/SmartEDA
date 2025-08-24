import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Page config
st.set_page_config(page_title="📊 EDA Profiler", layout="wide")

st.title("📊 SmartEDA - Exploratory Data Analysis with YData Profiling")

# Sidebar controls
st.sidebar.header("🔧 Controls")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

section = st.sidebar.radio("📊 Choose Section", [
    "Data Preview",
    "Data Quality Warnings",
    "Correlation Matrix",
    "Column Summary",
    "Missing Value Imputation",
    "Outlier Detection",
    "Profiling Report"
])

selected_corr_method = st.sidebar.selectbox("Correlation Method", ["pearson", "spearman", "kendall"])
show_heatmap = st.sidebar.checkbox("Show Heatmap", value=True)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    numeric_df = df.select_dtypes(include=["number"])
    non_numeric_cols = df.select_dtypes(exclude=["number"]).columns

    if section == "Data Preview":
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

    elif section == "Data Quality Warnings":
        st.subheader("🧪 Data Quality Warnings")
        warnings = []

        missing = df.isnull().sum()
        missing_cols = missing[missing > 0]
        if not missing_cols.empty:
            warnings.append(f"⚠️ Missing values in {len(missing_cols)} column(s): {', '.join(missing_cols.index)}")

        duplicate_count = df.duplicated().sum()
        if duplicate_count > 0:
            warnings.append(f"⚠️ {duplicate_count} duplicate row(s) found.")

        constant_cols = [col for col in df.columns if df[col].nunique() == 1]
        if constant_cols:
            warnings.append(f"⚠️ {len(constant_cols)} column(s) with constant values: {', '.join(constant_cols)}")

        high_card_cols = [col for col in non_numeric_cols if df[col].nunique() > 50]
        if high_card_cols:
            warnings.append(f"⚠️ High cardinality in {len(high_card_cols)} column(s): {', '.join(high_card_cols)}")

        if warnings:
            for w in warnings:
                st.warning(w)
        else:
            st.success("✅ No major data quality issues detected.")

    elif section == "Correlation Matrix":
        st.subheader("📈 Correlation Matrix")
        with st.spinner("Computing correlation matrix..."):
            if numeric_df.shape[1] < 2:
                st.warning("Not enough numeric columns to compute correlation.")
            else:
                corr_matrix = numeric_df.corr(method=selected_corr_method)
                st.dataframe(corr_matrix.style.background_gradient(cmap="coolwarm"))

                if show_heatmap:
                    st.subheader("🔍 Correlation Heatmap")
                    fig, ax = plt.subplots()
                    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
                    st.pyplot(fig)

    elif section == "Column Summary":
        st.subheader("📊 Column Summary Panel")
        selected_column = st.selectbox("Select a numeric column", numeric_df.columns)
        col_data = numeric_df[selected_column]
        st.write(f"**Summary for `{selected_column}`**")
        st.write({
            "Mean": col_data.mean(),
            "Median": col_data.median(),
            "Mode": col_data.mode().iloc[0] if not col_data.mode().empty else None,
            "Std Dev": col_data.std(),
            "Skewness": col_data.skew(),
            "Min": col_data.min(),
            "Max": col_data.max(),
            "Missing Values": col_data.isnull().sum()
        })

    elif section == "Missing Value Imputation":
        st.subheader("🧼 Missing Value Imputation")
        selected_column = st.selectbox("Select column to impute", numeric_df.columns)
        col_data = numeric_df[selected_column]
        impute_method = st.radio("Choose imputation method", ["None", "Mean", "Median", "Mode", "Custom Value"])
        if impute_method != "None":
            if col_data.isnull().sum() == 0:
                st.info("✅ No missing values to impute.")
            else:
                if impute_method == "Mean":
                    df[selected_column].fillna(col_data.mean(), inplace=True)
                elif impute_method == "Median":
                    df[selected_column].fillna(col_data.median(), inplace=True)
                elif impute_method == "Mode":
                    df[selected_column].fillna(col_data.mode().iloc[0], inplace=True)
                elif impute_method == "Custom Value":
                    custom_val = st.number_input("Enter custom value", value=0.0)
                    df[selected_column].fillna(custom_val, inplace=True)
                st.success(f"✅ Missing values in `{selected_column}` filled using {impute_method}.")

    elif section == "Outlier Detection":
        st.subheader("🚨 Outlier Detection")
        selected_column = st.selectbox("Select column for outlier detection", numeric_df.columns)
        col_data = numeric_df[selected_column]
        outlier_method = st.selectbox("Choose method", ["Z-score", "IQR"])

        if outlier_method == "Z-score":
            clean_data = col_data.dropna()
            z_scores = zscore(clean_data)
            outliers = clean_data[(abs(z_scores) > 3)]
        elif outlier_method == "IQR":
            Q1 = col_data.quantile(0.25)
            Q3 = col_data.quantile(0.75)
            IQR = Q3 - Q1
            outliers = col_data[(col_data < Q1 - 1.5 * IQR) | (col_data > Q3 + 1.5 * IQR)]

        st.write(f"Found {len(outliers)} outliers in `{selected_column}` using {outlier_method}.")
        st.dataframe(outliers)

    elif section == "Profiling Report":
        st.subheader("📋 Full Profiling Report")
        profile = ProfileReport(df, title="YData Profiling Report", explorative=True)
        st_profile_report(profile)

else:
    st.info("📁 Please upload a CSV file to begin.")