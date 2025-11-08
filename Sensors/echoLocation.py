import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trigPin=23
echoPin=24
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)    
try:
    while True:
        GPIO.output(trigPin, 0)
        time.sleep(2E-6)
        GPIO.output(trigPin, 1)
        time.sleep(10E-6)
        GPIO.output(trigPin, 0)
        while GPIO.input(echoPin) == 0:
            pass
        startTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        distance = elapsedTime * 34300 / 2
        print("Distance: %.1f cm" % distance)
        time.sleep(.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleaned up and Exiting")
