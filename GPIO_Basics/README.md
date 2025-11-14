# GPIO Basics 🚥

This section covers foundational Raspberry Pi GPIO programming examples. These scripts teach how to control LEDs, buzzers, read button inputs, and use internal pull-up resistors.

## Included Scripts
- **binCount.py** – Demonstrates how to control multiple LEDs connected to GPIO output pins. This program turns on five LEDs simultaneously for five seconds and then safely cleans up the GPIO configuration.
- **ButtonLED.py** – Reads input from a physical button and controls an LED in response. When the button is pressed, the LED turns off; when released, the LED turns on. Includes a clean shutdown routine on keyboard interrupt.
- **intPullUp.py** – Shows how to use internal pull-up resistors with GPIO inputs.
- **myDim.py** – Implements PWM (Pulse Width Modulation) to dim an LED using button inputs.
- **myRGBbutton.py** – Demonstrates how to control an RGB LED using three separate buttons. Each button toggles one color channel (red, green, or blue) on or off independently. The program continuously monitors button states, updates the LED colors in real time, and performs a safe GPIO cleanup when interrupted.
- **passive-beep.py** – Uses a passive buzzer with PWM to sweep through a range of frequencies. This demonstrates generating different tones by changing the PWM frequency over time.
- **active-beep.py** – Controls an active buzzer by toggling it on and off through a GPIO pin. This example shows how to activate a buzzer using digital HIGH/LOW signals.
- **keypad.py** – A simpler keypad test utility used for debugging.  
  Allows checking individual row/column combinations to verify wiring, ensure
  correct GPIO configuration, and confirm that each key is electrically responsive.
- **keypad2.py** – Implements full matrix keypad scanning for a 4×4 keypad.  
  The script drives each row HIGH one at a time and reads all column inputs to
  detect which key is pressed. Includes debouncing and prints the key value in
  real time.
- **kpLib.py** – A reusable Python class that implements a full 4×4 keypad driver. 
  Handles row scanning, column reading, debouncing, and multi-character input until
  a return key is pressed.
- **kp-read.py** – Example program that imports the keypad class, reads a 
  sequence of key presses, and prints the final string when the return key is pressed.

---

https://github.com/user-attachments/assets/741e1b84-bc0f-4ef8-a296-2c75eff9db6f

---

## Concepts Covered

- GPIO pin modes (`BOARD` vs `BCM`)
- Input and output pin configuration
- PWM and brightness control
- Buzzer control (passive vs active)
- Button input handling
- Pull-up and pull-down resistors
- Matrix keypad scanning (row/column driving, input reading, debouncing)
- Keypad wiring verification (testing individual row/column combinations)

## Hardware Needed

- LEDs
- Resistors
- Push buttons
- Passive and active buzzers
- Breadboard and jumper wires
- 4×4 Matrix Keypad (or similar keypad module)
- Additional jumper wires for row/column connections

---
