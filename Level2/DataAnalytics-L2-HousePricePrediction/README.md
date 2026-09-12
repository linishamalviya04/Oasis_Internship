# Task 1 (Level 2): Predicting House Prices with Linear Regression

**Track:** Data Analytics - Level 2  
**Internship:** Oasis Infobyte SIP  

## Objective
Build and evaluate a linear regression model that predicts house prices based on features such as area, location, number of rooms, and age. Develop end-to-end skills from data cleaning through to model interpretation.

## Dataset
- **Source:** Synthetic house price dataset (2,000 records, 33 features) inspired by Ames Housing dataset
- **Target:** Sale Price ($126K - $630K, mean $315K)
- **Features:** 21 numeric (area, rooms, year built, quality scores) + 11 categorical (neighborhood, building type, style, etc.)

## Tech Stack
- Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter Notebook

## Analysis Performed

### 1. Data Loading & EDA
- Loaded 2,000 records with 33 features
- Target variable: sale_price (range $126K-$630K, mean $315K)
- No missing values in target, ~5% missing in some features

### 2. Feature Selection
**High Impact Predictors:**
- `gr_liv_area` (Above ground living area) - Direct measure of usable space
- `total_bsmt_sf` (Total basement area) - Additional living/storage space
- `overall_qual` (Overall material and finish quality) - Quality directly affects value
- `garage_cars` / `garage_area` - Garage capacity is highly valued
- `year_built` / `year_remod_add` - Age and renovation status
- `neighborhood` - Location is paramount in real estate

### 3. Preprocessing
- Missing value imputation (median for numeric, mode for categorical)
- One-Hot encoding for 8 categorical features
- StandardScaler for numeric features
- Final feature count: 88 (after encoding)

### 4. Correlation Analysis
Top correlates with price:
- `overall_qual`: 0.73
- `gr_liv_area`: 0.57
- `second_flr_sf`: 0.41
- `first_flr_sf`: 0.38
- `garage_area`: 0.23

### 5. Linear Regression Results
| Metric | Train | Test |
|--------|-------|------|
| R² | 0.9406 | **0.9374** |
| RMSE | $14,718 | **$15,331** |
| MAE | $11,703 | $12,312 |

Model explains **93.7%** of price variance on test set.

### 6. Residual Analysis
- Mean residual: -$942 (slight underprediction)
- Residuals approximately normally distributed (skewness: 0.034)
- No systematic patterns in residual plots

### 7. Coefficient Analysis
**Top Positive Drivers:**
1. `overall_qual`: +$43,008 per quality point
2. `gr_liv_area`: +$16,582 per sq ft
3. `garage_area`: +$13,522 per sq ft
4. `second_flr_sf`: +$12,222 per sq ft

**Top Negative Drivers:**
1. `sale_type_ConLw`: -$8,833
2. `roof_style_Flat`: -$8,090

### 8. Regularization Comparison
| Model | Test R² | Test RMSE | Non-zero Coeff |
|-------|---------|-----------|----------------|
| Linear Regression | 0.9374 | $15,331 | 88/88 |
| Ridge (α=19.31) | 0.9374 | $15,331 | 88/88 |
| Lasso (α=323.75) | 0.9368 | $15,352 | **11/88** |

Lasso performed automatic feature selection, keeping only 11 most important features.

## Files
- `house_price_prediction.ipynb` - Main analysis notebook
- `house_price_prediction_executed.ipynb` - Executed notebook with outputs
- `house_prices.csv` - Dataset used

## Key Learnings
- End-to-end regression pipeline from EDA to model interpretation
- Correlation analysis for feature selection
- Linear regression with proper evaluation metrics
- Residual diagnostics for model validation
- Regularization techniques (Ridge/Lasso) for feature selection
- Coefficient interpretation for business insights