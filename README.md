# Gene Expression Data Analysis Pipeline

## Overview
This project is an end-to-end data analysis pipeline built on a gene expression dataset.  
It covers data loading, cleaning, exploratory analysis, visualization, and database integration using Python.

The goal of this project is to simulate a real-world bioinformatics/data science workflow.

---

## Dataset
This project uses publicly avaliable gene expression datasetes from Kaggle.

Due to size constraints (>100MB GitHub limit), the full dataset is not included in this repository.
You can access it here: https://www.kaggle.com/datasets/waalbannyantudre/gene-expression-cancer-rna-seq-donated-on-682016/data


The processed data and outputs are avaliable below:

[Access Processed Data] (]https://drive.google.com/drive/folders/1l7HhFUaAUwQZBvIdTEtVDMp4GT6A2LDn?usp=drive_link)

Contents:
-Cleaned dataset (CSV)
- Excel sample output
- SQLite database file (.db)

These files demonstrate the data cleaning, transformation and database integration steps used in this project.

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
- Exported sample dataset to Excel ('gene_expression_sample.xlsx').

-----

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
