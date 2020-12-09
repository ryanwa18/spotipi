import logging
import spotipy
import spotipy.util as util

import requests
from io import BytesIO
from PIL import Image

from transferImage import display

#def saveImage(imageURL):
#  response = requests.get(imageURL)
#  image = Image.open(BytesIO(response.content))
#  image.resize((64,64),Image.ANTIALIAS)
#  image.save('../images/currentSong.png', optimize=True, quality=10)        

def getSongInfo(username, token_path):
  scope = 'user-read-currently-playing'
  token = util.prompt_for_user_token(username, scope, cache_path=token_path)

  if token:
      sp = spotipy.Spotify(auth=token)
      result = sp.current_user_playing_track()
    
      if result is None:
 #       logging.warning("No song is currently playing")
         print "No song playing"
      else:  
        song = result["item"]["name"]
        artist = result["item"]["album"]["artists"][0]["name"]
        imageURL = result["item"]["album"]["images"][0]["url"]
        # Remaining seconds in the song
#        timeLeft = (result["item"]["duration_ms"]/1000) - (result["progress_ms"]/1000) 
#        response = requests.get(imageURL)
#        image = Image.open(BytesIO(response.content))
#        image.resize((64,64),Image.ANTIALIAS)
#        logging.info("Song: %s ", song)
#        logging.info("Artist: %s", artist)
#        logging.info("Image URL: %s ", imageURL)
#        logging.info("Time Left: %ss ", timeLeft)
#        display(image, timeLeft)
        return [song, imageURL]
  else:
      print("Can't get token for", username)
      return None
  
