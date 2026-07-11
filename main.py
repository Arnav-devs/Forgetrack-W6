from dotenv import load_dotenv
import os
import requests
import json
from google import genai
from flask import Flask, render_template, request

# Load API keys
load_dotenv()
api_key1 = os.getenv("api_key")
api_key2 = os.getenv("api_key2")

app = Flask(__name__)
client = genai.Client(api_key=api_key1)

def video_data(playlist_id):
    token = None
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    videos_array = []

    while True:
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "maxResults": 50,
            "key": api_key2,
            "pageToken": token
        }
        response = requests.get(url, params=params).json()
        
        for video_item in response.get("items", []):
            snippet = video_item["snippet"]
            videos_array.append({
                "title": snippet["title"],
                "url": f"https://www.youtube.com/watch?v={snippet['resourceId']['videoId']}",
                "description": snippet["description"],
                "thumbnail": snippet["thumbnails"].get("maxres", {"url": ""})["url"]
            })

        token = response.get("nextPageToken")
        if not token: break
    
    return videos_array

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    playlist_url = request.form["playlist_url"]
    input_prompt = request.form["query"]
    
    # Extract ID
    playlist_id = playlist_url.split('list=')[-1]
    
    # Get Data
    videos = video_data(playlist_id)
    
    # Prepare Prompt
    prompt = f"""
    You are an expert data analysis engine. Rank these videos by relevance to: "{input_prompt}".
    
    ### INPUT DATA:
    {json.dumps(videos)}
    
    ### INSTRUCTIONS:
    1. Analyze the metadata (title and description) to determine relevance.
    2. Calculate a "relevance_score" (1-10). Ignore videos with low relevance.
    3. Return ONLY a valid JSON array. No conversational text or markdown.
    
    ### OUTPUT FORMAT:
    [
      {{"relevance_score": 1, "url": "string", "title": "string", "thumbnail": "string", "description": "string"}}
    ]
    """

    # Call AI
    response = client.models.generate_content(
        model="gemini-2.0-flash", # Changed to 1.5-flash for better free-tier stability
        contents=prompt
    )
    
    results = json.loads(response.text)
    return render_template("result.html", videos=results)

if __name__ == "__main__":
    app.run(debug=True)