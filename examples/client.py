# imports for raspberry
import Adafruit_DHT
SENSOR = Adafruit_DHT.AM2302
PIN = 4

import requests
import time
API_ENDPOINT = "http://83.209.246.44:5000/setTemp"

class Main:
    def __init__(self):
        self.run()

    def getTemp(self):
        # return '25'
        _, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        if type(temperature) == float:
            return int(temperature)
        return "Sensor error"

    def getHumidity(self):
        # return '60'
        humidity, _ = Adafruit_DHT.read_retry(SENSOR, PIN)
        if type(humidity) == float:
            return int(humidity)
        return "Sensor error"

    def run(self):
        print("The program is running sending temp updates every 30 mins...")
        while 1:
            try:
                data = {
                    'temp':str(self.getTemp()), 
                    'humid':str(self.getHumidity()) 
                }
                requests.post(url = API_ENDPOINT, data = data)
                print(data)
                time.sleep(1800)
            except EnvironmentError as e:
                print(e)
                time.sleep(360)

main = Main()
