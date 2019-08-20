from flask import Flask, redirect, url_for, request, abort
from flask_mail import Mail, Message
import sys
app = Flask(__name__)
SERVER_IP = '192.168.1.4'
import Adafruit_DHT
import json
SENSOR = Adafruit_DHT.AM2302
PIN = 4


app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'blidohuset@gmail.com',
	MAIL_PASSWORD = 'koppen123'
	)
mail = Mail(app)
def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(temperature,1)
def get_humid():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(humidity,1)

@app.route('/get_temp_and_humid', methods = ['POST'])
def get_temp_and_humid():
    return json.dumps({'temp':get_temp(), 'humidity':get_humid()})

@app.route('/send_mail', methods = ['POST'])
def send_mail():
	msg = Message("Send Mail Tutorial!",
	    sender="blidohuset@gmail.com",
		recipients=["molin.jakob@gmail.com"])
	msg.body = f"Yo!\nHave you heard the good word of Python???"           
	mail.send(msg)
	return 'Mail sent!'
    
if __name__ == '__main__':
   app.run(host = SERVER_IP, debug=False)