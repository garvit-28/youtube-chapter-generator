# YouTube Chapter Generator

This project generates YouTube video chapters from the video’s transcript using Natural Language Processing (NLP) and Topic Modeling (NMF) techniques. The chapters are dynamically generated based on the content, with meaningful titles derived from the transcript.

## Features

- Extracts YouTube video transcript using the provided URL.
- Generates chapters using KeyBERT for keyword extraction and NMF for topic modeling.
- Chapters are dynamically created with timestamps and meaningful titles.
- Provides an easy-to-use web interface with Streamlit.
- Chapters are displayed with timestamps and titles in a user-friendly format.

## Libraries Used

- **Streamlit** for building the web interface.
- **YouTube Transcript API** for extracting video transcripts.
- **KeyBERT** for keyword extraction to create chapter titles.
- **NLTK** and **SpaCy** for text processing and natural language understanding.
- **Pandas** for managing data.

## Requirements

To run this project, you'll need Python 3.x and the required libraries. You can install them using the following command:


pip install -r requirements.txt

## Setup and Usage

1. **Clone the repository**:
   
   git clone https://github.com/garvit-28/youtube-chapter-generator.git

 
2. **Navigate to the project folder**:

   cd youtube-chapter-generator


3. **Install required dependencies**:

   pip install -r requirements.txt


4. **Run the Streamlit App**:

To start the app, run:

streamlit run app.py



Make sure your main script is named `app.py`, or adjust the command to match your script's name.

5. **Enter the YouTube URL**:

In the Streamlit app, input the YouTube URL you want to process. The transcript will be fetched, and chapters will be generated with meaningful titles and timestamps.

Example command to run the app:

streamlit run app.py

Once the app is running, input a YouTube video URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`) to generate the chapters.


## Acknowledgments

- **YouTube API** for transcript extraction.
- **KeyBERT** for keyword extraction.
- **NLTK** and **SpaCy** for NLP tasks. 
- **Streamlit** for the web interface.






   






