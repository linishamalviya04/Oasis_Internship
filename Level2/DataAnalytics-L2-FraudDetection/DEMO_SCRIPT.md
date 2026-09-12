# Demo Video Script - Task 3 (Level 2): Fraud Detection

**Duration Target:** 5-7 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Analytics Level 2 | Task 3: Fraud Detection | [Your Name]"

---

## SCENE 1: Introduction (30 seconds)
**Visual:** Show repo, open `fraud_detection.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 3 Level 2: Fraud Detection. I build a machine learning pipeline to detect fraudulent credit card transactions from a heavily imbalanced dataset - 0.5% fraud rate, 199:1 imbalance ratio."

---

## SCENE 2: The Imbalance Problem (45 seconds)
**Visual:** Cell 2: class counts, imbalance ratio, "Why Accuracy Fails" markdown
**Script:**
> "The dataset has 50,000 transactions: 49,750 normal, only 250 fraud (0.5%). If a model always predicts 'Normal', it gets 99.5% accuracy but catches ZERO fraud. This is why accuracy is meaningless for fraud detection. We need Recall, Precision, F1, AUC-ROC."

---

## SCENE 3: EDA & Fraud Patterns (45 seconds)
**Visual:** Cell 4: amount distributions, time-of-day analysis
**Script:**
> "Fraud transactions have higher amounts (mean $80 vs $61) and different time patterns. Fraud rate varies by hour - higher during off-peak. V1-V28 are PCA components showing distinct patterns for fraud vs normal."

---

## SCENE 4: Imbalance Handling - SMOTE (45 seconds)
**Visual:** Cell 8: SMOTE explanation, before/after class distribution
**Script:**
> "Two techniques tested: class_weight='balanced' (adjusts loss function) and SMOTE (synthetic oversampling). SMOTE creates synthetic fraud samples, balancing training to 50/50 (39,800 each). Applied only on training data - no data leakage."

---

## SCENE 5: Model Training (60 seconds)
**Visual:** Cells 10-13: four model configurations training
**Script:**
> "Four configurations: 1) Logistic Regression with class weights, 2) Logistic Regression with SMOTE, 3) Random Forest with class weights, 4) Random Forest with SMOTE. All evaluated on held-out test set with proper metrics."

---

## SCENE 6: Results & Comparison (90 seconds)
**Visual:** Cells 15-17: classification reports, confusion matrices, comparison table, ROC curves
**Script:**
> "Results: Logistic Regression gets 96% recall but 84% precision. Random Forest achieves 100% precision AND recall - perfect scores! AUC-ROC is 1.0000 for both Random Forest configs. Random Forest with SMOTE is best for deployment."

---

## SCENE 7: Feature Importance & Coefficients (45 seconds)
**Visual:** Cells 19-20: feature importance chart, logistic regression coefficients
**Script:**
> "Random Forest feature importance: Time (47%), V19 (9%), V1 (6%), V10 (6%). Time is top predictor - fraud timing patterns. Logistic Regression coefficients show V19, V1 as strongest negative predictors (increase fraud probability)."

---

## SCENE 8: Scalability & Conclusion (45 seconds)
**Visual:** Cells 22-23: scalability markdown, conclusion
**Script:**
> "For 1M transactions/hour (278 TPS): Logistic Regression <1ms for real-time, Random Forest 1-5ms for review queue. Recommended: LR for real-time, RF for review queue. Optimize threshold for Recall >90%, Precision >30%. Key takeaway: Recall > Precision in fraud - missing fraud costs more than false alarms. Thank you!
> 
> #oasisinfobyte #dataanalytics #frauddetection #imbalancedlearning #smote"

---

## Recording Tips
- Emphasize the accuracy paradox early - memorable hook
- Show confusion matrices side-by-side - visual impact
- Highlight Random Forest's perfect scores - strong result
- Discuss scalability - shows production thinking