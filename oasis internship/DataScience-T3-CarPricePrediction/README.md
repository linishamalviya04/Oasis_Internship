# Task 3: Car Price Prediction with Machine Learning

**Track:** Data Science  
**Internship:** Oasis Infobyte SIP  

## Objective
Build a regression model that predicts the selling price of a used car based on features such as brand, age, mileage, fuel type, and transmission.

## Dataset
- **Source:** Synthetic dataset (3,000 records) inspired by CarDekho dataset
- **Features:** 13 columns including Name, Year, Present_Price, Kms_Driven, Fuel_Type, Transmission, etc.
- **Target:** Selling_Price (in Lakhs INR)

## Tech Stack
- Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter Notebook

## Analysis Performed

### 1. Data Cleaning & Feature Engineering
- No missing values, no duplicates
- Created `Car_Age` (2022 - Year)
- Extracted `Brand` from Name column
- Log-transformed skewed features (Kms_Driven, Selling_Price)

### 2. EDA Findings
- **Target distribution**: Right-skewed, log-normal after transform
- **Top correlations with Selling_Price**:
  - Present_Price: **0.57** (strongest)
  - Car_Age: **-0.53**
  - Kms_Driven: **-0.36**
- Diesel cars priced higher than Petrol
- Automatic transmission commands premium

### 3. Models Trained
| Model | MAE | RMSE | R² |
|-------|-----|------|-----|
| **Gradient Boosting** | **0.465** | **0.594** | **0.949** |
| Random Forest | 0.534 | 0.709 | 0.927 |
| Linear Regression | 1.036 | 1.362 | 0.732 |

### 4. Best Model
**Gradient Boosting Regressor** - R² = **0.949**, RMSE = **0.594 Lakhs**

### 5. Feature Importance (Gradient Boosting)
1. **Present_Price**: 38.9%
2. **Car_Age**: 37.1%
3. **Kms_Driven**: 19.4%
4. Owner_First: 1.9%
5. Power: 0.6%

## Files
- `car_price_prediction.ipynb` - Main analysis notebook
- `car_price_prediction_executed.ipynb` - Executed notebook with outputs
- `car_data.csv` - Dataset

## Key Insights
- Present_Price is the strongest predictor (expected)
- Tree-based models significantly outperform Linear Regression
- Gradient Boosting captures non-linear relationships best
- Feature engineering (Car_Age, Brand) adds predictive value
- Residuals centered near zero with no systematic patterns