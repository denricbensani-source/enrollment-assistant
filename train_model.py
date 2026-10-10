import csv
import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = "data/intents.csv"
MODEL_PATH = "models/intent_model.pkl"

# Load the training dataset
with open(DATA_PATH, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

questions = [row["question"].strip() for row in rows]
intents = [row["intent"].strip() for row in rows]

# Split data into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    questions,
    intents,
    test_size=0.2,
    random_state=42,
    stratify=intents,
)

# Create a TF-IDF + Logistic Regression pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
])

# Train and evaluate the model
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")
print("\nClassification report:")
print(classification_report(y_test, predictions, zero_division=0))
print("Confusion matrix (alphabetical label order):")
print(model.named_steps["classifier"].classes_)
print(confusion_matrix(y_test, predictions, labels=model.named_steps["classifier"].classes_))
print("\nMisclassified test questions:")
for question, actual, predicted in zip(X_test, y_test, predictions):
    if actual != predicted:
        print(f"Question: {question}")
        print(f"Actual: {actual} | Predicted: {predicted}")
        print("-" * 40)

# Save the trained model
os.makedirs("models", exist_ok=True)
with open(MODEL_PATH, "wb") as file:
    pickle.dump(model, file)

print(f"\nModel saved to {MODEL_PATH}")
