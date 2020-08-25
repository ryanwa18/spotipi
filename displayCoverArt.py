import sys
import spotipy
import spotipy.util as util

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
    song = result["item"]["name"]
    imageURI = result["item"]["album"]["images"][0]["url"]
    print song
    print imageURI
else:
    print("Can't get token for", username)