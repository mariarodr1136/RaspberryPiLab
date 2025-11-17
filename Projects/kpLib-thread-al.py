import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
PIRpin=12
GPIO.setup(PIRpin,GPIO.IN)
import LCD1602
import kpLib
from time import sleep
import threading
myPad=kpLib.keypad(returnChar='D')
LCD1602.init(0x27,1)
myString=""
pwd='1234'
def readKP():
    global myString
    while myString != '*':
        myString=myPad.readKey()
        sleep(.2)
readThread=threading.Thread(target=readKP,)
readThread.daemon=True
readThread.start()
while myString != '*':
    CMD=myString
    if CMD=='A'+pwd:
        LCD1602.write(0,0,"ARMED MODE      ")
        moveVal=GPIO.input(PIRpin)
        if moveVal==1:
            LCD1602.write(0,1,"INTRUDER ALERT! ")
        if moveVal==0:
            LCD1602.write(0,1,"ALL CLEAR       ")
    if CMD=='B'+pwd:
        LCD1602.write(0,0,"DISARMED MODE   ")
        LCD1602.write(0,1,"ALL SENSORS OFF ")
    if CMD=='C'+pwd:
        LCD1602.write(0,0,"PASSWORD?     ")
        LCD1602.write(0,1,"                ")
        while myString=='C'+pwd:
            pass
        pwd=myString
        LCD1602.write(0,0,"NEW PWD SET     ")
        LCD1602.write(0,1, pwd)
        sleep(2)
        LCD1602.clear()
sleep(1)
GPIO.cleanup()
LCD1602.clear()
print("Exiting program.")
