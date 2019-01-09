from flask import render_template, jsonify, request, Response
import Adafruit_DHT
from flask import Flask
import json

app = Flask(__name__)


@app.route('/api/gettmp',methods=["GET", "POST"])
def draw_stone():
    d_hum,d_temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
    d_hum = round(d_hum,2)
    d_temp = round(d_temp,2)
    data = [d_temp,d_hum]
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/')
def staff_page():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000 )
