<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/PrimaryDesk.png" align="center">

# Installation
## Install with pip3
```
sudo pip3 install debdialer
sudo wget https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/raw/master/Images/deblogo-128.png -O /usr/share/icons/hicolor/128x128/apps/deblogo-128.png
sudo wget https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/raw/master/debdialer.desktop -O /usr/share/applications/debdialer.desktop
sudo update-desktop-database /usr/share/applications/
```

## Install from source
```
# After cloning https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master
# Single command (recommended)
sudo python3 setup.py full-install
```
### Other Install options
```
# Install with Qt only
sudo python3 setup.py gui-install

# Install with dmenu only
sudo python3 setup.py nogui-install

# Install with pip
pip3 install .
```
### Optional Dependencies
```
sudo apt install python3-pyqt4 dmenu
```

#### To test the MIME link
```
xdg-open tel:873811
```
### Setting default country code
```
export DEBDIALER_COUNTRY='<2 letter country code>'

# For example
export DEBDIALER_COUNTRY='IN'
```

## Licenses and Copyright information
### [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) (*Python port of Google's [libphonenumber](https://github.com/googlei18n/libphonenumber) library*)
- License : [Apache-2.0](https://github.com/daviddrysdale/python-phonenumbers/blob/dev/LICENSE)
-Copyright : 2009-2015 The Libphonenumber Authors

### Country Codes (*Country and Dial or Phone codes in JSON format*)
- Source : [Github Gist](https://gist.github.com/Goles/3196253)
- Author : [Nicolas Goles](https://gist.github.com/Goles)

### [Country Flags](https://github.com/cristiroma/countries)
- License : [GPL-3.0](https://github.com/cristiroma/countries/blob/master/LICENSE)
- Copyright : 2011 Cristian Romanescu

### [kdeconnect](https://github.com/KDE/kdeconnect-android/)
- License : [GPL-2.0](https://github.com/KDE/kdeconnect-android/blob/master/COPYING)

### [vobject](https://github.com/eventable/vobject)
- License : [Apache-2.0](https://github.com/eventable/vobject/blob/master/LICENSE-2.0.txt)
- Copyright : NA

# Setting up KDE-Connect
Download apk here : [tiny.cc/ddial-kdeconnect](tiny.cc/ddial-kdeconnect)
<br/>
### Installing the apk
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Setup-1.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Setup-2.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Setup-3.jpg" width="200">

### Setting up KDE-Connect
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Setup-4.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Setup-5.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Setup-6.jpg" width="200">

# Usage
## Adding contact using .vcf file (`Add vcard to Contacts`)
#### Selecting vcf file on Debdialer
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AddContFileDesk-1.png" width="400">

#### Adding contact on Android Phone
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AddContFileApp-1.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AddContFileApp-2.jpg" width="200">

## Adding number in dialer as contact (`Add to Contacts`)
#### Selecting vcf file on Debdialer
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AddContactDesk-1.png" width="400">

#### Adding contact on Android Phone
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AddContactApp-1.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AddContactApp-2.jpg" width="200">

## Sending dialer number to Android phone (`DIAL ON ANDROID PHONE`)

#### Notification on Android Phone
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/DialApp-1.jpg" width="200">
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/DialApp-2.jpg" width="200">

## Parsing numbers from file (`Open File`)
#### Choosing File
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/OpenFile-1.png" width="400">
<br/>
#### Printing list of numbers
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/OpenFile-2.png" width="400">
## Automatic formatting of numbers and setting of details
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/AutoDetails.gif" width="400">
