# 30.05.2021, Author: dogacans

import requests
import time

# Put your locationiq API key here. To get a key: https://locationiq.com/
# Key is free for personal use, with limitations.
IQ_KEY = "PUT_YOUR_KEY_HERE"

# URL to get ISS coordinates. No API key needed.
getCoordUrl = "http://api.open-notify.org/iss-now.json"
# URL to get reverse geocoding. Can use us1 instead of eu1 if you are closer to USA.
getAddressUrl = "https://eu1.locationiq.com/v1/reverse.php"

# Error to print when we can't get an address from locationiq, usually when ISS is over an ocean
oceanError = "International Space Station is probably orbiting over an ocean right now, can not provide an address."
oldAddress = ''

while True:

    # get the coordinates, put it in latLong
    response = requests.get(getCoordUrl)
    latLong = response.json()['iss_position']
    
    # Parameters to add to the GET request. Documentation: https://locationiq.com/docs
    data = {
    'key': IQ_KEY,
    'lat': latLong['latitude'],
    'lon': latLong['longitude'],
    'format': 'json'
    }

    try:
        address = requests.get(getAddressUrl, params=data).json()['display_name']
    
    # Printing oceanError if locationiq returns unknown address
    except KeyError:
        if oldAddress != oceanError:
            print(oceanError)
            oldAddress = oceanError
        time.sleep(10)
        continue

    if address != oldAddress:
        print("International Space Station is currently orbiting over " + address)

    oldAddress = address
    time.sleep(10)
