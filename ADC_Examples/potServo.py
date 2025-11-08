import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
pwmPin=4
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)
ADC0834.setup()

try:
    while True:
        potValue = ADC0834.getResult(0)
        pwmPercent = 10/255*(potValue) + 2
        print("Potentiometer Value: {}, PWM %: {:.2f}".format(potValue, pwmPercent))    
        pwm.ChangeDutyCycle(pwmPercent)
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleaned up and Exiting")
