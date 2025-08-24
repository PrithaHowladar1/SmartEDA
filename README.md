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

<img width="1856" height="1023" alt="Screenshot 2025-08-25 024154" src="https://github.com/user-attachments/assets/8d6a33af-cb3e-4026-bb24-529953c26306" />
<img width="1854" height="1030" alt="Screenshot 2025-08-25 024226" src="https://github.com/user-attachments/assets/1d604527-e04c-4352-95ee-50b71ca33903" />
<img width="1858" height="1028" alt="Screenshot 2025-08-25 024251" src="https://github.com/user-attachments/assets/dcf2d7ae-7497-4657-a82f-fb66815eeb48" />
<img width="1844" height="1008" alt="Screenshot 2025-08-25 024319" src="https://github.com/user-attachments/assets/cc7e395a-c155-4463-bcb9-2c623934e118" />
<img width="1860" height="1019" alt="Screenshot 2025-08-25 024339" src="https://github.com/user-attachments/assets/4b809898-8314-4cc4-a696-8fcf6fce43a1" />
<img width="1853" height="1024" alt="Screenshot 2025-08-25 024352" src="https://github.com/user-attachments/assets/40f11ecf-b80d-4861-b954-a4e1c01edf20" />
<img width="1849" height="1018" alt="Screenshot 2025-08-25 024414" src="https://github.com/user-attachments/assets/5ad9f11c-dc57-44cb-9bd8-807a54e23ba0" />
<img width="1836" height="1036" alt="Screenshot 2025-08-25 024427" src="https://github.com/user-attachments/assets/78043a51-88be-40ae-8c9d-9632381bdb48" />
<img width="1855" height="1032" alt="Screenshot 2025-08-25 024528" src="https://github.com/user-attachments/assets/b7882e3d-7594-49fd-aaf7-5257ad4e302c" />
<img width="1844" height="1023" alt="Screenshot 2025-08-25 024602" src="https://github.com/user-attachments/assets/0ad87767-3441-47a4-a9f8-9a73c97e093b" />
<img width="1742" height="1028" alt="Screenshot 2025-08-25 024627" src="https://github.com/user-attachments/assets/c2524c73-314f-4c83-992b-a500b53c7b43" />
<img width="1852" height="1035" alt="Screenshot 2025-08-25 024701" src="https://github.com/user-attachments/assets/1657e0d7-a988-4c08-b525-90a3c27a0a06" />














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

