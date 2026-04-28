# Gene Expression Data Analysis Pipeline

## Overview
This project is an end-to-end data analysis pipeline built on a gene expression dataset.  
It covers data loading, cleaning, exploratory analysis, visualization, and database integration using Python.

The goal of this project is to simulate a real-world bioinformatics/data science workflow.

---

## Dataset
The dataset consists of:
- `data.csv` → gene expression features (801 samples, 20,532 genes)
- `labels.csv` → sample labels (e.g., classification of samples)

After merging, the final dataset contains:
- 801 samples
- 20,534 features (including labels)

---

## Technologies Used
- Python 3
- Pandas
- NumPy
- Matplotlib
- SQLite3
- OpenPyXL (Excel export)

---

## Pipeline Steps

### 1. Data Loading
- Imported gene expression data and labels using pandas.

### 2. Data Merging
- Combined feature and label datasets using `pd.concat`.

### 3. Data Cleaning
- Checked and removed missing values.
- Verified dataset integrity (no duplicates).

### 4. Exploratory Data Analysis (EDA)
- Computed statistical summaries using NumPy/Pandas.
- Calculated gene-wise mean expression values.

### 5. Visualization
- Generated gene expression plots using Matplotlib.
- Saved visualization as `gene_plot.png`.

### 6. Database Integration
- Stored processed data in SQLite database (`gene_data.db`).
- Executed SQL queries using `sqlite3`.

### 7. Export
- Exported cleaned dataset to CSV.
- Exported sample dataset to Excel (`gene_expression_sample.xlsx`).

---

## Outputs
- `cleaned_dataset.csv`
- `gene_expression_sample.xlsx`
- `gene_data.db`
- `gene_plot.png`

---

## How to Run

```bash
pip install pandas numpy matplotlib openpyxl
python3 analysis.py
