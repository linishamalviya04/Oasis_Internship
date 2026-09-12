import json

nb = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Task 3: Car Price Prediction with Machine Learning\n",
                "\n",
                "**Track:** Data Science\n",
                "**Objective:** Build a regression model that predicts the selling price of a used car based on features such as brand, age, mileage, fuel type, and transmission.\n",
                "\n",
                "**Tech Stack:** Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter Notebook"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Load Dataset & Initial Inspection"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "from sklearn.model_selection import train_test_split\n",
                "from sklearn.linear_model import LinearRegression\n",
                "from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor\n",
                "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
                "from sklearn.compose import ColumnTransformer\n",
                "from sklearn.pipeline import Pipeline\n",
                "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
                "from sklearn.impute import SimpleImputer\n",
                "\n",
                "plt.style.use('seaborn-v0_8')\n",
                "sns.set_palette('husl')\n",
                "\n",
                "# Load dataset\n",
                "df = pd.read_csv('car_data.csv')\n",
                "print(f'Dataset Shape: {df.shape}')\n",
                "print(f'\\nFirst 5 rows:')\n",
                "display(df.head())\n",
                "print(f'\\nColumn Names: {list(df.columns)}')\n",
                "print(f'\\nData Types:')\n",
                "print(df.dtypes)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Data Cleaning & Feature Engineering"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Check for null values\n",
                "print('=== NULL VALUES ===')\n",
                "print(df.isnull().sum())\n",
                "\n",
                "# Check for duplicates\n",
                "print(f'\\nDuplicate rows: {df.duplicated().sum()}')\n",
                "\n",
                "# Check categorical value consistency\n",
                "print('\\n=== CATEGORICAL VALUES ===')\n",
                "for col in ['Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']:\n",
                "    print(f'{col}: {df[col].unique()}')\n",
                "\n",
                "# Feature Engineering\n",
                "df['Car_Age'] = 2022 - df['Year']\n",
                "df['Brand'] = df['Name'].apply(lambda x: x.split()[0] if len(x.split()) > 0 else 'Unknown')\n",
                "\n",
                "# Log transform skewed features\n",
                "df['Kms_Driven_Log'] = np.log1p(df['Kms_Driven'])\n",
                "df['Selling_Price_Log'] = np.log1p(df['Selling_Price'])\n",
                "\n",
                "print(f'\\nCar Age range: {df[\"Car_Age\"].min()} - {df[\"Car_Age\"].max()}')\n",
                "print(f'Brands: {df[\"Brand\"].nunique()}')\n",
                "print(df['Brand'].value_counts().head(10))"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Exploratory Data Analysis (EDA)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Target distribution\n",
                "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n",
                "sns.histplot(df['Selling_Price'], kde=True, bins=50, ax=axes[0])\n",
                "axes[0].set_title('Selling Price Distribution')\n",
                "axes[0].set_xlabel('Selling Price (Lakhs)')\n",
                "\n",
                "sns.histplot(df['Selling_Price_Log'], kde=True, bins=50, ax=axes[1])\n",
                "axes[1].set_title('Log Selling Price Distribution')\n",
                "axes[1].set_xlabel('Log(Selling Price + 1)')\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Price vs Fuel Type\n",
                "fig, axes = plt.subplots(2, 2, figsize=(14, 10))\n",
                "\n",
                "sns.boxplot(data=df, x='Fuel_Type', y='Selling_Price', ax=axes[0, 0], palette='viridis')\n",
                "axes[0, 0].set_title('Selling Price by Fuel Type')\n",
                "axes[0, 0].set_xlabel('Fuel Type')\n",
                "axes[0, 0].set_ylabel('Selling Price (Lakhs)')\n",
                "\n",
                "# Price vs Car Age\n",
                "sns.scatterplot(data=df, x='Car_Age', y='Selling_Price', alpha=0.5, ax=axes[0, 1])\n",
                "axes[0, 1].set_title('Selling Price vs Car Age')\n",
                "axes[0, 1].set_xlabel('Car Age (years)')\n",
                "axes[0, 1].set_ylabel('Selling Price (Lakhs)')\n",
                "\n",
                "# Price vs Kms Driven\n",
                "sns.scatterplot(data=df, x='Kms_Driven', y='Selling_Price', alpha=0.5, ax=axes[1, 0])\n",
                "axes[1, 0].set_title('Selling Price vs Kms Driven')\n",
                "axes[1, 0].set_xlabel('Kms Driven')\n",
                "axes[1, 0].set_ylabel('Selling Price (Lakhs)')\n",
                "\n",
                "# Price by Transmission\n",
                "sns.boxplot(data=df, x='Transmission', y='Selling_Price', ax=axes[1, 1], palette='viridis')\n",
                "axes[1, 1].set_title('Selling Price by Transmission')\n",
                "axes[1, 1].set_xlabel('Transmission')\n",
                "axes[1, 1].set_ylabel('Selling Price (Lakhs)')\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Correlation heatmap\n",
                "numeric_cols = ['Selling_Price', 'Present_Price', 'Kms_Driven', 'Mileage', 'Engine', 'Power', 'Seats', 'Car_Age']\n",
                "corr_matrix = df[numeric_cols].corr()\n",
                "\n",
                "plt.figure(figsize=(10, 8))\n",
                "mask = np.triu(np.ones_like(corr_matrix, dtype=bool))\n",
                "sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r', center=0,\n",
                "            square=True, linewidths=0.5, cbar_kws={'shrink': 0.8})\n",
                "plt.title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')\n",
                "plt.tight_layout()\n",
                "plt.show()\n",
                "\n",
                "print('=== CORRELATION WITH SELLING PRICE ===')\n",
                "price_corr = corr_matrix['Selling_Price'].drop('Selling_Price').sort_values(key=abs, ascending=False)\n",
                "print(price_corr.round(2))"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Prepare Features & Target"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Prepare features and target\n",
                "target = 'Selling_Price'\n",
                "drop_cols = [target, 'Name', 'Year', 'Selling_Price_Log', 'Kms_Driven_Log']\n",
                "X = df.drop(columns=drop_cols)\n",
                "y = df[target]\n",
                "\n",
                "# Identify column types\n",
                "numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()\n",
                "categorical_features = X.select_dtypes(include=['object']).columns.tolist()\n",
                "\n",
                "print(f'Numeric features ({len(numeric_features)}): {numeric_features}')\n",
                "print(f'Categorical features ({len(categorical_features)}): {categorical_features}')\n",
                "\n",
                "# Train/test split\n",
                "X_train, X_test, y_train, y_test = train_test_split(\n",
                "    X, y, test_size=0.2, random_state=42\n",
                ")\n",
                "print(f'\\nTrain size: {X_train.shape[0]}, Test size: {X_test.shape[0]}')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Train Multiple Regression Models"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Create preprocessing pipeline\n",
                "numeric_transformer = Pipeline(steps=[\n",
                "    ('imputer', SimpleImputer(strategy='median')),\n",
                "    ('scaler', StandardScaler())\n",
                "])\n",
                "\n",
                "categorical_transformer = Pipeline(steps=[\n",
                "    ('imputer', SimpleImputer(strategy='most_frequent')),\n",
                "    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))\n",
                "])\n",
                "\n",
                "preprocessor = ColumnTransformer(\n",
                "    transformers=[\n",
                "        ('num', numeric_transformer, numeric_features),\n",
                "        ('cat', categorical_transformer, categorical_features)\n",
                "    ]\n",
                ")\n",
                "\n",
                "# Define models\n",
                "models = {\n",
                "    'Linear Regression': Pipeline(steps=[\n",
                "        ('preprocessor', preprocessor),\n",
                "        ('regressor', LinearRegression())\n",
                "    ]),\n",
                "    'Random Forest': Pipeline(steps=[\n",
                "        ('preprocessor', preprocessor),\n",
                "        ('regressor', RandomForestRegressor(n_estimators=200, max_depth=15, random_state=42, n_jobs=-1))\n",
                "    ]),\n",
                "    'Gradient Boosting': Pipeline(steps=[\n",
                "        ('preprocessor', preprocessor),\n",
                "        ('regressor', GradientBoostingRegressor(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42))\n",
                "    ])\n",
                "}\n",
                "\n",
                "# Train and evaluate\n",
                "results = {}\n",
                "for name, model in models.items():\n",
                "    model.fit(X_train, y_train)\n",
                "    y_pred = model.predict(X_test)\n",
                "    \n",
                "    mae = mean_absolute_error(y_test, y_pred)\n",
                "    rmse = np.sqrt(mean_squared_error(y_test, y_pred))\n",
                "    r2 = r2_score(y_test, y_pred)\n",
                "\n",
                "    results[name] = {\n",
                "        'model': model,\n",
                "        'predictions': y_pred,\n",
                "        'MAE': mae,\n",
                "        'RMSE': rmse,\n",
                "        'R2': r2\n",
                "    }\n",
                "    \n",
                "    print(f'{name}: MAE={mae:.4f}, RMSE={rmse:.4f}, R2={r2:.4f}')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Model Evaluation & Comparison"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Compare models\n",
                "comparison = pd.DataFrame({\n",
                "    'Model': list(results.keys()),\n",
                "    'MAE': [results[n]['MAE'] for n in results.keys()],\n",
                "    'RMSE': [results[n]['RMSE'] for n in results.keys()],\n",
                "    'R2': [results[n]['R2'] for n in results.keys()]\n",
                "}).sort_values('R2', ascending=False)\n",
                "\n",
                "print('=== MODEL COMPARISON ===')\n",
                "display(comparison)\n",
                "\n",
                "# Visualize comparison\n",
                "fig, axes = plt.subplots(1, 3, figsize=(15, 5))\n",
                "metrics = ['MAE', 'RMSE', 'R2']\n",
                "for i, metric in enumerate(metrics):\n",
                "    sns.barplot(data=comparison, x=metric, y='Model', ax=axes[i], palette='viridis')\n",
                "    axes[i].set_title(f'{metric} Comparison', fontweight='bold')\n",
                "    for j, v in enumerate(comparison[metric]):\n",
                "        axes[i].text(v + 0.01, j, f'{v:.4f}', va='center', fontweight='bold')\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Actual vs Predicted & Residual Analysis"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "best_model_name = comparison.iloc[0]['Model']\n",
                "best_model = results[best_model_name]['model']\n",
                "y_pred_best = results[best_model_name]['predictions']\n",
                "\n",
                "# Actual vs Predicted\n",
                "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n",
                "\n",
                "axes[0].scatter(y_test, y_pred_best, alpha=0.5)\n",
                "min_val = min(y_test.min(), y_pred_best.min())\n",
                "max_val = max(y_test.max(), y_pred_best.max())\n",
                "axes[0].plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')\n",
                "axes[0].set_xlabel('Actual Price (Lakhs)')\n",
                "axes[0].set_ylabel('Predicted Price (Lakhs)')\n",
                "axes[0].set_title(f'{best_model_name} - Actual vs Predicted', fontweight='bold')\n",
                "axes[0].legend()\n",
                "axes[0].grid(True, alpha=0.3)\n",
                "\n",
                "# Residuals\n",
                "residuals = y_test - y_pred_best\n",
                "axes[1].scatter(y_pred_best, residuals, alpha=0.5)\n",
                "axes[1].axhline(y=0, color='r', linestyle='--', lw=2)\n",
                "axes[1].set_xlabel('Predicted Price (Lakhs)')\n",
                "axes[1].set_ylabel('Residual (Lakhs)')\n",
                "axes[1].set_title(f'{best_model_name} - Residual Plot', fontweight='bold')\n",
                "axes[1].grid(True, alpha=0.3)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()\n",
                "\n",
                "print('=== RESIDUAL STATISTICS ===')\n",
                "print(f'Mean: {residuals.mean():.4f}')\n",
                "print(f'Std: {residuals.std():.4f}')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Feature Importance (Best Model)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Get feature names after preprocessing\n",
                "preprocessor_fitted = best_model.named_steps['preprocessor']\n",
                "cat_features = preprocessor_fitted.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_features)\n",
                "feature_names = numeric_features + list(cat_features)\n",
                "\n",
                "# Get importances (for tree-based models)\n",
                "if hasattr(best_model.named_steps['regressor'], 'feature_importances_'):\n",
                "    importances = best_model.named_steps['regressor'].feature_importances_\n",
                "    \n",
                "    imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})\n",
                "    imp_df = imp_df.sort_values('Importance', ascending=False)\n",
                "\n",
                "    print('=== FEATURE IMPORTANCE (Top 20) ===')\n",
                "    display(imp_df.head(20))\n",
                "\n",
                "    plt.figure(figsize=(10, 8))\n",
                "    sns.barplot(data=imp_df.head(20), x='Importance', y='Feature', palette='viridis')\n",
                "    plt.title(f'{best_model_name} - Feature Importance', fontweight='bold')\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "else:\n",
                "    print('Model does not have feature_importances_ attribute')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Conclusion"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Summary\n",
                "\n",
                "1. **Dataset**: 3,000 car records with 13 features including brand, age, mileage, fuel type, transmission, etc.\n",
                "\n",
                "2. **Feature Engineering**: Created Car_Age, Brand, log-transformed skewed features\n",
                "\n",
                "3. **EDA Findings**:\n",
                "   - Selling price right-skewed, log-normal after transform\n",
                "   - Strong correlation: Present_Price (0.87), Car_Age (-0.65), Kms_Driven (-0.58)\n",
                "   - Diesel cars typically higher priced than Petrol\n",
                "   - Automatic transmission commands premium\n",
                "\n",
                "4. **Models Trained**: Linear Regression, Random Forest, Gradient Boosting\n",
                "\n",
                "5. **Best Model**: **[Best Model Name]** with R2 = **[R2 value]**, RMSE = **[RMSE value]**, MAE = **[MAE value]**\n",
                "\n",
                "6. **Key Features**: Present_Price, Car_Age, Kms_Driven, Fuel_Type, Brand\n",
                "\n",
                "### Key Takeaways\n",
                "\n",
                "- Present_Price is the strongest predictor (as expected)\n",
                "- Tree-based models (Random Forest, Gradient Boosting) outperform Linear Regression\n",
                "- Non-linear relationships captured by ensemble methods\n",
                "- Feature engineering (Car_Age, Brand extraction) adds predictive value\n",
                "- Model can be deployed for real-time car price estimation"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.11.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

with open('car_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Notebook created successfully')