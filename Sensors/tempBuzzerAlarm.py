import RPi.GPIO as GPIO
import ADC0834
import LCD1602
import dht11
import time
GPIO.setmode(GPIO.BCM)

buzzPin=22
tempPin=26
buttonPin=24

myDHT=dht11.DHT11(pin=tempPin)
GPIO.setup(buzzPin,GPIO.OUT)
GPIO.output(buzzPin,GPIO.HIGH)
ADC0834.setup()
LCD1602.init(0x27,1)

GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
buttonState=1
buttonStateOld=1
setMode=True
buzzVal=85

try:
    while True:
        buttonState=GPIO.input(buttonPin)
        if buttonState==1 and buttonStateOld==0:
            setMode= not setMode
        print(setMode)
        buttonStateOld=buttonState
        time.sleep(.2)
        if setMode==True:
            analogVal=ADC0834.getResult()
            buzzVal=int(analogVal*(100/255))
            LCD1602.write(0,0,"Set Trip Temp: ")
            LCD1602.write(0,1,str(buzzVal))
            time.sleep(.25)
            LCD1602.clear()
            GPIO.output(buzzPin,GPIO.HIGH)
        if setMode==False:
            time.sleep(2)
            result = myDHT.read()
            print("Read result:", result.is_valid())
            if result.is_valid():
                tempC=result.temperature
                tempF=tempC*1.8+32
                tempF=round(tempF,1)
                hum=result.humidity
                print(buzzVal)
                if tempF<buzzVal:
                    GPIO.output(buzzPin,GPIO.HIGH)
                    LCD1602.write(0,0,"Temp: ")
                    LCD1602.write(6,0,str(tempF))
                    LCD1602.write(11,0," F")
                    LCD1602.write(0,1,"Humidity: ")
                    LCD1602.write(10,1,str(hum))
                    LCD1602.write(14,1," %")
                if tempF>=buzzVal:
                    GPIO.output(buzzPin,GPIO.LOW)
                    LCD1602.write(0,0,"Temp: ")
                    LCD1602.write(6,0,str(tempF))
                    LCD1602.write(11,0," F")
                    LCD1602.write(0,1,"ALERT: HIGH TEMP!")
    time.sleep(.1)
except KeyboardInterrupt:
    time.sleep(.2)
    GPIO.cleanup()
    LCD1602.clear()
    print("Program stopped by User")
