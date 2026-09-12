# Demo Video Script - Task 5: Sales Prediction

**Duration Target:** 4-5 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Science | Task 5: Sales Prediction | [Your Name]"

---

## SCENE 1: Introduction (20 seconds)
**Visual:** Show repo, open `sales_prediction.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 5: Sales Prediction. I build regression models to predict product sales from advertising spend across TV, Radio, and Newspaper channels."

---

## SCENE 2: Dataset & Cleaning (30 seconds)
**Visual:** Cells 1-2: dataset overview, null handling, outlier capping
**Script:**
> "The dataset has 200 records with TV, Radio, Newspaper spend predicting Sales. 18 missing values imputed with median, 2 outliers (TV=500, Sales=100) capped using IQR method. Clean dataset ready for modeling."

---

## SCENE 3: EDA & Correlation (45 seconds)
**Visual:** Cells 3-4: pairplot, scatter plots, correlation heatmap
**Script:**
> "Key finding: TV has strongest correlation with Sales at 0.77. Radio is moderate at 0.45. Newspaper is negligible at 0.01. Scatter plots confirm TV has the clearest linear relationship with Sales."

---

## SCENE 4: Model Training & Comparison (45 seconds)
**Visual:** Cells 5-6: Linear Regression vs Random Forest comparison table
**Script:**
> "I trained Linear Regression (baseline), Random Forest, and Polynomial Regression. Linear Regression wins with R²=0.936, RMSE=1.34. Random Forest R²=0.890, Polynomial R²=0.913. Linear Regression wins - simple and interpretable."

---

## SCENE 5: Coefficients & Feature Importance (30 seconds)
**Visual:** Cells 6-7: coefficient table, feature importance chart
**Script:**
> "Linear Regression coefficients: TV=4.25 (dominant), Radio=2.68, Newspaper=0.66. Random Forest importance: TV 66%, Radio 28%, Newspaper 5%. Both methods agree: TV is the dominant sales driver."

---

## SCENE 6: Residuals & Conclusion (20 seconds)
**Visual:** Cells 7: residual plots, conclusion
**Script:**
> "Residuals show Linear Regression has slight negative bias but low variance. Business recommendation: prioritize TV budget, maintain Radio, minimize Newspaper spend. Full code in notebook. Thank you!
> 
> #oasisinfobyte #datascience #salesprediction #regression #advertising"

---

## Recording Tips
- Show the correlation heatmap - TV's 0.77 is striking
- Highlight Linear Regression's 0.936 R² - strong result
- Emphasize business actionability of coefficients