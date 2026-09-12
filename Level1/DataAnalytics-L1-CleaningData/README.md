# Task 1: Cleaning Data

**Track:** Data Analytics - Level 1  
**Internship:** Oasis Infobyte SIP  

## Objective
Demonstrate professional-level data cleaning skills by taking a deliberately messy dataset and systematically transforming it into a clean, analysis-ready dataset. Document every decision.

## Dataset
- **Source:** Synthetic customer dataset (1050 rows, 12 columns) with intentional data quality issues
- **Issues included:** Missing values, duplicates, inconsistent categorical formatting, outliers, incorrect data types

## Tech Stack
- Python
- pandas
- numpy
- Jupyter Notebook

## Cleaning Pipeline Steps

### 1. Data Quality Report
- Null value analysis per column
- Duplicate row detection (47 duplicates found)
- Data type inspection
- Value range anomaly detection (age: 200, total_spent: -500, 999999)

### 2. Missing Data Handling
- **email**: Dropped rows (105 nulls, 10% - not critical for analysis)
- **gender**: Mode imputation ('Female')
- **city**: Mode imputation ('New York')
- **subscription_status**: Mode imputation ('Active')

### 3. Duplicate Removal
- Removed 42 duplicate rows (after email drops)
- Final unique rows: 903

### 4. Standardisation
- **gender**: 'Male'/'M'/'male' → 'Male', 'Female'/'F'/'female' → 'Female'
- **city**: 'NYC'→'New York', 'LA'→'Los Angeles', 'Chi'→'Chicago'
- **subscription_status**: 'active'/'ACTIVE'→'Active', 'inactive'/'cancelled'→'Inactive'
- **dates**: Converted to datetime64
- **phone**: Invalid entries marked as NaN

### 5. Outlier Detection & Handling (IQR Method)
- **age**: Capped at 18-100 (1 outlier at 200)
- **total_spent**: Capped at IQR upper bound (43 outliers, negative values set to 0)
- **purchase_count**: Capped at IQR upper bound (4 outliers)

### 6. Data Type Correction
- All columns assigned appropriate dtypes (int64, float64, datetime64, category, string)

## Results

| Metric | Before | After |
|--------|--------|-------|
| Row Count | 1,050 | 903 |
| Null Count (total) | 359 | 33 (phone only) |
| Duplicate Rows | 47 | 0 |
| Dtype Accuracy | Mixed | All correct |

## Files
- `cleaning_data.ipynb` - Main analysis notebook
- `cleaning_data_executed.ipynb` - Executed notebook with outputs
- `messy_customer_data.csv` - Original messy dataset
- `cleaned_customer_data.csv` - Final cleaned dataset (analysis-ready)

## Key Learnings
- Systematic approach to data quality assessment
- Strategic missing value handling with documented justification
- IQR method for outlier detection
- Importance of data type consistency for downstream analysis