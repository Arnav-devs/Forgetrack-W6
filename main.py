from dotenv import load_dotenv
import os

# import api key
load_dotenv()

api_key = os.getenv("api_key")
print (api_key)


