import RPi.GPIO as GPIO
import time

LedPin = 17
BtnPin = 12
Led_status = False

# Define a setup function for some setup
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BtnPin, GPIO.IN)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed)

# Define a callback function for button callback
def swLed(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)

# Define a main function for main process
def main():
    while True:
        # Don't do anything.
        time.sleep(1)

# Define a destroy function for clean up everything after
# the script finished
def destroy():
    # Turn off LED
    GPIO.output(LedPin, GPIO.LOW)
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
