import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv("Reviews.csv")

df = df[["Text", "Score"]]
df["Sentiment"] = df["Score"].apply(lambda x: 1 if x >= 4 else 0)
df = df.dropna()

df = df.sample(20000, random_state=42)

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

df["Clean_Text"] = df["Text"].apply(clean_text)

# TF-IDF
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
X = tfidf.fit_transform(df["Clean_Text"])
y = df["Sentiment"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Word Cloud
text_data = " ".join(df[df["Sentiment"] == 1]["Clean_Text"])

wc = WordCloud(width=800, height=400, background_color="white").generate(text_data)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Positive Reviews Word Cloud")
plt.show()