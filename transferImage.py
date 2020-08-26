from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys

def display(image):
  # Configuration for the matrix
  options = RGBMatrixOptions()
  options.rows = 32
  options.chain_length = 1
  options.parallel = 1
  options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

  matrix = RGBMatrix(options = options)

  # Make image fit our screen.
  image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

  matrix.SetImage(image.convert('RGB'))

#  try:
#     print("Press CTRL-C to stop.")
#     while True:
#        time.sleep(100)
#  except KeyboardInterrupt:
#     sys.exit(0)
