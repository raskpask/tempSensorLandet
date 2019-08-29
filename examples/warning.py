#True means that the warning will be turned on
class Warning_handler:
    
    def __init__(self, status):
        self.warning = status

    def warning_on(self):
        self.warning = True
    
    def warning_off(self):
        self.warning = False
    
    def get_status(self):
        return self.warning