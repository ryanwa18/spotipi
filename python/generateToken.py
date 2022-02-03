import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

if len(sys.argv) > 1:
    username = sys.argv[1]
    scope = 'user-read-currently-playing'

    # This way removes the need for a browser, it will instead give the URL to visit in the terminal
    auth = SpotifyOAuth(scope=scope, open_browser=False)
    token = auth.get_access_token()
