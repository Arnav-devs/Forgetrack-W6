from dotenv import load_dotenv
import os
import requests
import json
# from google import genai
# from flask import Flask, render_template, request
from ut.utility import add_array_in_json, dump_in_json
from ut.api import video_data
# # Load API keys
load_dotenv()
api_key1 = os.getenv("api_key1")
# api_key2 = os.getenv("api_key2")

# app = Flask(__name__)
# client = genai.Client(api_key=api_key1)



# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/search", methods=["POST"])
# def search():
#     playlist_url = request.form["playlist_url"]
#     input_prompt = request.form["query"]
    
#     # Extract ID
#     playlist_id = playlist_url.split('list=')[-1]
    
#     # Get Data
#     videos = video_data(playlist_id)
    
#     # Prepare Prompt
#     prompt = f"""
#     You are an expert data analysis engine. Rank these videos by relevance to: "{input_prompt}".
    
#     ### INPUT DATA:
#     {json.dumps(videos)}
    
#     ### INSTRUCTIONS:
#     1. Analyze the metadata (title and description) to determine relevance.
#     2. Calculate a "relevance_score" (1-10). Ignore videos with low relevance.
#     3. Return ONLY a valid JSON array. No conversational text or markdown.
    
#     ### OUTPUT FORMAT:
#     [
#       {{"relevance_score": 1, "url": "string", "title": "string", "thumbnail": "string", "description": "string"}}
#     ]
#     """

#     # Call AI
#     response = client.models.generate_content(
#         model="gemini-2.0-flash", # Changed to 1.5-flash for better free-tier stability
#         contents=prompt
#     )
    
#     results = json.loads(response.text)
#     return render_template("result.html", videos=results)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    # Get values from the form
    input_url = request.form["input1"]
    input_query = request.form["input2"]

    input_object = {
        "url": input_url,
        "query": input_query
    }
    add_array_in_json("input_file.json")
    dump_in_json("input_file.json",input_object)

    # Send them to the next page
    return render_template("result.html", value1=input_url, value2=input_query)

def fn(api_key1):
    with open ("input_file.json","r") as f:
        data = json.load(f)
    
    url = data[-1]["url"]
    playlist_id = url.split("list=")[1]

    video_data(playlist_id,api_key1)



if __name__ == "__main__":
    app.run(debug=True)