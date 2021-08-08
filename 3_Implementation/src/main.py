from blynkapi import Blynk 

import requests
import math

import RPi.GPIO as GPIO
import time

TOKEN = "A1E-f7i5Es3cR1icSq3hX5jAII7N84R5tt"  # Put your TOKEN here
DEVICE_LABEL = "raspberry"  # Put your device label here 
VARIABLE_LABEL_1 = "distance"
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



TRIG = 17
ECHO = 27
led = 22
m11=16
m12=12
m21=21
m22=20


GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)                   
GPIO.setup(led,GPIO.OUT) 
GPIO.setup(14,GPIO.OUT)
GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m12,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)
GPIO.setup(m22,GPIO.OUT)

GPIO.output(led, 1)

time.sleep(1)

def ON():
    count=0
    while True:
        i=0
        avgDistance=0
        GPIO.output(TRIG, False)                 
        time.sleep(0.1)                                   

        GPIO.output(TRIG, True)                  
        time.sleep(0.00001)                           
        GPIO.output(TRIG, False)                 

        while GPIO.input(ECHO)==0:
            GPIO.output(led, False)             
        pulse_start = time.time()

        while GPIO.input(ECHO)==1:              
            GPIO.output(led, False) 
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start 

        distance = pulse_duration * 17150        
        distance = round(distance,2)                 
        avgDistance=avgDistance+distance
        
        if avgDistance < 50:
            GPIO.output(14,GPIO.LOW)
            GPIO.output(m11, 0)
            GPIO.output(m12, 0)
            GPIO.output(m21, 0)
            GPIO.output(m22, 0)
            
        else:
            GPIO.output(14,GPIO.HIGH)
            GPIO.output(m11, 0)
            GPIO.output(m12, 1)
            GPIO.output(m21, 0)
            GPIO.output(m22, 1)
        
        payload = {VARIABLE_LABEL_1:avgDistance}
        url = "http://things.ubidots.com"
        url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
        status = 400
        attempts = 0
        while status >= 400 and attempts <= 5:
            req = requests.post(url=url, headers=headers, json=payload)
            status = req.status_code
            attempts += 1
            time.sleep(1)

    # Processes results
        if status >= 400:
            print("[ERROR] Could not send data after 5 attempts, please check \your token credentials and internet connection")
            return False

        print("[INFO] request made properly, your device is updated")
        return True
        

        
            
    
def OFF():
    GPIO.output(14,GPIO.LOW)
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    

# vars

auth_token = "31ec8d95ccc84ee09eeae4d17eae15e7"

 

lede = Blynk(auth_token, pin = "V3")

 

while True:

    blink = lede.get_val()

    if blink[0] == u'0':

        OFF()

    elif blink[0] == u'1':

        ON()
        
    
         
