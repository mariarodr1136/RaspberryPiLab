import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED1=37
LED2=35
LED3=33
LED4=31
LED5=29

ON=1
OFF=0

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)

GPIO.output(LED1,ON)
GPIO.output(LED2,ON)
GPIO.output(LED3,ON)
GPIO.output(LED4,ON)
GPIO.output(LED5,ON)

time.sleep(5)
GPIO.cleanup()
