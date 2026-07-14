import requests
import json

def video_data(playlist_id,api_key2):
  
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

      if not token:
        break

    # Save to JSON file
    with open("video_data.json", "w", encoding="utf-8") as f:
      json.dump(videos_array, f, indent=6, ensure_ascii=False)

    return videos_array