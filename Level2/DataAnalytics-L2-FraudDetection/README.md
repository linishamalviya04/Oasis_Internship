# Task 3 (Level 2): Fraud Detection

**Track:** Data Analytics - Level 2  
**Internship:** Oasis Infobyte SIP  

## Objective
Build a machine learning pipeline to detect fraudulent financial transactions from a heavily imbalanced dataset, addressing class imbalance as a core challenge.

## Dataset
- **Source:** Synthetic credit card fraud dataset (50,000 transactions) inspired by Kaggle Credit Card Fraud dataset
- **Target:** Binary classification (0 = Normal, 1 = Fraud)
- **Fraud Rate:** 0.5% (250 frauds, 49,750 normal)
- **Imbalance Ratio:** 199:1
- **Features:** Time, V1-V28 (PCA components), Amount

## Tech Stack
- Python, pandas, scikit-learn, imbalanced-learn (SMOTE), matplotlib, seaborn, Jupyter Notebook

## Analysis Performed

### 1. Class Imbalance Analysis
- **Normal transactions:** 49,750 (99.5%)
- **Fraud transactions:** 250 (0.5%)
- **Imbalance ratio:** 199:1

**Why Accuracy Fails:** A model predicting "Normal" for all transactions achieves 99.5% accuracy but catches **zero fraud**.

### 2. Exploratory Data Analysis
**Transaction Amounts:**
- Normal: Mean $61, Median $20, Max $5,000
- Fraud: Mean $80, Median $52, Max $737
- Fraud amounts typically higher

**Time of Day Analysis:**
- Fraud rate varies by hour
- Higher fraud rates during off-peak hours

### 3. Why Standard Accuracy is Misleading
| Model | Accuracy | Fraud Detected |
|-------|----------|----------------|
| Always "Normal" | **99.5%** | **0%** (Useless!) |

**Proper Metrics for Fraud:**
- **Recall (Sensitivity)**: Of actual frauds, how many caught? → **Priority #1**
- **Precision**: Of predicted frauds, how many real? → Minimize false alarms
- **F1-Score**: Harmonic mean of precision/recall
- **AUC-ROC**: Threshold-independent performance

**Business Reality:** Missing fraud (False Negative) costs >> False alarm (False Positive)

### 4. Imbalance Handling Techniques

#### Technique 1: Class Weight Balancing
- Adjusts loss function: `class_weight='balanced'`
- No data modification, works with any model

#### Technique 2: SMOTE Oversampling
- Synthetic Minority Over-sampling Technique
- Generates synthetic fraud samples
- Applied **only on training data** (no data leakage)
- Balanced training set: 39,800 normal + 39,800 fraud (50/50)

### 5. Models Trained (4 Configurations)

| Model | Technique | Precision | Recall | F1-Score | AUC-ROC |
|-------|-----------|-----------|--------|----------|---------|
| Logistic Regression | class_weight=balanced | 84.2% | **96.0%** | 89.7% | 0.9999 |
| Logistic Regression | SMOTE | **87.3%** | **96.0%** | **91.4%** | 0.9999 |
| Random Forest | class_weight=balanced | **100%** | **100%** | **100%** | **1.0000** |
| Random Forest | SMOTE | **100%** | **100%** | **100%** | **1.0000** |

### 6. Model Comparison Results

**Best Model: Random Forest** (both balanced and SMOTE achieve perfect scores on test set)

| Metric | LR (Balanced) | LR (SMOTE) | RF (Balanced) | RF (SMOTE) |
|--------|---------------|------------|---------------|------------|
| Precision | 84.2% | 87.3% | **100%** | **100%** |
| Recall | 96.0% | 96.0% | **100%** | **100%** |
| F1-Score | 89.7% | 91.4% | **100%** | **100%** |
| AUC-ROC | 0.9999 | 0.9999 | **1.0000** | **1.0000** |

### 7. Feature Importance (Random Forest SMOTE)
**Top 5 Predictors:**
1. **Time**: 46.7% (transaction timing pattern)
2. **V19**: 9.4%
3. **V1**: 6.4%
4. **V10**: 6.3%
5. **V4**: 5.3%

### 8. AUC-ROC Curves
All models achieved **AUC > 0.9999**, indicating near-perfect discriminative ability.

### 9. Scalability Discussion (1M Transactions/Hour)
**Real-time Requirements:** <10ms per transaction

| Model | Latency | Scalability | Use Case |
|-------|---------|-------------|----------|
| Logistic Regression | ~0.1ms | Excellent | Real-time scoring |
| Random Forest | ~1-5ms | Good | Review queue |

**Production Architecture:**
- **Real-time**: Logistic Regression (<1ms) for instant decisions
- **Review Queue**: Random Forest for high-risk transactions
- **Threshold**: Optimize for Recall > 90%, Precision > 30%
- **Monitoring**: Daily PSI checks, weekly retraining

### 9. Recall vs Precision Trade-off
**Fraud Detection Priority: RECALL**
- Missing fraud (False Negative) = Full transaction loss + reputation
- False alarm (False Positive) = Investigation time only
- **Optimize for Recall > 90%** while maintaining Precision > 30%
- Use F1-Score or AUC-ROC for threshold optimization

## Files
- `fraud_detection.ipynb` - Main analysis notebook
- `fraud_detection_executed.ipynb` - Executed notebook with outputs
- `credit_card_fraud.csv` - Dataset used

## Key Learnings
- **Accuracy is meaningless** for imbalanced fraud detection
- **Recall is the primary metric** - missing fraud costs more than false alarms
- **SMOTE + Random Forest** provides excellent performance for tabular fraud data
- **Logistic Regression** is fastest for real-time scoring (<1ms)
- **Class weights** are simpler alternative to SMOTE
- **Production systems** need ensemble approach: fast LR + accurate RF
- **Monitoring** essential: feature drift, prediction drift, precision/recall tracking

## Files
- `fraud_detection.ipynb` - Main analysis notebook
- `fraud_detection_executed.ipynb` - Executed notebook with outputs
- `credit_card_fraud.csv` - Dataset used