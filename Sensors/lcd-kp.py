import RPi.GPIO as GPIO
import LCD1602
from kpLib import keypad
from time import sleep
myPad=keypad(returnChar='D')
LCD1602.init(0x27,1)
try:
    while True:
        LCD1602.write(0,0,"Input Value:")
        myString=myPad.readKey()
        LCD1602.write(0,0,"User Input Was: "+ myString)
        LCD1602.write(0,1, myString)
        sleep(5)
        LCD1602.clear()
except KeyboardInterrupt:
    sleep(.2)
    LCD1602.clear()
    GPIO.cleanup()
    print("Program stopped by User")
