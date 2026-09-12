# Demo Video Script - Task 1: Iris Flower Classification

**Duration Target:** 3-4 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Science | Task 1: Iris Classification | [Your Name]"

---

## SCENE 1: Introduction (20 seconds)
**Visual:** Show repo, open `iris_classification.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 1: Iris Flower Classification for the Oasis Infobyte Data Science track. I build and compare multiple classifiers to identify iris species from 4 physical measurements."

---

## SCENE 2: Dataset & EDA (45 seconds)
**Visual:** Cells 1-2: dataset overview, species balance, descriptive stats
**Script:**
> "The Iris dataset has 150 samples, 4 features, 3 species - perfectly balanced at 50 each. No missing values. Key finding: petal length and width are highly correlated (0.96) and clearly separate all three species. Sepal width is the least discriminative."

---

## SCENE 3: Visualizations (30 seconds)
**Visual:** Cells 3-4: pairplot, box plots
**Script:**
> "The pairplot shows setosa is completely separate from versicolor and virginica. Petal measurements create clear decision boundaries. Box plots confirm petal features have zero overlap between setosa and others."

---

## SCENE 4: Model Training & Results (45 seconds)
**Visual:** Cells 5-7: train/test split, 4 models training, accuracy comparison
**Script:**
> "I train 4 classifiers with 80/20 stratified split: Logistic Regression, KNN (k=3), Decision Tree, Random Forest. Results: KNN achieves 100% accuracy, Logistic Regression 96.7%, Decision Tree 93.3%, Random Forest 90%. KNN wins with perfect classification."

---

## SCENE 5: Confusion Matrices & Feature Importance (30 seconds)
**Visual:** Cells 7-8: confusion matrices, feature importance
**Script:**
> "KNN has zero misclassifications. Feature importance from tree models confirms petal length and width are the top predictors - consistent with EDA findings."

---

## SCENE 6: Conclusion (15 seconds)
**Visual:** Conclusion markdown, GitHub repo
**Script:**
> "The Iris dataset is ideal for learning classification - well-separated classes make even simple models effective. KNN achieves 100% accuracy. Full code and outputs in the notebook. Thank you!
> 
> #oasisinfobyte #datascience #iris #classification #knn"

---

## Recording Tips
- Show pairplot prominently - it's the most visually impressive
- Highlight the 100% accuracy result
- Mention this is a "toy" dataset - real world data is noisier