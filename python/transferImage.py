from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys

def display(image, timeLeft):
  # Configuration for the matrix
  options = RGBMatrixOptions()
  options.rows = 32
  options.chain_length = 1
  options.parallel = 1
  options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'
  options.gpio_slowdown = 2
  options.brightness=40
  matrix = RGBMatrix(options = options)

  # Make image fit our screen.
  image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

  for n in range(-32, 0):  # Start off top-left, move off bottom-right
    matrix.SetImage(image.convert('RGB'), n, 0)
    time.sleep(0.03)  
    matrix.Clear()

  matrix.SetImage(image.convert('RGB')) 
  time.sleep(10)
  
  for n in range(0, 33):  # Start off top-left, move off bottom-right
    matrix.SetImage(image.convert('RGB'), n, 0)
    time.sleep(0.03)
    matrix.Clear()
#  try:
#      print("Press CTRL-C to stop.")
#      while timeLeft > 10:
#        time.sleep(5)
#  except KeyboardInterrupt:
#      sys.exit(0)
