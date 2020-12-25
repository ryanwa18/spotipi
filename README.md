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
* Edit settings on the web app: <br />
```
navigate to http://<raspberrypi_hostname or ip_address> within a web browser
```

### Final Product
![](https://i.redd.it/8s1cxqo5jfk51.jpg)
