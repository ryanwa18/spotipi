
import sys
import spotipy
import spotipy.util as util

import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import requests
from io import BytesIO

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
else:
    print("Can't get token for", username)

# Configuration for the matrix
# options = RGBMatrixOptions()
# options.rows = 32
# options.chain_length = 1
# options.parallel = 1
# options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

# matrix = RGBMatrix(options = options)

# Make image fit our screen.
# image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

# matrix.SetImage(image.convert('RGB'))

# try:
#    print("Press CTRL-C to stop.")
#    while True:
#       time.sleep(100)
# except KeyboardInterrupt:
#    sys.exit(0)
