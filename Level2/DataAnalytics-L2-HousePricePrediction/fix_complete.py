import json

with open('house_price_prediction.ipynb', 'r') as f:
    nb = json.load(f)

# Replace the entire problematic cell (index 20) with correct source
new_cell_source = [
    '# Ridge Regression with cross-validation for alpha',
    'from sklearn.linear_model import RidgeCV, LassoCV',
    '',
    'alphas = np.logspace(-3, 3, 50)',
    '',
    'ridge_cv = RidgeCV(alphas=alphas, cv=5)',
    'ridge_cv.fit(X_train_processed, y_train)',
    '',
    'lasso_cv = LassoCV(alphas=alphas, cv=5, max_iter=10000, random_state=42)',
    'lasso_cv.fit(X_train_processed, y_train)',
    '',
    "print('Best Ridge alpha: {:.4f}'.format(ridge_cv.alpha_))",
    "print('Best Lasso alpha: {:.4f}'.format(lasso_cv.alpha_))",
    '',
    '# Evaluate all three models',
    'models = {',
    "    'Linear Regression': lr,",
    "    'Ridge (alpha={:.4f})'.format(ridge_cv.alpha_): ridge_cv,",
    "    'Lasso (alpha={:.4f})'.format(lasso_cv.alpha_): lasso_cv",
    '}',
    '',
    'results = []',
    'for name, model in models.items():',
    "    y_pred = model.predict(X_test_processed)",
    "    metrics = evaluate_model(y_test, y_pred, 'Test_')",
    "    metrics['Model'] = name",
    '    results.append(metrics)',
    '    ',
    '    # Count non-zero coefficients for Lasso',
    "    if hasattr(model, 'coef_'):",
    "        n_nonzero = np.sum(model.coef_ != 0)",
    "        print('{}: {}/{} non-zero coefficients'.format(name, n_nonzero, len(model.coef_)))",
    '',
    "results_df = pd.DataFrame(results)[['Model', 'Test_MSE', 'Test_RMSE', 'Test_MAE', 'Test_R2']]",
    "print('\\n=== MODEL COMPARISON ===')",
    'display(results_df.round(4))'
]

nb['cells'][20]['source'] = new_cell_source

with open('house_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Fixed completely')