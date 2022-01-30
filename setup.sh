#!/bin/bash

echo "Ensure packages are installed:"
sudo apt-get install libopenjp2-7 python3-dbus

echo "Installing spotipy library:"
pip install spotipy --upgrade

echo "Installing pillow library:"
pip install pillow --upgrade

echo "Installing flask library:"
pip install flask --upgrade

echo "Enter your Spotify Client ID:"
read spotify_client_id

echo "Enter your Spotify Client Secret:"
read spotify_client_secret

echo "Enter your Spotify Redirect URI:"
read spotify_redirect_uri

echo "Enter your spotify username:"
read spotify_username

echo "Enter the full path to your spotify token:"
read spotify_token_path

install_path=$(pwd)

echo "Downloading rgb-matrix software setup:"
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh

sed -n '/REBOOT NOW?/q;p' < rgb-matrix.sh > rgb-matrix-spotipi.sh

echo "Running rgb-matrix software setup:"
sudo bash rgb-matrix-spotipi.sh

echo "Removing rgb-matrix setup script:"
sudo rm rgb-matrix.sh
echo "...done"

echo "Removing spotipi service if it exists:"
sudo systemctl stop spotipi
sudo rm -rf /etc/systemd/system/spotipi.*
sudo systemctl daemon-reload
echo "...done"

echo "Removing spotipi-client service if it exists:"
sudo systemctl stop spotipi-client
sudo rm -rf /etc/systemd/system/spotipi-client.*
sudo systemctl daemon-reload
echo "...done"

echo "Creating spotipi service:"
sudo cp ./config/spotipi.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=python ${install_path}/python/displayCoverArt.py ${spotify_username} ${spotify_token_path} < /dev/zero &> /dev/null &" /etc/systemd/system/spotipi.service
sudo mkdir /etc/systemd/system/spotipi.service.d
spotipi_env_path=/etc/systemd/system/spotipi.service.d/spotipi_env.conf
sudo touch $spotipi_env_path
sudo echo "[Service]" >> $spotipi_env_path
sudo echo "Environment=\"SPOTIPY_CLIENT_ID=${spotify_client_id}\"" >> $spotipi_env_path
sudo echo "Environment=\"SPOTIPY_CLIENT_SECRET=${spotify_client_secret}\"" >> $spotipi_env_path
sudo echo "Environment=\"SPOTIPY_REDIRECT_URI=${spotify_redirect_uri}\"" >> $spotipi_env_path
sudo systemctl daemon-reload
sudo systemctl start spotipi
sudo systemctl enable spotipi
echo "...done"

echo "Creating spotipi-client service:"
sudo cp ./config/spotipi-client.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=python ${install_path}/python/client/app.py &" /etc/systemd/system/spotipi-client.service
sudo systemctl daemon-reload
sudo systemctl start spotipi-client
sudo systemctl enable spotipi-client
echo "...done"

echo -n "In order to finish setup a reboot is necessary..."
echo -n "REBOOT NOW? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
        echo "Exiting without reboot."
        exit 0
fi
echo "Reboot started..."
reboot
sleep infinity
