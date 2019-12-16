from mail import Mail_Handler
from warning import Warning_handler
from requests.exceptions import ConnectionError
from messengerAPI import MessengerHandler
import sys, time
MAIL_USERNAME = 'blidohuset@gmail.com'
MAIL_PASSWORD = 'koppen123'
import Adafruit_DHT
SENSOR = Adafruit_DHT.AM2302
PIN = 4
warning_handler = Warning_handler(True)
mail_handler =Mail_Handler()
#Settings for the program!
warning_list = ['molin.jakob@gmail.com','fredrikmolin65@gmail.com']
warning_temp = 6 #The teperature is has to go below to get a warning
delay_warning_message= 900 # 300 loops as aproximately 1 hour 
refresh_intervall= 10
messengerAPI = MessengerHandler()
userIDs = messengerAPI.getUsers()



def get_temp():
    _, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if type(temperature) == float:
        return round(temperature,1) 
    return "Sensor error"
def get_humid():
    humidity, _ = Adafruit_DHT.read_retry(SENSOR, PIN)
    if type(humidity) == float:
        return round(humidity,1)
    return "Sensor error"

def do_command(command):
    if "Off" in command or "off" in command:
        warning_handler.warning_off()
        print("Warning is now turned off")
    elif "On" in command or "on" in command:
        warning_handler.warning_on()
        warning_handler.auto_warning_on()
        print("Warning is now turned on")
def check_new_mails():
    messengerAPI.fetchMessage(userIDs)
    # sender, subject = mail_handler.check_messages(MAIL_USERNAME,MAIL_PASSWORD)
    # if 0 != sender: # 0 equals no new messages
    #     do_command(subject)
    #     info_message = "Hej!\nTemperaturen i huset: " + str(get_temp()) + " Grader Celsius \nLuftfuktighet: " + str(get_humid()) + "%\nKommandon for temperaturvarning: 'On' och 'off'\n\nMVH\nHuset"
    #     mail_handler.send_message(sender,'Temperatur i huset', info_message)
    #     print("Info mail was sent")

def check_temp():
    if get_temp() < warning_temp:
        warning_message= "Hej!\nTemperaturen i huset har sjunkit under "+ str(warning_temp) + " Grader Celsius.\nJust nu: "+ str(get_temp()) + " Grader Celsus.\nIngen ny varning kommer skickas de timmarna som kommer om den inte aktiveras!\nAktivera genom att svara med 'On' i Amne (Subject).\nMVH\nHuset"
        mail_handler.send_message(warning_list,'Temperatur varning', warning_message)
        print("Warning was sent")
        warning_handler.auto_warning_off()
        return True
    return False

time.sleep(15)
print("The program is running and searching for mails...")
while 1:
    try:
        # if warning_handler.get_maunal_status() and warning_handler.get_auto_status():
        #     if check_temp():
        #         i=0
        #         while i<delay_warning_message: 
        #             if warning_handler.get_auto_status():
        #                 break
        #             check_new_mails()
        #             time.sleep(refresh_intervall)
        #             i= i+1
        #         warning_handler.auto_warning_on()
        check_new_mails()        
        time.sleep(refresh_intervall)
    except ConnectionError as e:
        print(e)