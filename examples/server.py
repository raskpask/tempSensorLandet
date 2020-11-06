from flask import Flask,request,abort
from mail import Mail_Handler
from values import Values
from datetime import datetime
import json
import sys
import threading
app = Flask(__name__)
SERVER_IP = '192.168.1.15'
values = Values()
mailClient = Mail_Handler()

warningTemp = 40

@app.route('/setTemp',methods = ['POST'])
def setTemp():
    try:
        if (request.form['temp'] != 'Sensor error' or 'Sensor error' != request.form['humid']):
            f = open("./../frontend/src/data/tempData.json", "r")
            data = json.load(f)
            write = "[\n" + json.dumps(data[0]).split('}')[0] + ', "' + datetime.today().strftime('%Y-%m-%d:%H%M') + '" : '+ request.form['temp'] + "}}" + ",\n" + json.dumps(data[1]).split('}')[0] + ', "' + datetime.today().strftime('%Y-%m-%d:%H%M') + '" : ' + request.form['humid'] + "}}" + "\n]"
            originalStdout = sys.stdout
            f = open("./../frontend/src/data/tempData.json", "w")
            sys.stdout = f
            print(write)
            sys.stdout = originalStdout
            f.close()
        if warningTemp > values.getTemp():
            mailClient.send_message("molin.jakob@gmail.com","Temp varning på blido", f"Temperaturen är under {warningTemp} grader.")
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

