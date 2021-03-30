ssh pi@192.168.0.11
HTI_hydrophone

sudo blkid   # find usb stick
sudo mkdir /mnt/usbdrive
sudo mount /dev/sda1 /mnt/usbdrive

sudo apt update

sudo apt install python3-pip
#install flask
sudo pip3 install flask
#install numpy
sudo apt-get -y install python3-numpy
#install sounddevice
sudo apt-get install -y libportaudio2
sudo pip3 install sounddevice

export FLASK_APP=app_1.py
flask run



headless setup of Rpi
in boot sector: touch ssh
in boot sector create file: wpa_supplicant.conf
containing:
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}


