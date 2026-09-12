# Demo Video Script - Task 2 (Level 2): Wine Quality Prediction

**Duration Target:** 4-6 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Analytics Level 2 | Task 2: Wine Quality Prediction | [Your Name]"

---

## SCENE 1: Introduction (30 seconds)
**Visual:** Show repo, open `wine_quality_prediction.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 2 Level 2: Wine Quality Prediction. I train and compare three classification models - Random Forest, SGD, and SVC - to predict wine quality from 11 physicochemical properties like acidity, alcohol, and sulphates."

---

## SCENE 2: Data & Class Imbalance (45 seconds)
**Visual:** Cells 1-2: dataset overview, quality distribution chart, imbalance analysis
**Script:**
> "The dataset has 5,000 wines with 11 features. Quality scores 3-8 are imbalanced: qualities 5 and 6 dominate at 52%, while 3 and 8 are rare at 10% and 6.6%. Imbalance ratio is 4:1. I bin into 3 actionable classes: Low (3-4), Medium (5-6), High (7-8)."

---

## SCENE 3: EDA & Key Correlations (45 seconds)
**Visual:** Cells 3-4: feature distributions by quality, correlation heatmap, key correlations table
**Script:**
> "Key correlations with quality: volatile acidity -0.55 (strongest negative), sulphates +0.39, alcohol +0.34, chlorides -0.23. Alcohol and sulphates increase quality; volatile acidity decreases it. Binned classes: Low 25%, Medium 53%, High 22% - much better balance."

---

## SCENE 5: Model Training (60 seconds)
**Visual:** Cells 5-8: preprocessing, three model training cells with outputs
**Script:**
> "Three models with balanced class weights: Random Forest (200 trees), SGD Classifier (log loss), SVC (RBF kernel). Stratified 80/20 split preserves class ratios. Class weights computed for imbalance handling. All models trained on scaled features."

---

## SCENE 6: Model Evaluation & Comparison (60 seconds)
**Visual:** Cells 9-10: classification reports, confusion matrices, comparison table, bar charts
**Script:**
> "Results: Random Forest 71% accuracy, 69% macro F1. SGD 66%, SVC 67%. Random Forest wins on accuracy and weighted F1. SGD has highest recall (71%) but lower precision. All models AUC > 0.95. Random Forest best for deployment - highest accuracy, provides feature importance."

---

## SCENE 7: Feature Importance & Conclusion (30 seconds)
**Visual:** Cells 11-12: feature importance chart, conclusion
**Script:**
> "Random Forest feature importance: volatile acidity 26% (top predictor), sulphates 15%, alcohol 14%. These align with correlation analysis. Random Forest recommended for deployment - best accuracy, interpretable, robust. Thank you!
> 
> #oasisinfobyte #dataanalytics #winequality #classification #randomforest"

---

## Recording Tips
- Highlight class imbalance early - key challenge
- Show confusion matrices - visual proof of performance
- Emphasize Random Forest's feature importance for business value