from flask import Flask, redirect, url_for, request, abort
from flask_mail import Mail, Message
from mail import Mail_Handler
import sys
app = Flask(__name__)
SERVER_IP = '192.168.1.4'
MAIL_USERNAME = 'blidohuset@gmail.com'
MAIL_PASSWORD = 'koppen123'
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
	MAIL_USERNAME = MAIL_USERNAME,
	MAIL_PASSWORD = MAIL_PASSWORD
	)
mail = Mail(app)
mail_handler =Mail_Handler()
import imaplib

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(temperature,1) 

def get_humid():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(humidity,1)

def send_mail(reciver):
	msg = Message("Temperatur Blido",
	    sender="blidohuset@gmail.com",
		recipients=[reciver])
	msg.body = "Hej!\nTemperaturen i huset: "+ str(get_temp()) + " C"+ chr(176)+" \nLuftfuktighet: "+ str(get_humid()) + "%\nMVH\nHuset"           
	mail.send(msg)
	return 'Mail sent!'

def check_new_mails():
    sender = mail_handler.check_messages(MAIL_USERNAME,MAIL_PASSWORD)
    if 0 != sender:
        send_mail(sender)
        
@app.route('/get_temp_and_humid', methods = ['POST'])
def get_temp_and_humid():
    return json.dumps({'temp':get_temp(), 'humidity':get_humid()})


if __name__ == '__main__':
   app.run(host = SERVER_IP, debug=False)