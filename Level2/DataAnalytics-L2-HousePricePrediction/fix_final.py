import json

with open('house_price_prediction.ipynb', 'r') as f:
    nb = json.load(f)

# Fix cell index 20 (the Ridge/Lasso cell) 
cell = nb['cells'][20]
source = cell['source']
new_source = []
for line in source:
    if line.strip() == "metrics = evaluate_model(y_test, y_pred)":
        new_source.append("    metrics = evaluate_model(y_test, y_pred, 'Test_')")
    else:
        new_source.append(line)
cell['source'] = new_source

with open('house_price_prediction.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Fixed')