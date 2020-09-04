import time
import sys
import logging
from logging.handlers import RotatingFileHandler
from getSongInfo import getSongInfo

if len(sys.argv) > 1:
    username = sys.argv[1]
    
    # Configures logger for storing song data    
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='spotipy.log',level=logging.INFO)
    logger = logging.getLogger('spotipy_logger')

    # automatically deletes logs more than 2000 bytes
    handler = RotatingFileHandler('spotipy.log', maxBytes=2000,  backupCount=3)
    logger.addHandler(handler)

    while 1:
      getSongInfo(username)
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()
