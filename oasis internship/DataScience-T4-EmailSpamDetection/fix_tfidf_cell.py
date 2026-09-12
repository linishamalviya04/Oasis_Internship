import json

with open('spam_detection.ipynb', 'r') as f:
    nb = json.load(f)

# Fix the TF-IDF cell (cell index 5) - replace the entire cell source
new_source = [
    '# TF-IDF Vectorization',
    'tfidf = TfidfVectorizer(',
    '    max_features=5000,',
    '    ngram_range=(1, 2),',
    '    min_df=2,',
    '    max_df=0.95',
    ')',
    '',
    'X = tfidf.fit_transform(df["processed_message"])',
    'y = df["label"].map({"ham": 0, "spam": 1})',
    '',
    'print("TF-IDF Matrix Shape: {0}".format(X.shape))',
    'print("Vocabulary Size: {0}".format(len(tfidf.vocabulary_)))',
    '',
    '# Show top TF-IDF features for spam vs ham',
    'feature_names = tfidf.get_feature_names_out()',
    '',
    '# Get average TF-IDF per class - use numpy array for indexing',
    'import numpy as np',
    'spam_mask = np.array(y == 1)',
    'ham_mask = np.array(y == 0)',
    '',
    'spam_tfidf = X[spam_mask].mean(axis=0).A1',
    'ham_tfidf = X[ham_mask].mean(axis=0).A1',
    '',
    'tfidf_df = pd.DataFrame({',
    '    "feature": tfidf.get_feature_names_out(),',
    '    "spam_avg": spam_tfidf,',
    '    "ham_avg": ham_tfidf',
    '})',
    'tfidf_df["spam_ham_ratio"] = tfidf_df["spam_avg"] / (tfidf_df["ham_avg"] + 1e-10)',
    '',
    'print("\\n=== TOP SPAM INDICATORS (highest spam/ham ratio) ===")',
    'top_spam = tfidf_df.nlargest(15, "spam_ham_ratio")',
    'display(top_spam[["feature", "spam_avg", "ham_avg", "spam_ham_ratio"]].round(4))',
    '',
    'print("\\n=== TOP HAM INDICATORS (lowest spam/ham ratio) ===")',
    'top_ham = tfidf_df.nsmallest(15, "spam_ham_ratio")',
    'display(top_ham[["feature", "spam_avg", "ham_avg", "spam_ham_ratio"]].round(4))'
]

nb['cells'][5]['source'] = new_source

with open('spam_detection.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Fixed TF-IDF cell completely')