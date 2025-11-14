import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

rows = [11, 13, 15, 29]
columns = [31, 33, 35, 37]
keyPad=[[1,2,3,'A'],
        [4,5,6,'B'],
        [7,8,9,'C'],
        ['*',0,'#','D']]

GPIO.setup(rows[0], GPIO.OUT)
GPIO.setup(rows[1], GPIO.OUT)
GPIO.setup(rows[2], GPIO.OUT)
GPIO.setup(rows[3], GPIO.OUT)

GPIO.setup(columns[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    myRow=int(input("Which Row to Read "))
    myColumn=int(input("Which Column to Read "))
    while True:
        GPIO.output(rows[myRow], GPIO.HIGH)
        butVal=GPIO.input(columns[myColumn])
        GPIO.output(rows[myRow], GPIO.LOW)
        print("Button Value is: ", butVal)
        sleep(.2)
except KeyboardInterrupt:
    sleep(.1)
    GPIO.cleanup()
    print("Program Stopped")
