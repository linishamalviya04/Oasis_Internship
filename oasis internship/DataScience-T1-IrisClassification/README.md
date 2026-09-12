# Task 1: Iris Flower Classification

**Track:** Data Science  
**Internship:** Oasis Infobyte SIP  

## Objective
Train a machine learning classification model to identify the species of an iris flower (Setosa, Versicolor, or Virginica) from its physical measurements.

## Dataset
- **Source:** Built-in sklearn dataset (`sklearn.datasets.load_iris()`)
- **Samples:** 150 (50 per species)
- **Features:** 4 measurements (sepal length, sepal width, petal length, petal width)
- **Target:** 3 classes (setosa, versicolor, virginica) - perfectly balanced

## Tech Stack
- Python, scikit-learn, pandas, matplotlib/seaborn, Jupyter Notebook

## Analysis Performed

### 1. EDA
- No missing values, perfectly balanced classes (50 each)
- **Key correlations**: Petal length & width highly correlated (0.96)
- **Discriminative features**: Petal length & width clearly separate all 3 species; Sepal width least discriminative
- Setosa linearly separable; Versicolor & Virginica overlap in sepal measurements

### 2. Visualizations
- Pairplot showing feature distributions by species
- Box plots & violin plots for each feature by species
- Correlation heatmap

### 3. Model Training (80/20 stratified split)
| Model | Test Accuracy |
|-------|---------------|
| **K-Nearest Neighbors (k=3)** | **100%** |
| Logistic Regression | 96.7% |
| Decision Tree | 93.3% |
| Random Forest | 90.0% |

### 4. Best Model
**K-Nearest Neighbors (k=3)** - 100% accuracy on test set

## Files
- `iris_classification.ipynb` - Main analysis notebook
- `iris_classification_executed.ipynb` - Executed notebook with outputs
- `iris.csv` - Dataset

## Key Learnings
- Classic "hello world" classification dataset
- Petal measurements are most discriminative
- Well-separated classes make even simple models effective
- KNN excels with clear class boundaries and small datasets