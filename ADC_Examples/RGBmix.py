import RPi.GPIO as GPIO
import ADC0834
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
LEDred=23
LEDgreen=24
LEDblue=21

GPIO.setup(LEDred,GPIO.OUT)
GPIO.setup(LEDgreen,GPIO.OUT)
GPIO.setup(LEDblue,GPIO.OUT)

myPWMred=GPIO.PWM(LEDred,1000)
myPWMred.start(0)
myPWMgreen=GPIO.PWM(LEDgreen,1000)
myPWMgreen.start(0)
myPWMblue=GPIO.PWM(LEDblue,1000)
myPWMblue.start(0)

ADC0834.setup()

try: 
    while True:
        analogRed=ADC0834.getResult(0)
        analogGreen=ADC0834.getResult(1)
        analogBlue=ADC0834.getResult(2)

        print('RawRed= ',analogRed, 'RawGreen= ',analogGreen, 'RawBlue= ',analogBlue) 

        DCred=analogRed*100/255
        DCgreen=analogGreen*100/255
        DCblue=analogBlue*100/255
        if DCred<=3:
            DCred=0
        if DCgreen<=3:
            DCgreen=0
        if DCblue<=3:   
            DCblue=0
        myPWMred.ChangeDutyCycle(DCred)
        myPWMgreen.ChangeDutyCycle(DCgreen)
        myPWMblue.ChangeDutyCycle(DCblue)
        sleep(.2)
        
except KeyboardInterrupt:
    myPWMred.stop()
    myPWMgreen.stop()
    myPWMblue.stop()
    GPIO.cleanup()
    print('GPIO Good to Go')
