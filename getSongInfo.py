import logging
import spotipy
import spotipy.util as util

import requests
from io import BytesIO
from PIL import Image

from transferImage import display

def getSongInfo(username):
  scope = 'user-read-currently-playing'
  token = util.prompt_for_user_token(username, scope)

  if token:
      sp = spotipy.Spotify(auth=token)
      result = sp.current_user_playing_track()
    
      if result is None:
        logging.warning("No song is currently playing")
      else:  
        song = result["item"]["name"]
        artist = result["item"]["album"]["artists"][0]["name"]
        imageURL = result["item"]["album"]["images"][0]["url"]
      
        response = requests.get(imageURL)
        image = Image.open(BytesIO(response.content))

        logging.info("Song: %s ", song)
        logging.info("Artist: %s", artist)
        logging.info("Image URL: %s ", imageURL)
  else:
      print("Can't get token for", username)
#       display(image)
