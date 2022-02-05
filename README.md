# Spotipi
### Overview
This project is to display information on 32x32 led matrix from the Spotify web api.
### Getting Started
* Create a new application within the [Spotify developer dashboard](https://developer.spotify.com/dashboard/applications) <br />
* Edit the settings of the application within the dashboard.
    * Set the redirect uri to any local url such as http://127.0.0.1/callback
* First step is to ssh to your raspberry pi to clone the repository
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
* This will generate a file named `.cache` which will be used for authentication
    * A url will show up in the terminal window and you must copy this into your own web broswer
    * The url will redirect you to another url and you need to copy/paste this in the terminal when prompted.
   
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
