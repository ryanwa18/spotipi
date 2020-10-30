import sys
import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
    scope = 'user-read-currently-playing'
    token = util.prompt_for_user_token(username, scope)
