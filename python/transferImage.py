from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys,os
import configparser

def display(image, timeLeft):
  dir = os.path.dirname(__file__)
  filename = os.path.join(dir, '../config/rgb_options.ini')

  # Configuration for the matrix
  config = configparser.ConfigParser()
  config.read(filename)

  options = RGBMatrixOptions()
  options.rows = int(config['DEFAULT']['rows'])
  options.chain_length = int(config['DEFAULT']['chain_length'])
  options.parallel = int(config['DEFAULT']['parallel'])
  options.hardware_mapping = config['DEFAULT']['hardware_mapping']
  options.gpio_slowdown = int(config['DEFAULT']['gpio_slowdown'])
  options.brightness = int(config['DEFAULT']['brightness'])

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
