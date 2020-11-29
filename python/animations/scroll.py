import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def scroll(matrix):
  for n in range(-32, 0):  # Start off top-left, move off bottom-right
    matrix.SetImage(image.convert('RGB'), n, 0)
    time.sleep(0.03)  
    matrix.Clear()
  
  matrix.SetImage(image.convert('RGB'))
  time.sleep(10)
  
  for n in range(0, 33):  # Start off top-left, move off bottom-right
    matrix.SetImage(image.convert('RGB'), n, 0)
    time.sleep(0.03)
