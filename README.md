# Spotipi
### Overview
This project is to display information on 32x32 led matrix from the Spotify web api.
### Getting Started
* Create a new application within the [Spotify developer dashboard](https://developer.spotify.com/dashboard/applications) <br />
* Edit the settings of the application within the dashboard.
    * Set the redirect uri to any local url such as http://127.0.0.1/callback
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
cd spotipy
sudo python --preserve-env displayCoverArt.py <username> &
```
