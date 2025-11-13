import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
motionPin=23
buzzPin=26
GPIO.setup(buzzPin,GPIO.OUT)
GPIO.output(buzzPin,GPIO.HIGH)
GPIO.setup(motionPin,GPIO.IN)
ADC0834.setup()
sleep(2)
try:
    while True:
        motion=GPIO.input(motionPin)
        lightVal=ADC0834.getResult(0)
        print("Light Value: ", lightVal, " Motion: ", motion    )
        sleep(.1)
        if motion==1 and lightVal<140:
            GPIO.output(buzzPin,GPIO.LOW)
            print("INTRUDER ALERT: Deploy Countermeasures! ")
        else:
            print("Area Secure")
            GPIO.output(buzzPin,GPIO.HIGH)
except KeyboardInterrupt:
        sleep(0.25)
        GPIO.cleanup()
        print("Program terminated")
