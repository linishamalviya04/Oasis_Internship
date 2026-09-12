import json

with open('house_price_prediction.ipynb', 'r') as f:
    nb = json.load(f)

# Fix the evaluate_model call in the model comparison cell
# Cell index 19 (0-indexed) - the Ridge/Lasso comparison cell
cell = nb['cells'][19]
source = cell['source']
new_source = []
for line in source:
    if 'metrics = evaluate_model(y_test, y_pred)' in line and 'Test_' not in line:
        new_source.append("    metrics = evaluate_model(y_test, y_pred, 'Test_')")
    else:
        new_source.append(line)
cell['source'] = new_source

with open('house_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)

print('Fixed')