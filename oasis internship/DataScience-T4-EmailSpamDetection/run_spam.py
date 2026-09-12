import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

df = pd.read_csv('spam_data.csv')
print('Dataset Shape:', df.shape)

# Preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    return ' '.join(tokens)

df['processed_message'] = df['message'].apply(preprocess_text)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2), min_df=2, max_df=0.95)
X = tfidf.fit_transform(df['processed_message'])
y = df['label'].map({'ham': 0, 'spam': 1})

print('TF-IDF Matrix Shape:', X.shape)
print('Vocabulary Size:', len(tfidf.vocabulary_))

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Models
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

models = {
    'Multinomial Naive Bayes': MultinomialNB(alpha=0.1),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'),
    'SVM (Linear)': SVC(kernel='linear', random_state=42, class_weight='balanced', probability=True)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    results[name] = {'predictions': y_pred, 'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1}
    print(name + ': Acc=' + format(acc, '.4f') + ', Prec=' + format(prec, '.4f') + ', Rec=' + format(rec, '.4f') + ', F1=' + format(f1, '.4f'))

# Best model
best_name = max(results, key=lambda k: results[k]['f1'])
best_result = results[best_name]
print()
print('BEST MODEL: ' + best_name + ' with F1=' + format(best_result['f1'], '.4f'))