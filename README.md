# Spotipi
### Overview
This project is to display information on 32x32 led matrix from the Spotify web api.
### Getting Started
* Create a new application within the [Spotify developer dashboard](https://developer.spotify.com/dashboard/applications) <br />
* Edit the settings of the application within the dashboard.
    * Set the redirect uri to any local url such as http://127.0.0.1/callback
* Before logging into the raspberry pi, you will need to generate an authentication token.
* To do this, you are going to want to clone my spotipi repository on your main computer.
```
git clone  https://github.com/ryanwa18/spotipi.git
```
* Next go ahead and change into the directory using 
```
cd spotipi
```
* Next we are going to need to set the following environment variables to be used for authentication to the Spotify web api.
```
export SPOTIPY_CLIENT_ID=your_spotify_client_id
export SPOTIPY_CLIENT_SECRET=your_spotify_secret_id
export SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
```
* Go ahead and now run the software by replacing <username> with your spotify username
```
python generateToken.py <username>
```
* This will generate a file named `.cache-<username>`
* You are going to want to scp this file over to your raspberry pi
```
scp .cache-<username> pi@spotipy.local:/home/pi
```
* Clone the repository to your raspberrypi 
```
git clone https://github.com/ryanwa18/spotipi.git
```
* Install the led matrix software by Henner Zeller <br />
```
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh
```
* Install the following python packages
```
pip install spotipy
```
* Set the following environment variables
```
export SPOTIPY_CLIENT_ID=your_spotify_client_id
export SPOTIPY_CLIENT_SECRET=your_spotify_secret_id
export SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
```
* Make sure to set the resource limit for root user
```
sudo su
ulimit -Sr 99
```
### Start Software
```
cd spotipi
sudo --preserve-env python displayCoverArt.py <username> &
```
