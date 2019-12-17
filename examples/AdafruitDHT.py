# imports for raspberry
import Adafruit_DHT
SENSOR = Adafruit_DHT.AM2302
PIN = 4

from mail import Mail_Handler
from warning import WarningHandler
from requests.exceptions import ConnectionError
from messengerAPI import MessengerHandler
import sys
import time
MAIL_USERNAME = 'blidohuset@gmail.com'
MAIL_PASSWORD = 'koppen123'


mail_handler = Mail_Handler()
# Settings for the program!
warningTemp = 6  # The teperature is has to go below to get a warning
delayWarningMessage = 300  # 300 loops as aproximately 1 hour
refreshIntervall = 10


class Main:
    def __init__(self):
        self.messengerAPI = MessengerHandler()
        self.userIDs = self.messengerAPI.getUsers()
        self.warningHandler = WarningHandler(True)
        self.run()

    def getTemp(self):
        _, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        if type(temperature) == float:
            return round(temperature,1)
        return "Sensor error"

    def getHumidity(self):
        humidity, _ = Adafruit_DHT.read_retry(SENSOR, PIN)
        if type(humidity) == float:
            return round(humidity,1)
        return "Sensor error"

    def sendInfo(self, userID):
        infoMessage = "Hej!\nTemperaturen i huset: " + str(self.getTemp()) + " Grader Celsius \nLuftfuktighet: " + str(self.getHumidity()) + "%\nKommandon for temperaturvarning: 'on' och 'off'\n\nMVH\nHuset"
        self.messengerAPI.sendMessage(userID, infoMessage)

    def warningON(self, userID):
        self.warningHandler.warningOn()
        self.messengerAPI.sendMessage(userID, "Varningar ar nu paslagna!\nDu kommer fa en varning om temperatruen sjunker under+" +self.warningTemp+"grader celcius.\nFor att stanga av det skriv 'off'")

    def warningOff(self, userID):
        self.warningHandler.warningOff()
        self.messengerAPI.sendMessage(userID, "Varningar ar nu avstangda!\nDu kommer INTE fa en varning om temperatruen sjunker under"+ self.warningTemp +"grader celcius.\nFor att satta pa varnignar skriv 'on'")

    def checkNewMails(self):
        self.messengerAPI.fetchMessage(self, self.userIDs)

    def checkTemp(self):
        if self.getTemp() < warningTemp:
                for userID in self.userIDs:

                    self.messengerAPI.sendMessage(userID, "Hej!\nTemperaturen i huset har sjunkit under " + str(warningTemp) + " Grader Celsius.\nJust nu: " + str(self.getTemp()) + " Grader Celsus.\nIngen ny varning kommer skickas de timmarna som kommer om den inte aktiveras!\nFor att kontrollera temp skriv 'info'.\nMVH\nHuset")
            self.warningHandler.autoWarningOff()
            return True
        return False

    def run(self):

        print("The program is running and searching for messages...")
        while 1:
                if (self.warningHandler.getMaunalStatus):
                    if self.checkTemp():
                        i = 0
                        while i < delayWarningMessage:
                            if self.warningHandler.getAutoStatus():
                                break
                            self.checkNewMails()
                            time.sleep(refreshIntervall)
                            i = i+1
                        self.warningHandler.autoWarningOn()
                self.checkNewMails()
                time.sleep(refreshIntervall)
        # time.sleep(15)


main = Main()
