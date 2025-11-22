import RPi.GPIO as GPIO
import time

Buzzer = 17
BtnPin = [18,27,22,23,24,25,8,7]

CL = [0, 131, 147, 165, 175, 196, 211, 248]        # Frequency of Low C notes
CM = [0, 262, 294, 330, 350, 393, 441, 495]        # Frequency of Middle C notes
CH = [1, 525, 589, 661, 700, 786, 882, 990]        # Frequency of High C notes

song = [     0,CM[1],CM[2],CM[3],CM[4],CM[5],CM[6],CM[7]    ]
beat = [    1,1, 1, 1, 1, 1, 1,  1]

def setup():
    GPIO.setmode(GPIO.BCM)
    for i in range(1, len(BtnPin)):
        GPIO.setup(BtnPin[i],GPIO.IN)
    GPIO.setup(Buzzer, GPIO.OUT)

def loop():
    global Buzz
    while True:
        #print ('\n    Please playing piano...')
        for i in range(1, len(BtnPin)):
            if GPIO.input(BtnPin[i]) == 1:
                Buzz = GPIO.PWM(Buzzer, song[i])
                Buzz.start(50)
                time.sleep(beat[i] * 0.25)
                Buzz.stop()

def destory():
    Buzz.stop()
    GPIO.output(Buzzer, 0)
    GPIO.cleanup()

if __name__ == '__main__':        # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:      # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destory()
