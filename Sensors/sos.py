import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(2E-6)
        GPIO.output(TRIG, True)
        time.sleep(10E-6)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
            pass
        ECHO_start = time.time()
        while GPIO.input(ECHO) == 1:
            pass
        ECHO_end = time.time()
        pulse_duration = ECHO_end - ECHO_start
        sos = 16/pulse_duration* (3600)/(12*5820)
        print("The Speed of Sound is: ", sos, "MPH")
        time.sleep(.2)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
