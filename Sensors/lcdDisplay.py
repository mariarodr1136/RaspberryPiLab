import LCD1602
import time
LCD1602.init(0x27,1)
try:
    while True:
        LCD1602.write(0,0,"Hello, World!")
        LCD1602.write(0,1,"RPi LCD1602")
        time.sleep(5)
except KeyboardInterrupt:
    time.sleep(.2)
    LCD1602.clear()
    print("Program stopped by User")
