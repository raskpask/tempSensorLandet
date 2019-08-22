from mail import Mail_Handler
import sys, time
MAIL_USERNAME = 'blidohuset@gmail.com'
MAIL_PASSWORD = 'koppen123'
# import Adafruit_DHT
# SENSOR = Adafruit_DHT.AM2302
PIN = 4
mail_handler =Mail_Handler()
warning_list = ['molin.jakob@gmail.com']
warning_temp = 10
temp = 15
humid =24

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(temperature,1) 

def get_humid():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return round(humidity,1)

def check_new_mails():
    sender = mail_handler.check_messages(MAIL_USERNAME,MAIL_PASSWORD)
    if 0 != sender:
        mail_handler.send_message(sender,'Temperatur i huset',
        f"Hej!\nTemperaturen i huset: {temp} Grader Celsius \nLuftfuktighet: {humid}%\nMVH\nHuset")

def check_temp():
    if 9 < warning_temp:
        mail_handler.send_message(warning_list,'Temperatur varning',
        f"Hej!\nTemperaturen i huset har sjunkit under {warning_temp} Grader Celsius!\nJust nu: {temp} Grader Celsus!\nMVH\nHuset")

print("The program is running and searching for mails")
while 1:
    check_new_mails()
    check_temp()
    time.sleep(15)