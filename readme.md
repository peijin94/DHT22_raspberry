# The backend and webUI for the temp-Meter DHT22

## Module
- Backend : Flask
- Frontend : Simple single page, no framework. Pure HTML, CSS, JS
- 3rd Party : JQurey, Font-awsome-icons, Adafruit_DHT

## Preview
![preview_img](https://github.com/Pjer-zhang/DHT22_raspberry/blob/master/preview.png)

## API 
The flask-server can serve the webpage and also provide an API

API:

[POST] /api/gettmp

will return a pair of number, for example [23,50], this means the current temperature is 23 Degree and the humidity is 50%.



# TODO

Add data logger to the system, considering the limited storage of Rasp-Pi. The logger is run on another system using the api of this system.
