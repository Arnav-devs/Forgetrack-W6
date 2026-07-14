# i = 0
# while("vbskdh"):
#   print("g")
#   i=i+1
#   if (i ==3):
#     break

# if("string" == True):
#   print("yes")
# else: print('no')

# from ut.utility import add_array_in_json
# add_array_in_json("tset.json")

from ut.api import video_data
url = "https://www.youtube.com/playlist?list=PLbSVnB00gZfk"
playlist_id = url.split("list=")[1]
print (playlist_id)

# video_data("PLbSVnB00gZfk","AIzaSyAzyAJ_D0xWQAYqkBtonZIIfvvylw4ojmE")
