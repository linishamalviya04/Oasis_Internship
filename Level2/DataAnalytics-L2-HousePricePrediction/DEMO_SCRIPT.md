# Demo Video Script - Task 1 (Level 2): House Price Prediction

**Duration Target:** 4-6 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Analytics Level 2 | Task 1: House Price Prediction | [Your Name]"

---

## SCENE 1: Introduction (30 seconds)
**Visual:** Show GitHub repo, open `house_price_prediction.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 1 Level 2: Predicting House Prices with Linear Regression for the Oasis Infobyte Data Analytics internship.
> 
> I build and evaluate a linear regression model to predict house prices using features like living area, quality, garage, and neighborhood. The dataset has 2,000 houses with 33 features, inspired by the Ames Housing dataset."

---

## SCENE 2: Data Loading & EDA (45 seconds)
**Visual:** Cells 1-2: dataset shape, target distribution, feature types
**Script:**
> "The dataset has 2,000 records with 33 features. Sale price ranges from $126K to $630K with mean $315K. Features include 21 numeric (areas, rooms, years) and 11 categorical (neighborhood, building type, style). No missing values in target, about 5% missing in some features like masonry veneer area."

---

## SCENE 3: Feature Selection & Correlation (60 seconds)
**Visual:** Cells 3-5: feature discussion markdown, correlation bar chart, heatmap
**Script:**
> "I identify key predictors: living area, basement area, overall quality, garage, year built, and neighborhood. Correlation analysis confirms: overall quality correlates 0.73 with price, living area 0.57, second floor area 0.41. I avoid multicollinearity by using composite features like total living area instead of separate floor areas."

---

## SCENE 4: Preprocessing & Model Training (45 seconds)
**Visual:** Cells 6-8: preprocessing pipeline, train/test split, model fitting
**Script:**
> "Preprocessing: median imputation for numeric, mode for categorical, One-Hot encoding for 8 categorical features, StandardScaler. 80/20 train/test split. Linear Regression trained on 88 features after encoding. Test R-squared is 0.937 - the model explains 93.7% of price variance. RMSE is $15,331."

---

## SCENE 5: Residual Analysis & Coefficients (60 seconds)
**Visual:** Cells 9-10: residual plots, coefficient bar chart
**Script:**
> "Residual analysis shows mean residual of -$942 with normal distribution (skewness 0.03). No systematic patterns - good model fit. Top positive coefficients: overall quality (+$43K per point), living area (+$16K per sq ft), garage area (+$13K per sq ft). Negative coefficients for certain sale types and flat roofs."

---

## SCENE 6: Regularization Comparison (45 seconds)
**Visual:** Cells 11-12: Ridge/Lasso results table, coefficient comparison chart
**Script:**
> "Bonus: Ridge and Lasso regularization. Ridge (alpha=19.3) matches Linear Regression. Lasso (alpha=324) performs automatic feature selection - only 11 of 88 features kept, with similar R-squared. This shows only a few features truly drive price."

---

## SCENE 7: Conclusion (15 seconds)
**Visual:** Conclusion markdown, GitHub repo
**Script:**
> "The model achieves 93.7% R-squared with $15K RMSE. Living area and quality are dominant price drivers. Regularization helps with feature selection. Full code and outputs in the notebook. Thank you!
> 
> #oasisinfobyte #dataanalytics #linearregression #houseprices #python"

---

## Recording Tips
- Record at 1080p minimum
- Zoom in on charts when explaining
- Keep mouse movements smooth
- Pause 2 seconds between sections