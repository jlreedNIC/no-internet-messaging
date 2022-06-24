# no-internet-messaging
MQTT messaging on a local broker. No internet connection required after setup. 

This program is designed to work with a local MQTT broker to provide messaging over a network without requiring an internet connection. I wrote/am writing this program for personal use because there can be frequrent internet problems on my property and this will provide a convenient 'texting' like interface between households on the property.

## Status
In development.
Working on computer program. Want to develop app for use on android phones.

## Requirements
You will need a local MQTT server that can run constantly (or when needed). I used a raspberry pi for this, and I used the [Eclipse Mosquitto](https://mosquitto.org/) open source software to run it. 

## Install on Linux/Windows
- download files from github
- install python
    - install python from microsoft store for windows
- install paho module
    - `pip install paho-mqtt`
- run program (needs local server set up and running to work properly)
    - linux
        `python3 /<path>/messaging.py`
    - windows
        `Python \<path>\messaging.py`