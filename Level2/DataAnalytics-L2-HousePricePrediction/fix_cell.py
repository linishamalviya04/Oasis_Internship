import json

with open('house_price_prediction.ipynb', 'r') as f:
    nb = json.load(f)

# Fix the model comparison cell (cell index 19)
cell = nb['cells'][19]
source = cell['source']

# Replace the entire cell source with corrected version
new_source = [
    "# Ridge Regression with cross-validation for alpha\n",
    "from sklearn.linear_model import RidgeCV, LassoCV\n",
    "\n",
    "alphas = np.logspace(-3, 3, 50)\n",
    "\n",
    "ridge_cv = RidgeCV(alphas=alphas, cv=5)\n",
    "ridge_cv.fit(X_train_processed, y_train)\n",
    "\n",
    "lasso_cv = LassoCV(alphas=alphas, cv=5, max_iter=10000, random_state=42)\n",
    "lasso_cv.fit(X_train_processed, y_train)\n",
    "\n",
    "print('Best Ridge alpha: {:.4f}'.format(ridge_cv.alpha_))\n",
    "print('Best Lasso alpha: {:.4f}'.format(lasso_cv.alpha_))\n",
    "\n",
    "# Evaluate all three models\n",
    "models = {\n",
    "    'Linear Regression': lr,\n",
    "    'Ridge (alpha={:.4f})'.format(ridge_cv.alpha_): ridge_cv,\n",
    "    'Lasso (alpha={:.4f})'.format(lasso_cv.alpha_): lasso_cv\n",
    "}\n",
    "\n",
    "results = []\n",
    "for name, model in models.items():\n",
    "    y_pred = model.predict(X_test_processed)\n",
    "    metrics = evaluate_model(y_test, y_pred, 'Test_')\n",
    "    metrics['Model'] = name\n",
    "    results.append(metrics)\n",
    "    \n",
    "    # Count non-zero coefficients for Lasso\n",
    "    if hasattr(model, 'coef_'):\n",
    "        n_nonzero = np.sum(model.coef_ != 0)\n",
    "        print('{}: {}/{} non-zero coefficients'.format(name, n_nonzero, len(model.coef_)))\n",
    "\n",
    "results_df = pd.DataFrame(results)[['Model', 'Test_MSE', 'Test_RMSE', 'Test_MAE', 'Test_R2']]\n",
    "print('\\n=== MODEL COMPARISON ===')\n",
    "display(results_df.round(4))"
]

cell['source'] = new_source

with open('house_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)

print('Fixed cell')