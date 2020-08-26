import time
import logging
from logging.handlers import RotatingFileHandler
import sys
import spotipy
import spotipy.util as util

import requests
from io import BytesIO
from PIL import Image

from transferImage import display

def main():
  scope = 'user-read-currently-playing'

  if len(sys.argv) > 1:
      username = sys.argv[1]
    
      # Configures logger for storing song data    
      logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='spotipy.log',level=logging.INFO)
      logger = logging.getLogger('spotipy_logger')

      # automatically deletes logs more than 2000 bytes
      handler = RotatingFileHandler('spotipy.log', maxBytes=2000,  backupCount=3)
      logger.addHandler(handler)
  else:
      print("Usage: %s username" % (sys.argv[0],))
      sys.exit()

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

        display(image)
  else:
      print("Can't get token for", username)

# Execute program every 5 seconds
try:
  print("Press CTRL-C to stop.")
  while True:
      main()
      time.sleep(500)
except KeyboardInterrupt:
    sys.exit(0)
