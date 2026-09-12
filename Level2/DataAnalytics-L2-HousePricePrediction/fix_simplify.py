import json

with open('house_price_prediction.ipynb', 'r') as f:
    nb = json.load(f)

# Simplify the Ridge/Lasso cell (index 20) to use fewer alphas and cv folds for speed
# Also make the coefficient comparison cell (index 21) handle missing ridge/lasso gracefully
new_cell_20 = [
    '# Ridge Regression with cross-validation for alpha',
    'from sklearn.linear_model import RidgeCV, LassoCV',
    '',
    '# Use fewer alphas and cv folds for faster execution',
    'alphas = np.logspace(-3, 3, 20)',
    '',
    'ridge_cv = RidgeCV(alphas=alphas, cv=3)',
    'ridge_cv.fit(X_train_processed, y_train)',
    '',
    'lasso_cv = LassoCV(alphas=alphas, cv=3, max_iter=5000, random_state=42)',
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

# Fix cell 21 to handle missing ridge/lasso
new_cell_21 = [
    '# Compare coefficients across models',
    'try:',
    '    coeff_comparison = pd.DataFrame({',
    "    'Feature': feature_names,",
    "    'Linear': lr.coef_,",
    "    'Ridge': ridge_cv.coef_,",
    "    'Lasso': lasso_cv.coef_",
    '})',
    '',
    '    # Plot comparison for top features',
    '    top_feats = coeff_comparison.set_index(\'Feature\').abs().sum(axis=1).nlargest(15).index',
    '    plot_data = coeff_comparison[coeff_comparison[\'Feature\'].isin(top_feats)].set_index(\'Feature\')',
    '',
    '    fig, axes = plt.subplots(1, 3, figsize=(18, 8))',
    "    for i, (name, col) in enumerate([('Linear', 'Linear'), ('Ridge', 'Ridge'), ('Lasso', 'Lasso')]):",
    "        colors = ['green' if c > 0 else 'red' for c in plot_data[col]]",
    '        axes[i].barh(range(len(plot_data)), plot_data[col], color=colors, alpha=0.7)',
    '        axes[i].set_yticks(range(len(plot_data)))',
    '        axes[i].set_yticklabels(plot_data.index)',
    '        axes[i].set_xlabel(\'Coefficient\')',
    "        axes[i].set_title('{} Coefficients'.format(name), fontweight='bold')",
    '        axes[i].axvline(x=0, color=\'black\', linewidth=0.5)',
    '        axes[i].grid(True, alpha=0.3)',
    '',
    '    plt.tight_layout()',
    '    plt.show()',
    '',
    "    print('=== COEFFICIENT COMPARISON (Top 15 by combined magnitude) ===')",
    '    display(plot_data.round(4))',
    'except NameError:',
    "    print('Ridge/Lasso models not available for comparison')"
]

nb['cells'][20]['source'] = new_cell_20
nb['cells'][21]['source'] = new_cell_21

with open('house_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Fixed - simplified alphas and added error handling')