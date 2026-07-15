# 🎥 YouTube Playlist Semantic Search

DEPLOYED LINK - https://forgetrack-w6.onrender.com/

A Flask-based web application that lets users search a YouTube playlist using **natural language** instead of exact keywords.

The application fetches video metadata using the **YouTube Data API v3**, converts the metadata into **vector embeddings** using the **Google Gemini Embedding API**, stores them in a **FAISS vector database**, and returns the most relevant videos based on semantic similarity.

---

## ✨ Features

- Search any public YouTube playlist using natural language.
- Fetches all videos from a playlist.
- Extracts video metadata:
  - Title
  - Description
  - Channel
  - Publish Date
  - Thumbnail
  - Video URL
- Generates embeddings using Gemini.
- Stores vectors in a FAISS index.
- Returns the Top 5 most relevant videos.
- Simple HTML frontend with a Flask backend.

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask

**APIs**
- YouTube Data API v3
- Google Gemini Embedding API

**Libraries**
- FAISS
- NumPy
- python-dotenv
- pickle

**Frontend**
- HTML
- CSS

---

## 📂 Project Structure

```
YouTube-Playlist-Search/
│
├── app.py
├── templates/
│   └── index.html
├── vector_db/
│   ├── youtube.index
│   └── metadata.pkl
├── .env
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 📦 Installation

```bash
pip install flask
pip install python-dotenv
pip install google-api-python-client
pip install google-genai
pip install faiss-cpu
pip install numpy
```

---

## ▶️ Running the Project

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 🔍 How It Works

1. Enter a public YouTube playlist URL.
2. The application fetches all video metadata using the YouTube Data API v3.
3. Metadata (title, description, and channel) is converted into **768-dimensional embeddings** using Gemini.
4. The embeddings are stored in a FAISS vector database.
5. A user query is also converted into an embedding.
6. FAISS finds the most similar vectors and returns the most relevant videos.

---

## 💡 Example Queries

- Machine Learning Basics
- Neural Networks
- Python Projects
- heart.csv project
- Linear Regression

---

## ⚠️ Current Limitations

- Supports public playlists only.
- Uses video metadata for embeddings (not transcripts or comments).
- Rebuilds the FAISS index for every new playlist.

---

## 🚀 Future Improvements

- Transcript support
- Multiple playlist indexing
- Similarity score display
- Better UI
- Deployment support

---

## 📚 Concepts Used

- Flask
- REST APIs
- Vector Embeddings
- Semantic Search
- FAISS
- NumPy
- Environment Variables
- Pickle Serialization

---

## 🙌 Acknowledgements

- Google Gemini API
- YouTube Data API v3
- FAISS by Meta
- Flask
