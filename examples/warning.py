class Warning_handler:
    
    def __init__(self, status):
        self.warning_on = status

    def warning_on(self):
        self.warning_on = True
    
    def warning_off(self):
        self.warning_on = False
    
    def get_status(self):
        return self.warning_on