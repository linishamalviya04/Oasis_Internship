# Task 2 (Level 2): Wine Quality Prediction

**Track:** Data Analytics - Level 2  
**Internship:** Oasis Infobyte SIP  

## Objective
Train and compare multiple classification models to predict the quality score of wine (scale of 3-8) based on its physicochemical properties such as acidity, density, and alcohol content.

## Dataset
- **Source:** Synthetic wine quality dataset (5,000 samples, 11 features) based on UCI Wine Quality dataset
- **Target:** Quality score (3-8), binned into 3 classes: Low (3-4), Medium (5-6), High (7-8)
- **Features:** 11 physicochemical properties (fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free/total sulfur dioxide, density, pH, sulphates, alcohol)

## Tech Stack
- Python, pandas, numpy, scikit-learn (Random Forest, SGD, SVC), seaborn, matplotlib, Jupyter Notebook

## Analysis Performed

### 1. Class Distribution Analysis
Original quality distribution (imbalanced):
- Quality 3: 509 (10.2%)
- Quality 4: 750 (15.0%)
- **Quality 5: 1,301 (26.0%)** ← Majority
- **Quality 6: 1,325 (26.5%)** ← Majority
- Quality 7: 786 (15.7%)
- Quality 8: 329 (6.6%)

Imbalance ratio: 4.03:1 (max/min)

**Solution:** Binned into 3 actionable classes:
- **Low (3-4)**: 1,259 samples (25.2%)
- **Medium (5-6)**: 2,626 samples (52.5%)
- **High (7-8)**: 1,115 samples (22.3%)

### 2. Exploratory Data Analysis
**Key Correlations with Quality:**
- `volatile_acidity`: **-0.55** (strongest negative)
- `sulphates`: **+0.39** (positive)
- `alcohol`: **+0.34** (positive)
- `chlorides`: **-0.23** (negative)

### 3. Feature Engineering & Preprocessing
- Binned quality into 3 classes (Low/Medium/High)
- StandardScaler for feature normalization
- Stratified train/test split (80/20) preserving class ratios
- Class weights computed for imbalance handling

### 4. Model Training (3 Classifiers)

#### Random Forest
- 200 trees, max_depth=15, balanced class weights
- **Accuracy: 70.9%**
- Macro F1: 0.694

#### SGD Classifier (Logistic Regression)
- Log loss, L2 penalty, balanced class weights
- **Accuracy: 65.9%**
- Macro F1: 0.666

#### Support Vector Classifier (SVC)
- RBF kernel, balanced class weights
- **Accuracy: 67.1%**
- Macro F1: 0.673

### 5. Model Comparison

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 |
|-------|----------|-----------------|--------------|----------|-------------|
| **Random Forest** | **70.9%** | **71.2%** | 68.0% | **69.4%** | **70.7%** |
| SGD Classifier | 65.9% | 65.6% | **71.5%** | 66.6% | 65.3% |
| SVC | 67.1% | 66.0% | 70.0% | 67.3% | 67.0% |

### 6. Feature Importance (Random Forest)
**Top Predictors:**
1. `volatile_acidity`: 25.8% (most important - negative correlation)
2. `sulphates`: 15.1%
3. `alcohol`: 14.3%
4. `chlorides`: 8.9%
4. `fixed_acidity`: 6.3%

### 7. AUC-ROC Performance
All models achieved **AUC > 0.95**, indicating excellent discriminative ability across all quality classes.

## Files
- `wine_quality_prediction.ipynb` - Main analysis notebook
- `wine_quality_prediction_executed.ipynb` - Executed notebook with outputs
- `wine_quality.csv` - Dataset used

## Conclusion
**Random Forest is the best model for deployment** because:
- Highest accuracy (70.9%) and weighted F1 (70.7%)
- Provides feature importance for interpretability
- Robust to outliers and non-linear relationships
- Handles class imbalance well with balanced weights

## Key Learnings
- Handling class imbalance in multi-class classification
- Feature binning for improved model performance and interpretability
- Comparing Random Forest, SGD, and SVC for tabular data
- Feature importance interpretation for business insights
- Stratified sampling for imbalanced datasets