import sys
import spotipy
import spotipy.util as util

import requests
from io import BytesIO
from PIL import Image

from transferImage import display

scope = 'user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    result = sp.current_user_playing_track()
    
    if result is None:
      print("No song is currently playing")
    else:  
      song = result["item"]["name"]
      artist = result["item"]["album"]["artists"][0]["name"]
      imageURL = result["item"]["album"]["images"][0]["url"]
      
      response = requests.get(imageURL)
      image = Image.open(BytesIO(response.content))

      print ("Song: ", song)
      print ("Artist: ", artist)
      print ("Image URL: ", imageURL)

      display(image)
else:
    print("Can't get token for", username)

