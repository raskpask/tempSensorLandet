from flask import Flask,request
from messengerAPI import MessengerHandler
from values import Values
import json
import threading
import datetime
app = Flask(__name__)
SERVER_IP = '192.168.1.16'
values = Values()
messengerAPI = MessengerHandler()
userIDs = messengerAPI.getUsers()
warningTemp = 6

@app.route('/setTemp',methods = ['POST'])
def setTemp():
    try:
        messengerAPI = MessengerHandler()
        values.setTemp(int(request.form['temp']))
        values.setHumid(int(request.form['humid']))
        if warningTemp > values.getTemp():
            for userID in userIDs:
                messengerAPI.sendMessage(userID, f"Hej!\nTemperaturen i huset har sjunkit under {warningTemp} Grader Celsius.\nJust nu: {values.getTemp()} Grader Celsus.\nFor att kontrollera temp skriv 'info'.\nMVH\nHuset")
        values.setTime(datetime.now())
        return 'Done'
    except:
        abort(500)

def fetch():
    threading.Timer(5.0, fetch).start()
    try:
      messengerAPI.fetchMessage(values.getTemp(),values.getHumid(),values.getTime(),userIDs)
    except:
        print("Error")

if __name__ == '__main__':
    fetch()
    app.run(host = SERVER_IP, debug=False)

