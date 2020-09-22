from flask import Flask,request,abort
from messengerAPI import MessengerHandler
from values import Values
from datetime import datetime
import json
import sys
import threading
app = Flask(__name__)
SERVER_IP = '192.168.1.15'
values = Values()
# messengerAPI = MessengerHandler()
# userIDs = messengerAPI.getUsers()
warningTemp = 6

@app.route('/setTemp',methods = ['POST'])
def setTemp():
    try:
        f = open("./../frontend/src/data/tempData.json", "r")
        data = json.load(f)
        write = "[\n" + json.dumps(data[0]).split('}')[0] + ', "' + datetime.today().strftime('%Y-%m-%d') + '" : '+ int(request.form['temp']) + "}}" + ",\n" + json.dumps(data[1]).split('}')[0] + ', "' + datetime.today().strftime('%Y-%m-%d') + '" : ' + int(request.form['humid']) + "}}" + "\n]"
        originalStdout = sys.stdout
        f = open("./../frontend/src/data/tempData.json", "w")
        sys.stdout = f
        print(write)
        sys.stdout = originalStdout
        f.close()
        # messengerAPI = MessengerHandler()
        # values.setTemp(int(request.form['temp']))
        # values.setHumid(int(request.form['humid']))
        # if warningTemp > values.getTemp():
        #     for userID in userIDs:
        #         messengerAPI.sendMessage(userID, f"Hej!\nTemperaturen i huset har sjunkit under {warningTemp} Grader Celsius.\nJust nu: {values.getTemp()} Grader Celsus.\nFor att kontrollera temp skriv 'info'.\nMVH\nHuset")
        # values.setTime(datetime.datetime.now())
        return 'Done'
    except:
        abort(500)

# def fetch():
#     threading.Timer(5.0, fetch).start()
#     try:
#       messengerAPI.fetchMessage(values.getTemp(),values.getHumid(),values.getTime(),userIDs)
#     except:
#         print("Error")

if __name__ == '__main__':
    # fetch()
    # setTemp()
    app.run(host = SERVER_IP, debug=False)

