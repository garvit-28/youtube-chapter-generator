import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import pickle

# Load the transcript CSV (replace with your actual file name if needed)
df = pd.read_csv("SobRqlT0pOM_transcript.csv")

# Clean and prepare
df.dropna(subset=['text'], inplace=True)

# Vectorization
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(df['text'])

# Topic Modeling
n_topics = 10
nmf_model = NMF(n_components=n_topics, random_state=42)
nmf_model.fit(tfidf)

# Save models as .pkl files
with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf_vectorizer, f)

with open("nmf_model.pkl", "wb") as f:
    pickle.dump(nmf_model, f)

print("✅ Model and vectorizer saved as .pkl files.")
