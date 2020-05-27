from flask import Flask,request
from messengerAPI import MessengerHandler
import json
import threading
app = Flask(__name__)
sensorTemp = 20
sensorHumid = 50
warningTemp = 6
SERVER_IP = '83.209.111.80'
messengerAPI = MessengerHandler()
userIDs = messengerAPI.getUsers()

@app.route('/setTemp',methods = ['POST'])
def setTemp():
    try:
        messengerAPI = MessengerHandler()
        sensorTemp = int(request.form['temp'])
        sensorHumid = int(request.form['humid'])
        if warningTemp > sensorTemp:
            for userID in userIDs:
                messengerAPI.sendMessage(userID, f"Hej!\nTemperaturen i huset har sjunkit under {warningTemp} Grader Celsius.\nJust nu: {sensorTemp} Grader Celsus.\nFor att kontrollera temp skriv 'info'.\nMVH\nHuset")
        
        return 'Done'
    except:
        abort(500)

def sendInfo(userID):
    messengerAPI = MessengerHandler()
    messengerAPI.sendMessage(userID, f"Hej!\nTemperaturen i huset är {sensorTemp} och luftfuktigheten är {sensorHumid}\nMvh\nHuset")

def fetch():
    threading.Timer(5.0, fetch).start()
    try:
      messengerAPI.fetchMessage(sendInfo,userIDs)
    except:
        print("Error")

if __name__ == '__main__':
    fetch()
    app.run(host = SERVER_IP, debug=False)

