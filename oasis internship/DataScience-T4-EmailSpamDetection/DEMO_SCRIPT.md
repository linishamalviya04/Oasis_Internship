# Demo Video Script - Task 4: Email Spam Detection

**Duration Target:** 4-5 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Science | Task 4: Email Spam Detection | [Your Name]"

---

## SCENE 1: Introduction (20 seconds)
**Visual:** Show repo, open `spam_detection.ipynb`
**Script:**
> "Hi, I'm [Your Name] presenting Task 4: Email Spam Detection. I build an NLP classifier to distinguish spam from legitimate emails using TF-IDF and three classifiers."

---

## SCENE 2: Dataset & Preprocessing (30 seconds)
**Visual:** Cells 1-2: dataset overview, preprocessing pipeline
**Script:**
> "The dataset has 5,000 SMS messages: 3,000 ham, 2,000 spam (40% spam). Preprocessing: lowercase, remove punctuation, remove stopwords, stemming. This reduces noise and focuses on meaningful words."

---

## SCENE 3: TF-IDF Feature Extraction (45 seconds)
**Visual:** Cell 3: TF-IDF explanation, top spam/ham indicators
**Script:**
> "TF-IDF vectorization with n-grams (1,2) captures phrases like 'click here', 'free money'. Top spam indicators: win, free, prize, click, claim, urgent, cash. Ham indicators: meeting, thanks, please, tomorrow. These perfectly separate the classes."

---

## SCENE 4: Model Training & Results (45 seconds)
**Visual:** Cells 5-7: three models, classification reports, confusion matrices
**Script:**
> "Three classifiers: Multinomial Naive Bayes (industry standard), Logistic Regression, SVM. All three achieve perfect 1.0 precision, recall, and F1-score! The synthetic dataset is perfectly separable. Naive Bayes is industry standard for text classification."

---

## SCENE 6: Why Recall Matters (30 seconds)
**Visual:** Cell 8: Recall vs Precision explanation markdown
**Script:**
> "Key insight: Recall > Precision for spam detection. Missing spam (false negative) = phishing risk, malware. False alarm = user checks spam folder. Cost asymmetry favors high recall. F1-score balances both."

---

## SCENE 7: Conclusion (15 seconds)
**Visual:** Conclusion markdown, GitHub repo
**Script:**
> "All three models achieve perfect 1.0 F1-score. Naive Bayes is industry standard for text classification. TF-IDF + Naive Bayes works excellently for spam filtering. Thank you!
> 
> #oasisinfobyte #datascience #spamdetection #nlp #tfidf #naivebayes"

---

## Recording Tips
- Show confusion matrices - they're all perfect (diagonal only)
- Emphasize the TF-IDF top features - very intuitive
- Explain the recall vs precision tradeoff clearly - shows deep understanding