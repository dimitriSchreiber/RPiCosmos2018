#!/bin/sh
cd ~/Desktop
sudo apt-get update
sudo apt-get install libbluetooth-dev -y
sudo apt-get install -y libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev -y
sudo apt-get install pyqt4-dev-tools qt4-designer libjack-dev -y
git clone https://github.com/luetzel/bluez
cd bluez/
./configure --prefix=/usr --mandir=/usr/share/man --sysconfdir=/etc --localstatedir=/var --enable-sixaxis
make -j3
sudo make install
systemctl status bluetooth
sudo systemctl daemon-reload
systemctl status bluetooth
sudo systemctl stop bluetooth
sudo systemctl start bluetooth
sudo systemctl disable bluetooth
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
systemctl status bluetooth
sudo hciconfig
sudo hciconfig hci0 up piscan
wget http://downloads.sourceforge.net/project/qtsixa/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
tar xvfz QtSixA-1.5.1-src.tar.gz
cd QtSixA-1.5.1
wget https://launchpadlibrarian.net/112709848/compilation_sid.patch
patch -p1 < compilation_sid.patch
make
cd utils/bins/
read -n 1 -s key
dmesg
read -n 1 -s key
sudo ./sixpair

