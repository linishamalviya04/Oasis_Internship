import json

with open('spam_detection.ipynb', 'r') as f:
    nb = json.load(f)

# Fix the TF-IDF cell (cell index 5)
cell = nb['cells'][5]
source = cell['source']
new_source = [
    "# TF-IDF Vectorization\n",
    "tfidf = TfidfVectorizer(\n",
    "    max_features=5000,\n",
    "    ngram_range=(1, 2),\n",
    "    min_df=2,\n",
    "    max_df=0.95\n",
    ")\n",
    "\n",
    "X = tfidf.fit_transform(df['processed_message'])\n",
    "y = df['label'].map({'ham': 0, 'spam': 1})\n",
    "\n",
    "print(f'TF-IDF Matrix Shape: {X.shape}')\n",
    "print(f'Vocabulary Size: {len(tfidf.vocabulary_)}')\n",
    "\n",
    "# Show top TF-IDF features for spam vs ham\n",
    "feature_names = tfidf.get_feature_names_out()\n",
    "\n",
    "# Get average TF-IDF per class\n",
    "spam_mask = (y == 1).values\n",
    "ham_mask = (y == 0).values\n",
    "\n",
    "spam_tfidf = X[spam_mask].mean(axis=0).A1\n",
    "ham_tfidf = X[ham_mask].mean(axis=0).A1\n",
    "\n",
    "tfidf_df = pd.DataFrame({\n",
    "    'feature': tfidf.get_feature_names_out(),\n",
    "    'spam_avg': spam_tfidf,\n",
    "    'ham_avg': ham_tfidf\n",
    "})\n",
    "tfidf_df['spam_ham_ratio'] = tfidf_df['spam_avg'] / (tfidf_df['ham_avg'] + 1e-10)\n",
    "\n",
    "print('\\n=== TOP SPAM INDICATORS (highest spam/ham ratio) ===')\n",
    "top_spam = tfidf_df.nlargest(15, 'spam_ham_ratio')\n",
    "display(top_spam[['feature', 'spam_avg', 'ham_avg', 'spam_ham_ratio']].round(4))\n",
    "\n",
    "print('\\n=== TOP HAM INDICATORS (lowest spam/ham ratio) ===')\n",
    "top_ham = tfidf_df.nsmallest(15, 'spam_ham_ratio')\n",
    "display(top_ham[['feature', 'spam_avg', 'ham_avg', 'spam_ham_ratio']].round(4))"
]
cell['source'] = new_source

with open('spam_detection.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Fixed TF-IDF cell')