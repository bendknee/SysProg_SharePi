import RPi.GPIO as GPIO
import time
import subprocess
from PIL import Image
import zbarlight
import requests
#from gpiozero import Buzzer


GPIO.setmode(GPIO.BOARD)

#buzzer
GPIO.setup(8, GPIO.OUT)
#button
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#led
GPIO.setup(12, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
#buzzer = Buzzer(13)
GPIO.output(8, GPIO.HIGH)

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(pin, GPIO.LOW)
def beep(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)



try:
    while True:
        input_state = GPIO.input(10)
        if input_state == False:
    
            
            subprocess.call("raspistill -o qrcode.jpg", shell=True)
            scanned_code = ""
	
            file_path = 'qrcode.jpg'
            with open(file_path, 'rb') as image_file:
                image = Image.open(image_file)
                image.load()

                codes = zbarlight.scan_codes(['qrcode'], image)
                scanned_code = str(codes)[3:-2]
                r = requests.get("http://192.168.4.1/verification?code="+scanned_code)
                print(r.json())
                print('QR codes: %s' % scanned_code)
                status = r.json()["status"]
            if(status == "success"):
                blink(12)
            else:
                beep(8)

except KeyboardInterrupt:
    GPIO.cleanup()
