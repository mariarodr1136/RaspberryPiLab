import LCD1602
from kpLib import keypad
from time import sleep
import threading
myPad=keypad(returnChar='D')
LCD1602.init(0x27,1)
myString=""
pwd='1234'
def readKP():
    global myString
    while True:
        myString=myPad.readKey()
        sleep(.2)
readThread=threading.Thread(target=readKP,)
readThread.daemon=True
readThread.start()
while True:
    CMD=myString
    if CMD=='A'+pwd:
        LCD1602.write(0,0,"ARMED MODE      ")
    if CMD=='B'+pwd:
        LCD1602.write(0,0,"DISARMED MODE   ")
    if CMD=='C'+pwd:
        LCD1602.write(0,0,"PASSWORD?     ")
        while myString=='C'+pwd:
            pass
        pwd=myString
        LCD1602.write(0,0,"NEW PWD SET     ")
        LCD1602.write(0,1, pwd)
        sleep(2)
        LCD1602.clear()
