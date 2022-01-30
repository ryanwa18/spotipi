import logging
import spotipy
import spotipy.util as util

import requests
from io import BytesIO
from PIL import Image

def getSongInfo(username, token_path):
  scope = 'user-read-currently-playing'
  token = util.prompt_for_user_token(username, scope, cache_path=token_path)
  print("hello")
  if token:
      sp = spotipy.Spotify(auth=token)
      result = sp.current_user_playing_track()
    
      if result is None:
         print("No song playing")
      else:  
        song = result["item"]["name"]
        imageURL = result["item"]["album"]["images"][0]["url"]
        print(song)
        return [song, imageURL]
  else:
      print("Can't get token for", username)
      return None
  
