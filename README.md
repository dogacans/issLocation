# issLocation
This small program gives you the address which International Space Station currently orbits over, with help of  two APIs. It is a program I created with the sole purpose of learning HTTP requests and APIs.

The program uses Open Notify API to get the current coordinates of the ISS (http://open-notify.org/Open-Notify-API/ISS-Location-Now/) and uses LocationIQ API (https://locationiq.com/) to reverse geocode the coordinates and get an address.

The program checks the coordinate every 10 seconds, finds out the address, and prints the address to console if it is different than the last address.

If you see the output "International Space Station is probably orbiting over an ocean right now, can not provide an address.", it is because the ISS is over an ocean, and LocationIQ API does not return the name of the ocean, it returns a string that indicates it can not geolocate the coordinates. If it still can't find an address in the next check, it will not print a new string.

