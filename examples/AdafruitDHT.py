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
import imaplib

def read(username, password, sender_of_interest):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')

    # Use search(), not status()
    status, response = imap.search(None, 'INBOX', '(UNSEEN)')
    unread_msg_nums = response[0].split()

    # Print the count of all unread messages
    print(len(unread_msg_nums))

    # Print all unread messages from a certain sender of interest
    status, response = imap.search(None, '(UNSEEN)', '(FROM "%s")' % (sender_of_interest))
    unread_msg_nums = response[0].split()
    da = []
    for e_id in unread_msg_nums:
        _, response = imap.fetch(e_id, '(UID BODY[TEXT])')
        da.append(response[0][1])
    print(da)

    # Mark them as seen
    for e_id in unread_msg_nums:
        imap.store(e_id, '+FLAGS', '\Seen')



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
	msg = Message("Temperatur Blido",
	    sender="blidohuset@gmail.com",
		recipients=["molin.jakob@gmail.com"])
	msg.body = "Hej!\nTemperaturen i huset: "+ str(get_temp()) + " C"+ chr(176)+" \nLuftfuktighet: "+ str(get_humid()) + "%\nMVH\nHuset"           
	mail.send(msg)
	return 'Mail sent!'
    
if __name__ == '__main__':
   app.run(host = SERVER_IP, debug=False)