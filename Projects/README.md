
# Projects 🚨

This section features complete Raspberry Pi projects that integrate multiple sensors, actuators, and logic to demonstrate real-world embedded applications. Each project combines concepts from the **GPIO_Basics**, **Sensors**, and **ADC_Examples** sections, providing a bridge between experimentation and system-level prototyping.

---

## 🕵️‍♀️ Motion-Dark Alarm System (`motion-dark-alarm.py`)

### 🔍 Overview

The **Motion-Dark Alarm** project detects motion in low-light environments and triggers a buzzer or LED alert. It combines a **PIR motion sensor** and a **photoresistor (LDR)** connected through the **ADC0834** module. When both conditions (motion + darkness) are met, the system activates an audible or visual alarm.

This project demonstrates **multi-sensor logic**, **ADC integration**, and **real-time control** with GPIO on the Raspberry Pi.

---

![IMG_5111](https://github.com/user-attachments/assets/743b7dcd-8875-4300-a42d-e9024c2cb353)

---

### ⚙️ Features

* Detects motion using a **PIR sensor**
* Measures ambient light intensity with an **LDR**
* Triggers a buzzer or LED alert when motion occurs in the dark
* Adjustable light-sensitivity threshold
* Uses **ADC0834** for analog sensor reading
* Safe shutdown via keyboard interrupt (`Ctrl+C`)

### 🧠 Concepts Applied

* GPIO input/output handling
* Analog sensor interfacing (LDR via ADC0834)
* Conditional logic combining multiple sensors
* Real-time signal monitoring and event-based control

---

## 🧩 Hardware Setup

### 🔌 Components

* Raspberry Pi 4 (or compatible model)
* PIR Motion Sensor (HC-SR501)
* Photoresistor (LDR)
* ADC0834 A/D converter
* Active buzzer or LED
* Breadboard and jumper wires

### 🧰 Circuit Schematic

![Screenshot 2025-11-13 at 2 04 27 PM](https://github.com/user-attachments/assets/d24910f3-d3f1-4f5a-bd85-091dc9dd6369)
> *Note: The motion detector (not shown) connects directly to 3V3, GPIO23, and GND*
---

## 💻 Code Summary

```python
import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
motionPin=23
buzzPin=26
GPIO.setup(buzzPin,GPIO.OUT)
GPIO.output(buzzPin,GPIO.HIGH)
GPIO.setup(motionPin,GPIO.IN)
ADC0834.setup()
sleep(2)
try:
    while True:
        motion=GPIO.input(motionPin)
        lightVal=ADC0834.getResult(0)
        print("Light Value: ", lightVal, " Motion: ", motion)
        sleep(.1)
        if motion==1 and lightVal<140:
            GPIO.output(buzzPin,GPIO.LOW)
            print("INTRUDER ALERT: Deploy Countermeasures! ")
        else:
            print("Area Secure")
            GPIO.output(buzzPin,GPIO.HIGH)
except KeyboardInterrupt:
        sleep(0.25)
        GPIO.cleanup()
        print("Program terminated")
```

## 📘 Learning Outcomes

* Combine multiple sensor inputs for event detection
* Apply ADC for analog light measurement
* Implement alert systems with Python and GPIO
* Reinforce understanding of conditional automation in embedded systems

---

⭐ *More projects will be added soon — stay tuned for IoT integration, remote monitoring, and camera-based automation systems!*
