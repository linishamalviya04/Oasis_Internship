# Task 4: Email Spam Detection with Machine Learning

**Track:** Data Science  
**Internship:** Oasis Infobyte SIP  

## Objective
Build a Natural Language Processing (NLP) binary classifier that distinguishes spam emails from legitimate (ham) emails.

## Dataset
- **Source:** Synthetic SMS dataset (5,000 messages, 3,000 ham, 2,000 spam)
- **Features:** Message text
- **Target:** Binary classification (0 = Ham, 1 = Spam)
- **Class Distribution:** 60% Ham, 40% Spam

## Tech Stack
- Python, pandas, scikit-learn (TF-IDF, Naive Bayes/SVM), NLTK, Jupyter Notebook

## Analysis Performed

### 1. Text Preprocessing
- Lowercasing
- Punctuation removal
- Stopword removal (NLTK English stopwords)
- Stemming (Porter Stemmer)

### 2. Feature Extraction: TF-IDF
- **Vectorizer**: TF-IDF with n-grams (1,2), max 5000 features
- **Vocabulary Size**: 252 features
- **Top Spam Indicators**: 'win', 'free', 'prize', 'click', 'claim', 'urgent', 'cash', 'congratulations', 'call', 'claim'
- **Top Ham Indicators**: 'meeting', 'thanks', 'please', 'tomorrow', 'schedule', 'call', 'meeting', 'know'

### 3. Models Trained
| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Multinomial Naive Bayes** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| **Logistic Regression** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| **SVM (Linear)** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |

### 4. Best Model
All three models achieved **perfect 1.0000 F1-Score** on this synthetic dataset. Multinomial Naive Bayes is selected as best (industry standard for text classification).

## Key Insight: Why Recall > Precision for Spam Detection
- **False Negative (Missed Spam)**: Spam reaches inbox → phishing risk, malware, user annoyance
- **False Positive (False Alarm)**: Legitimate email in spam folder → user checks spam folder
- **Cost of missing spam >> Cost of false alarm**

## Files
- `spam_detection.ipynb` - Main analysis notebook
- `spam_data.csv` - Dataset

## Key Learnings
- TF-IDF + Naive Bayes is industry standard for text classification
- N-grams capture spam phrases like "click here", "free money"
- Class imbalance handled with balanced class weights
- Recall prioritized over precision for spam detection
- Perfect scores achieved on synthetic dataset