# Spotipi
### Overview
This project is to display information on 32x32 led matrix from the Spotify web api.
### Getting Started
* Create a new application within the [Spotify developer dashboard](https://developer.spotify.com/dashboard/applications) <br />
* Edit the settings of the application within the dashboard.
    * Set the redirect uri to any local url such as http://127.0.0.1/callback
* Before logging into the raspberry pi, you will need to generate an authentication token.
* To do this, you are going to want to clone my spotipi repository on your main computer with access to a web browser.
```
git clone  https://github.com/ryanwa18/spotipi.git
```
* Next go ahead and change into the directory using 
```
cd spotipi
```
* Run the generate token script and enter the prompted spotify credentials using
```
bash generate-token.sh
```
* This will generate a file named `.cache-<username>`
* You are going to want to scp this file over to your raspberry pi, for example:
```
scp .cache-<username> pi@spotipy.local:/home/pi
```
* SSH into your raspberrypi
```
ssh raspberrypi.local -l pi
```
* It will ask you for a password so just type in a password of your choice

* Clone the repository to your raspberrypi
```
git clone https://github.com/ryanwa18/spotipi.git
```
* Move the token file to the repository root
```
mv <path_to_cache_file> <path_to_cloned_repository>
```
* Install the software: <br />
```
cd spotipi
sudo bash setup.sh
```
* It will ask you again for spotifyt credentials and the full path to the spotify token
* After this it will run a bash script that will install all of the drivers for the RGB matrix
* It will ask you for your interface board type which should by the Bonnet so select 1
* Next it will ask you to choose between QUALITY and CONVENIENCE (sound vs no sound, requires soldering vs no soldering), choose your preference by typing 1 or 2
* After it finishes setting up its gonna ask you to reboot, type y to confirm
* You can check if your raspberrypi is running properly after reboot by pinging it using
```
ping raspeberrypi.local
```
* Edit settings on the web app: <br />
```
navigate to http://<raspberrypi_hostname or ip_address> within a web browser
```
* After this your rgb matrix should be displaying your cover art, enjoy!

### Final Product
![](https://i.redd.it/8s1cxqo5jfk51.jpg)
