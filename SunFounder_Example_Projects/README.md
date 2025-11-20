# Slide Switch – Raspberry Pi Electronic Kit (Lesson 7)

This project demonstrates how to use a **slide switch** to control two LEDs on a Raspberry Pi.
Depending on the slide switch position, either **LED1** or **LED2** will turn on.

---

https://github.com/user-attachments/assets/1d76f6a4-ca38-4659-b681-7ddb06b1d8b7
> Switch left → LED1 ON

> Switch right → LED2 ON
---

## 📘 Overview

A slide switch has three pins:

* **Middle pin** → signal input to the Raspberry Pi
* **Left pin** → GND
* **Right pin** → 3.3V

When the switch slides left or right, different pins connect, changing the signal read by the Pi.
This lesson shows how to read that signal and light up one of two LEDs.

---

## 🛠 Hardware Required

* Raspberry Pi
* Slide switch (3-pin)
* 2× LEDs
* 2× 220Ω resistors
* Jumper wires
* Breadboard

---

## 🔌 Circuit Wiring

**Slide Switch:**

* Middle pin → GPIO 11 (BCM 17 in Python example)
* Left pin → GND
* Right pin → 3.3V

**LEDs:**

* LED1 anode → GPIO 13
* LED2 anode → GPIO 15
* Cathodes → GND (through 220Ω resistors)

Behavior:

* Switch **left** → Pi reads **1** → LED1 on
* Switch **right** → Pi reads **0** → LED2 on

---

## 💻 Code (Python Example)

```python
import RPi.GPIO as GPIO
import time

slidePin = 17
led1Pin = 27
led2Pin = 22

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(slidePin, GPIO.IN)
    GPIO.setup(led1Pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(led2Pin, GPIO.OUT, initial=GPIO.LOW)

def loop():
    while True:
        if GPIO.input(slidePin) == 1:
            GPIO.output(led1Pin, GPIO.HIGH)
            GPIO.output(led2Pin, GPIO.LOW)
        else:
            GPIO.output(led1Pin, GPIO.LOW)
            GPIO.output(led2Pin, GPIO.HIGH)
        time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
```

---

# Relay – Raspberry Pi Electronic Kit (Lesson 8)

This project demonstrates how to use a **relay** with a Raspberry Pi to control a higher-power device (simulated here with an LED).
The relay clicks between **normally open (NO)** and **normally closed (NC)** positions based on the GPIO signal.

---


https://github.com/user-attachments/assets/a94f2632-1515-4402-ba01-ace39770a424
> Relay clicks between open and closed every second, turning the LED **ON / OFF**.

---

## 📘 Overview

A relay is an electrically-controlled switch.
A small control signal from your Raspberry Pi energizes an internal electromagnet, which flips the relay’s contacts.

This allows the Pi to control devices that use **higher voltage or higher current** than GPIO pins can handle directly.

Relays include:

* **Electromagnet coil**
* **Armature** (moving metal switch)
* **Spring**
* **NO (Normally Open) contact**
* **NC (Normally Closed) contact**
* **Freewheeling diode** (protection)

---

## 🛠 Hardware Required

* Raspberry Pi
* Relay module
* NPN transistor
* 1N4007 diode
* LED
* 220Ω resistor
* Jumper wires
* Breadboard

---

## 🔌 Circuit Wiring

**Control Side (low voltage):**

* Raspberry Pi GPIO 11 (BCM 17) → transistor base (through relay circuit)
* Relay coil powered through transistor
* Diode across relay coil for protection
* Relay pin → 5V
* Relay pin → GND

**Load Side:**

* LED anode → Relay NO contact
* Relay common contact → 5V
* LED cathode → GND through resistor

Behavior:

* GPIO HIGH → relay energizes → **NO closes** → LED ON
* GPIO LOW → relay releases → **NO opens** → LED OFF

You’ll hear a soft **“tick-tock”** sound as the relay switches.

---

## 💻 Code (Python Example)

```python
import RPi.GPIO as GPIO
import time

relayPin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayPin, GPIO.OUT, initial=GPIO.LOW)

def loop():
    while True:
        print("Relay Open (LED OFF)")
        GPIO.output(relayPin, GPIO.LOW)
        time.sleep(1)

        print("Relay Close (LED ON)")
        GPIO.output(relayPin, GPIO.HIGH)
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
```

---

# Button Piano – Raspberry Pi Electronic Kit (Lesson 13)

This project demonstrates how to use **buttons** and a **passive buzzer** to create a simple piano with your Raspberry Pi.
Pressing the buttons plays the corresponding musical notes (DO, RE, MI, FA, SO, LA, TI).

---


https://github.com/user-attachments/assets/d4141ea3-25ac-45e8-ab75-1dd12e1fc71d
> Press the seven buttons to play notes with the buzzer.

---

## 📘 Overview

A passive buzzer produces sound when driven by **PWM (Pulse Width Modulation)** signals.
Each button triggers a specific frequency corresponding to a musical note.

Components:

* **Passive buzzer**
* **Push buttons**
* GPIO pins on Raspberry Pi
* Resistors for button pull-downs (if needed)

Behavior:

* Press button → buzzer emits **corresponding note**
* Release button → buzzer silences

---

## 🛠 Hardware Required

* Raspberry Pi
* Passive buzzer
* 7 push buttons
* Jumper wires
* Breadboard
* Resistors (optional, for pull-down)

---

## 🔌 Circuit Wiring

* Buzzer positive → GPIO 17
* Buzzer negative → GND
* Buttons connected between GPIO pins and GND (pins: 18, 27, 22, 23, 24, 25, 8, 7)
* Optional: add pull-down resistors to buttons

Behavior:

* Button pressed → buzzer plays **assigned note**
* No button pressed → buzzer **OFF**

---

## 💻 Code (Python Example)

```python
import RPi.GPIO as GPIO
import time

Buzzer = 17
BtnPin = [18,27,22,23,24,25,8]  # 7 buttons
CM = [0, 262, 294, 330, 350, 393, 441, 495]  # DO, RE, MI, FA, SO, LA, TI
song = [0, CM[1], CM[2], CM[3], CM[4], CM[5], CM[6], CM[7]]
beat = [1,1,1,1,1,1,1,1]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    for i in BtnPin:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
    while True:
        for i in range(len(BtnPin)):
            if GPIO.input(BtnPin[i]) == 1:
                buzz = GPIO.PWM(Buzzer, song[i+1])
                buzz.start(50)
                time.sleep(beat[i+1]*0.25)
                buzz.stop()

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
```

---

