import RPi.GPIO as GPIO
from kpLib import keypad
myPad=keypad()
myString=myPad.readKey()
print("You Pressed: ", myString)
GPIO.cleanup()
