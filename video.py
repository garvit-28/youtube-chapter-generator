import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from keybert import KeyBERT
from datetime import timedelta
import re
import nltk
import spacy
import pandas as pd
import os

# ✅ MUST be first Streamlit command
st.set_page_config(page_title="YouTube Chapter Generator", page_icon="🎬")

# Download NLTK resources
nltk.download('punkt')

import subprocess

# Ensure the spaCy model is downloaded
def download_spacy_model():
    subprocess.call([ "python", "-m", "spacy", "download", "en_core_web_sm"])

try:
    # Try to load the model
    nlp = spacy.load("en_core_web_sm")
except IOError:
    # If model loading fails, download the model
    download_spacy_model()
    nlp = spacy.load("en_core_web_sm")


# Cache KeyBERT model
@st.cache_resource
def load_kw_model():
    return KeyBERT(model="all-MiniLM-L6-v2")

kw_model = load_kw_model()

# Extract video ID from YouTube URL
def extract_video_id(url):
    video_id_match = re.search(r"(?:v=|youtu.be/)([\w-]{11})", url)
    return video_id_match.group(1) if video_id_match else None

# Fetch transcript using YouTubeTranscriptApi
def fetch_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

# Convert seconds to HH:MM:SS
def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))

# Break transcript into chunks (default: 60s)
def chunk_transcript(transcript, chunk_duration=60):
    chunks = []
    current_chunk = []
    current_time = 0
    for entry in transcript:
        start = entry['start']
        if start - current_time >= chunk_duration:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = [entry]
            current_time = start
        else:
            current_chunk.append(entry)
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

# Get top keyword using KeyBERT
def generate_keywords(text):
    keywords = kw_model.extract_keywords(
        text, 
        keyphrase_ngram_range=(1, 3), 
        stop_words='english', 
        top_n=1
    )
    return keywords[0][0] if keywords else "Untitled"

# Generate chapters with timestamp + keyword
def generate_chapters(transcript):
    chunks = chunk_transcript(transcript)
    chapters = []
    used_titles = {}
    
    for chunk in chunks:
        combined_text = " ".join([entry['text'] for entry in chunk])
        start_time = format_time(chunk[0]['start'])
        keyword = generate_keywords(combined_text).title()  # Capitalize each word
        
        # Ensure uniqueness
        if keyword in used_titles:
            used_titles[keyword] += 1
            keyword = f"{keyword} ({used_titles[keyword]})"
        else:
            used_titles[keyword] = 1

        chapters.append((start_time, keyword))
    
    return chapters


# Streamlit UI
def main():
    st.title("🎬 YouTube Chapter Generator")
    st.write("Enter a YouTube video URL to generate keyword-rich chapters like YouTube timestamps!")

    video_url = st.text_input("Enter YouTube Video URL", value="")
    generate_button = st.button("Generate Chapters")

    if generate_button and video_url:
        with st.spinner('⏳ Fetching transcript and generating chapters...'):
            try:
                video_id = extract_video_id(video_url)
                if not video_id:
                    st.error("❌ Invalid YouTube URL.")
                    return

                transcript = fetch_transcript(video_id)
                if not transcript:
                    st.warning("⚠️ No transcript available for this video.")
                    return

                chapters = generate_chapters(transcript)

                st.subheader("📍 Chapters")
                for idx, (time, title) in enumerate(chapters, 1):
                    st.markdown(f"**{time} — Chapter {idx}: {title}**")

            except Exception as e:
                st.error(f"🚨 Error: {str(e)}")

if __name__ == "__main__":
    main()



