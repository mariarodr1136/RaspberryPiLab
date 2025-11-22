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

# Driving LEDs with 74HC595 – Raspberry Pi Electronic Kit (Lesson 18)

This project demonstrates how to use a **74HC595 shift register** to control **8 LEDs** with a Raspberry Pi.  
Using the shift register allows you to save GPIO pins while controlling multiple LEDs.

---


https://github.com/user-attachments/assets/c7322170-643a-4d43-9b5c-b9d80f8c916f



> LEDs light from left → right, then flash together 3 times  
> LEDs light from right → left, then flash together 3 times  
> Loop continues

---

## 📘 Overview

The **74HC595** is an 8-bit shift register with serial input and parallel output:

* **DS (SDI)** → Serial data input  
* **SHCP (SRCLK)** → Shift register clock input  
* **STCP (RCLK)** → Storage register clock input  
* **Q0–Q7** → Parallel outputs to LEDs  
* **MR** → Reset (active low)  
* **OE** → Output enable (active low)  

Data is sent serially from the Raspberry Pi to the 74HC595, then displayed on the LEDs.  
This lesson shows how to shift bits and control the LEDs in patterns.

---

## 🛠 Hardware Required

* Raspberry Pi
* 74HC595 shift register
* 8× LEDs
* 8× 220Ω resistors
* Jumper wires
* Breadboard

---

## 🔌 Circuit Wiring

**74HC595 Pins:**

* DS (serial input) → GPIO 0
* SHCP (shift clock) → GPIO 2
* STCP (storage clock) → GPIO 1
* MR → 3.3V (HIGH)
* OE → GND (LOW)
* Q0–Q7 → LED anodes through 220Ω resistors  
* LED cathodes → GND

Behavior:

* LEDs light **left to right**, then flash all together 3 times  
* LEDs light **right to left**, then flash all together 3 times  
* Pattern repeats in a loop

---

# Traffic Light – Raspberry Pi Electronic Kit (Lesson 20)

This project demonstrates how to use a **74HC595 shift register** to drive a **7-segment display** and control three LEDs on a Raspberry Pi, simulating a traffic light. 
The display shows a countdown timer, and the LEDs change in the order: **Red → Green → Yellow**.

---


https://github.com/user-attachments/assets/4de0dd9e-80a1-4074-97da-b790091dfb6f


> Red LED → 9 seconds

> Green LED → 5 seconds

> Yellow LED → 3 seconds
---

## 📘 Overview

This lesson uses a 74HC595 shift register to extend GPIO outputs and control a 7-segment display. The display shows the remaining seconds for each traffic light color. The LEDs light up according to the traffic light state.

- **Red LED** → 9 seconds
- **Green LED** → 5 seconds
- **Yellow LED** → 3 seconds

---

## 🛠 Hardware Required

* Raspberry Pi
* 3× LEDs (Red, Green, Yellow)
* 3× 220Ω resistors
* 1× 7-segment display
* 1× 74HC595 shift register
* Jumper wires
* Breadboard

---

## 🔌 Circuit Wiring

**74HC595 Shift Register:**

* SDI → GPIO 0
* RCLK → GPIO 1
* SRCLK → GPIO 2

**Traffic Light LEDs:**

* Red → GPIO 3
* Green → GPIO 4
* Yellow → GPIO 5

**7-Segment Display:**

* Connect each segment pin (a–g, DP) to the 74HC595 outputs with current-limiting resistors.

Behavior:

* Display shows countdown for current LED.
* LEDs light according to traffic light state:
  * **Red** → 9s
  * **Green** → 5s
  * **Yellow** → 3s
