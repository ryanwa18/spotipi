# app.py

# also importing the request module
from flask import Flask, render_template, request
import sys,os
import configparser

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../../config/rgb_options.ini')

# Configuration for the matrix
config = configparser.ConfigParser()

# home route
@app.route("/")
def hello():
    config.read(filename)
    
    # Brightness from config file
    brightness = int(config['DEFAULT']['brightness'])
    return render_template('index.html', brightness = brightness)

# serving form web page
@app.route("/form")
def form():
    return render_template('form.html')

# handling form data
@app.route('/brightness', methods=['POST'])
def handle_data():
    config.set('DEFAULT', 'brightness', request.form['brightness'])
    with open(filename, 'w') as configfile:
        config.write(configfile)
    return render_template('index.html', brightness = request.form['brightness'])

app.run(debug = True) 
