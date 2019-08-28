from mail import Mail_Handler
import sys, time
MAIL_USERNAME = 'blidohuset@gmail.com'
MAIL_PASSWORD = 'koppen123'
import Adafruit_DHT
SENSOR = Adafruit_DHT.AM2302
PIN = 4
mail_handler =Mail_Handler()
#Settings for the program!
WARNING_OFF = False
warning_list = ['molin.jakob@gmail.com']
warning_temp = 6


refresh_intervall= 15


def get_temp():
    _, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(temperature,1) 

def get_humid():
    humidity, _ = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(humidity,1)

def get_command(command):
    if command == "Warning off" or 'Warning off':
        WARNING_OFF = True
        print("Warning is now turned off")
    elif command == "Warning on":
        WARNING_OFF = False

def check_new_mails():
    sender, subject = mail_handler.check_messages(MAIL_USERNAME,MAIL_PASSWORD)
    if 0 != sender: # 0 equals no new messages
        print(subject)
        get_command(subject)
        info_message = "Hej!\nTemperaturen i huset: " + str(get_temp()) + " Grader Celsius \nLuftfuktighet: " + str(get_humid()) + "%\nMVH\nHuset"
        mail_handler.send_message(sender,'Temperatur i huset', info_message)
        print("Info mail was sent")

def check_temp():
    if get_temp() < warning_temp:
        warning_message= "Hej!\nTemperaturen i huset har sjunkit under "+ str(warning_temp) + " Grader Celsius!\nJust nu: "+ str(get_temp()) + " Grader Celsus!\nMVH\nHuset"
        mail_handler.send_message(warning_list,'Temperatur varning', warning_message)
        WARNING_OFF = True
        print("Warning was sent")
        return True
    return False

print("The program is running and searching for mails")
while 1:
    check_new_mails()
    if check_temp():
        while WARNING_OFF:
            check_new_mails()
            time.sleep(refresh_intervall)
    time.sleep(refresh_intervall)