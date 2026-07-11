from dotenv import load_dotenv
import os
import requests
import json

# import api key
load_dotenv()
api_key = os.getenv("api_key")
api_key2 = os.getenv("api_key2")
# print(api_key2)

# taking input from user 
input = "https://www.youtube.com/playlist?list=PL257w7s4XIVVW73H7v2vUtyxDf2OB7tf7"
playlist_id = input.split('list=', 1)[1]
# print (playlist_id)


#request data from yt api
import json
import requests

def video_data(playlist_id):

  token = None
  url = "https://www.googleapis.com/youtube/v3/playlistItems"
  playlist_array = []
  videos_array = []

  while True:
      
    params = {
      "part": "snippet",
      "playlistId": playlist_id,
      "maxResults": 50,
      "key": api_key2
    }

    if token:
      params["pageToken"] = token

    response = requests.get(url, params=params)
    data = response.json()

    playlist_array.append(data)

    for video_item in data["items"]:

      snippet = video_item["snippet"]

      video_details = {
        "title": snippet["title"],
        "video_id": snippet["resourceId"]["videoId"],
        "url": f"https://www.youtube.com/watch?v={snippet['resourceId']['videoId']}",
        "channel": snippet["channelTitle"],
        "published_at": snippet["publishedAt"],
        "description": snippet["description"]
      }

      videos_array.append(video_details)

    token = data.get("nextPageToken")

    if not token:
      break

  with open("playlist_data.json", "w", encoding="utf-8") as file:
    json.dump(playlist_array, file, indent=4, ensure_ascii=False)

  with open("video_data.json", "w", encoding="utf-8") as file:
    json.dump(videos_array, file, indent=4, ensure_ascii=False)

  return videos_array

video_data(playlist_id)

