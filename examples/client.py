# imports for raspberry
# import Adafruit_DHT
# SENSOR = Adafruit_DHT.AM2302
PIN = 4

import requests
import time
API_ENDPOINT = "http://85.226.137.140:5000/setTemp"

class Main:
    def __init__(self):
        self.run()

    def getTemp(self):
        return '4'
        # _, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        # if type(temperature) == float:
        #     return round(temperature, 1)
        # return "Sensor error"

    def getHumidity(self):
        return '55'
        # humidity, _ = Adafruit_DHT.read_retry(SENSOR, PIN)
        # if type(humidity) == float:
        #     return round(humidity, 1)
        # return "Sensor error"

    def run(self):
        print("The program is running sending temp updates every 30 mins...")
        while 1:
            try:
                data = {
                    'temp':self.getTemp(), 
                    'humid':self.getHumidity() 
                }
                requests.post(url = API_ENDPOINT, data = data)
                time.sleep(1800) 
            except ConnectionError as e:
                print(e)
                time.sleep(360)

main = Main()
