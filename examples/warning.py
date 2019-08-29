#True means that the warning will be turned on
class Warning_handler:
    
    def __init__(self, status):
        self.warning = status
        self.auto_warning = status

    def warning_on(self):
        self.warning = True
    def auto_warning_on(self):
        self.auto_warning=True

    def warning_off(self):
        self.warning = False
    def auto_warning_off(self):
        self.auto_warning=False

    def get_maunal_status(self):
        return self.warning
    def get_auto_status(self):
        return self.auto_warning