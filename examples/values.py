import datetime

class Values():
    temp = 0
    humid = 0
    datetime = datetime.fromtimestamp(0)
    def __init__(self):
        self.temp = 20
        self.humid = 50
    def setTemp(self,temp):
        self.temp = temp
    def setHumid(self,humid):
        self.humid = humid
    def setTime(self,datetime):
        self.datetime = datetime
    def getTime(self):
        return self.datetime
    def getTemp(self):
        return self.temp
    def getHumid(self):
        return self.humid
    