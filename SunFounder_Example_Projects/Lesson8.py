import RPi.GPIO as GPIO
import time

relayPin = 17

# Define a setup function for some setup
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayPin, GPIO.OUT, initial=GPIO.LOW)

# Define a main function for main process
def main():
    while True:
        print ('...Relay open')
        # Tick
        GPIO.output(relayPin, GPIO.LOW)
        time.sleep(1)
        print ('Relay close...')
        # Tock
        GPIO.output(relayPin, GPIO.HIGH)
        time.sleep(1)

def destroy():
    # Turn off LED
    GPIO.output(relayPin, GPIO.LOW)
    # Release resource
    GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
