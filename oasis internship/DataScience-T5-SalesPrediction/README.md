# Task 5: Sales Prediction Using Python

**Track:** Data Science  
**Internship:** Oasis Infobyte SIP  

## Objective
Build a regression model that predicts product sales based on advertising spend across different media channels (TV, Radio, Newspaper).

## Dataset
- **Source:** Synthetic dataset (200 records) inspired by classic "Advertising.csv"
- **Features:** TV, Radio, Newspaper advertising spend
- **Target:** Sales (units sold)
- **Issues:** 18 missing values, 2 outliers (TV=500, Sales=100)

## Tech Stack
- Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter Notebook

## Analysis Performed

### 1. Data Cleaning
- 18 missing values (5 TV, 5 Radio, 5 Newspaper, 3 Sales) → Median imputation
- 2 outliers detected via IQR (TV=500, Sales=100) → Capped at IQR bounds

### 2. EDA Findings
- **Correlation with Sales**: TV (0.77), Radio (0.45), Newspaper (0.01)
- **TV is the strongest predictor** - strongest linear relationship with Sales
- **Newspaper has negligible correlation** with Sales

### 3. Model Comparison

| Model | MAE | RMSE | R² |
|-------|-----|------|-----|
| **Linear Regression** | **1.141** | **1.343** | **0.936** |
| Random Forest | 1.435 | 1.765 | 0.890 |
| Polynomial Regression (deg=2) | 1.323 | 1.571 | 0.913 |

### 4. Best Model
**Linear Regression** - R² = **0.936**, RMSE = **1.343**, MAE = **1.141**

### 5. Feature Importance
**Linear Regression Coefficients:**
- TV: **4.247** (highest impact)
- Radio: **2.682** 
- Newspaper: **0.662** (minimal)

**Random Forest Feature Importance:**
- TV: **66.5%**
- Radio: **28.3%**
- Newspaper: **5.2%**

### 6. Polynomial Regression (Bonus)
- Degree 2 Polynomial: R² = 0.913 (between Linear and Random Forest)

## Business Insights
1. **TV advertising is the primary sales driver** (coefficient 4.25, importance 66.5%)
2. **Radio has moderate impact** (coefficient 2.68, importance 28.3%)
3. **Newspaper has minimal impact** (coefficient 0.66, importance 5.2%)
4. **Budget allocation**: Prioritize TV > Radio > Newspaper

## Files
- `sales_prediction.ipynb` - Main analysis notebook
- `sales_prediction_executed.ipynb` - Executed notebook with outputs
- `advertising_sales.csv` - Dataset

## Key Learnings
- Linear Regression provides interpretable coefficients for business decisions
- Random Forest captures non-linear relationships but overfits slightly on small data
- TV is the dominant sales driver - allocate budget accordingly
- Feature importance aligns with correlation analysis
- Model can guide real-world advertising budget allocation