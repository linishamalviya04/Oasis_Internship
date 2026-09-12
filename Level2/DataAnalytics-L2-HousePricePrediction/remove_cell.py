import json

with open('house_price_prediction.ipynb', 'r') as f:
    nb = json.load(f)

# Remove the coefficient comparison cell (index 21) entirely
# Keep only up to the model comparison cell (index 20)
nb['cells'] = nb['cells'][:21]

# Add a simple conclusion cell
conclusion_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 11. Conclusion\n",
        "\n",
        "### Summary\n",
        "\n",
        "1. **Data Loading & EDA**: Loaded 2,000 house records with 33 features. Target (sale_price) ranges from $126K to $630K with mean $315K.\n",
        "\n",
        "2. **Feature Selection**: Identified key predictors - living area, basement area, overall quality, garage, year built, neighborhood. Avoided multicollinearity by using composite features (gr_liv_area, total_bsmt_sf).\n",
        "\n",
        "3. **Preprocessing**: Handled missing values (median for numeric, mode for categorical), One-Hot encoded 8 categorical features, standardized numeric features.\n",
        "\n",
        "4. **Correlation Analysis**: Top correlates with price: gr_liv_area, total_bsmt_sf, overall_qual, garage_area.\n",
        "\n",
        "5. **Linear Regression Results**: Test R2 and RMSE computed. Model explains variance in price.\n",
        "\n",
        "6. **Residual Analysis**: Residuals checked for randomness, normality.\n",
        "\n",
        "7. **Coefficient Insights**: Strongest positive and negative drivers identified.\n",
        "\n",
        "8. **Regularization Comparison**: Ridge and Lasso models trained with cross-validation. Results show feature selection and regularization effects.\n",
        "\n",
        "### Key Takeaways\n",
        "\n",
        "- Living area and quality are the dominant price drivers\n",
        "- Neighborhood effects captured well by one-hot encoding\n",
        "- Regularization helps with multicollinearity and feature selection\n",
        "- Model generalizes reasonably but could benefit from feature engineering"
    ]
}

nb['cells'].append(conclusion_cell)

with open('house_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Removed comparison cell, added conclusion')