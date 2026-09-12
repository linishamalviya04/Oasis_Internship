# Demo Video Script - Task 3: Car Price Prediction

**Duration Target:** 4-5 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Science | Task 3: Car Price Prediction | [Your Name]"

---

## SCENE 1: Introduction (20 seconds)
**Visual:** Show repo, open `car_price_prediction.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 3: Car Price Prediction. I build regression models to predict used car selling prices using features like brand, age, mileage, fuel type, and transmission."

---

## SCENE 2: Dataset & Feature Engineering (30 seconds)
**Visual:** Cells 1-2: dataset overview, feature engineering
**Script:**
> "The dataset has 3,000 cars with 13 features. I created Car_Age from Year, extracted Brand from Name, and log-transformed skewed features like Kms_Driven. No missing values or duplicates."

---

## SCENE 3: EDA & Correlations (45 seconds)
**Visual:** Cells 3-4: target distribution, box plots, correlation heatmap
**Script:**
> "Selling price is right-skewed. Key correlations: Present_Price 0.57 (strongest), Car_Age -0.53, Kms_Driven -0.36. Diesel cars priced higher than Petrol. Automatic transmission commands premium."

---

## SCENE 4: Model Training & Comparison (60 seconds)
**Visual:** Cells 5-6: three models training, comparison table, bar charts
**Script:**
> "I trained three models: Linear Regression, Random Forest, and Gradient Boosting with proper preprocessing pipelines. Results: Gradient Boosting wins with R²=0.949, RMSE=0.594 Lakhs. Random Forest close at 0.927. Linear Regression only 0.732 - non-linear relationships need tree-based models."

---

## SCENE 5: Residuals & Feature Importance (45 seconds)
**Visual:** Cells 7-8: actual vs predicted, residual plot, feature importance chart
**Script:**
> "Gradient Boosting predictions closely match actual values. Residuals centered near zero - no systematic bias. Feature importance: Present_Price 39%, Car_Age 37%, Kms_Driven 19%. Present price and car age dominate."

---

## SCENE 6: Conclusion (15 seconds)
**Visual:** Conclusion markdown, GitHub repo
**Script:**
> "Gradient Boosting achieves 94.9% R² with 0.59 Lakhs RMSE. Present price and car age are dominant predictors. Tree-based models capture non-linear depreciation patterns. Full code in notebook. Thank you!
> 
> #oasisinfobyte #datascience #carprice #regression #gradientboosting"

---

## Recording Tips
- Show the model comparison chart prominently
- Highlight the 0.949 R² - strong result
- Mention the 3x improvement over Linear Regression