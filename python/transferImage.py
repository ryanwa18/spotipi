from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from threading import Thread

import time
import sys,os
import configparser

def timer(timeLeft):
  while timeLeft > 0:
    sleep(1)
    timeLeft = timeLeft - 1

def config():
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

def display(image, timeLeft):
  config()
  timer_thread = Thread(target=timer)

  matrix = RGBMatrix(options = options)

  # Make image fit our screen.
  image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
  
  while not timer_thread.is_alive()
    matrix.SetImage(image.convert('RGB'))   
