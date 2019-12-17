#True means that the warning will be turned on
class WarningHandler:
    
    def __init__(self, status):
        self.warning = status
        self.autoWarning = status

    def warningOn(self):
        self.warning = True

    def autoWarningOn(self):
        self.autoWarning=True

    def warningOff(self):
        self.warning = False

    def autoWarningOff(self):
        self.autoWarning=False

    def getMaunalStatus(self):
        return self.warning

    def getAutoStatus(self):
        return self.autoWarning