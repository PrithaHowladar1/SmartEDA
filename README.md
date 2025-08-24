SmartEDA is a powerful, interactive data profiling tool built with Streamlit, YData Profiling, and Pandas. It empowers data scientists, analysts, and engineers to explore datasets visually, detect quality issues, and prepare data for modeling—all in one elegant interface.
From correlation heatmaps to missing value imputation, outlier detection, data quality warnings, distribution plots, and feature interactions—SmartEDA brings together everything you need for fast, intuitive, and thorough exploratory data analysis.

Key Features-

**📁 Upload & Preview**
- Upload CSV files directly from the UI
- View the first few rows of your dataset instantly


  
**📊 Column Summary Panel**
- Select any numeric column
- View key statistics- **mean, median, mode, std dev, skewness, min/max, missing values**


  
**🧼 Missing Value Imputation**
- Choose how to fill missing values- **Mean, Median, Mode, Custom value**
- Impute directly from the UI


  
**🚨 Outlier Detection**
- Detect outliers using- **Z-score method, IQR method**
- View flagged rows and export for review



**📈 Correlation Analysis**
Compute correlation matrix using- **Pearson, Spearman, Kendall**
- Visualize with interactive heatmaps


  
**🧪 Data Quality Warnings**
- Automatic detection of- **Missing values, Duplicate rows, Constant columns**
- High cardinality categorical features


  
**📋 Full Profiling Report**
- Generate a complete EDA report using YData Profiling
- Embedded directly in the app
- Includes distributions, interactions, correlations, missing data, and more



**🎛️ Sidebar Navigation**
- Modular layout with section toggles
- Choose which analysis to view
- Clean, responsive interface



**Frontend & UI**
- [Streamlit](https://streamlit.io/) – Interactive web app framework for Python
- [Plotly](https://plotly.com/python/) – Interactive visualizations
- [Seaborn](https://seaborn.pydata.org/) – Statistical data visualization
- [Matplotlib](https://matplotlib.org/) – Core plotting library

**EDA & Data Profiling**
- [Pandas](https://pandas.pydata.org/) – Data manipulation and analysis
- [YData Profiling](https://docs.ydata.ai/docs/profiling/) – Automated EDA report generation
- [NumPy](https://numpy.org/) – Numerical computing
- [SciPy](https://scipy.org/) – Z-score and statistical utilities

**Data Cleaning & Analysis**
- Custom logic for:
  - Missing value imputation
  - Outlier detection (Z-score, IQR)
  - Duplicate and constant column detection
  - Correlation analysis (Pearson, Spearman, Kendall)

**Deployment (Optional)**
- [Streamlit Cloud](https://streamlit.io/cloud) – One-click app hosting
- [Hugging Face Spaces](https://huggingface.co/spaces) – Free hosting for ML apps

**Environment**
- Python 3.10+
- Conda or virtualenv recommended

