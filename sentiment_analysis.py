import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Amazon reviews
print("Loading dataset...")

df = pd.read_csv(
    "dataset/raw/1429_1.csv",
    usecols=["reviews.text", "reviews.rating"],
    low_memory=False
)

# Step 2: Clean data
df = df.dropna(subset=["reviews.text", "reviews.rating"])

df["reviews.rating"] = pd.to_numeric(
    df["reviews.rating"], errors="coerce"
)

df = df.dropna(subset=["reviews.rating"])

# Step 3: Convert ratings into sentiment labels
def get_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating <= 2:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["reviews.rating"].apply(get_sentiment)

# Remove neutral reviews
df = df[df["sentiment"] != "Neutral"]

print("Total reviews:", len(df))

# Step 4: Prepare input and output
X = df["reviews.text"].astype(str)
y = df["sentiment"]

# Step 5: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Step 6: Convert text into TF-IDF features
vectorizer = TfidfVectorizer(
    max_features=20000,
    stop_words="english",
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Step 7: Train three ML models
models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Linear SVM": LinearSVC()
}

best_accuracy = 0
best_model = None
best_name = ""

for name, model in models.items():

    print("\nTraining:", name)

    model.fit(X_train_tfidf, y_train)

    predictions = model.predict(X_test_tfidf)

    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", round(accuracy * 100, 2), "%")

    print(classification_report(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_name = name

# Step 8: Save the best model
joblib.dump(best_model, "best_sentiment_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("\nBest Model:", best_name)
print("Best Accuracy:", round(best_accuracy * 100, 2), "%")

print("\nSentiment analysis completed successfully!")
