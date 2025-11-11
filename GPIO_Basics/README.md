# GPIO Basics 🚥

This section covers foundational Raspberry Pi GPIO programming examples. These scripts teach how to control LEDs, read button inputs, and use internal pull-up resistors.

## Included Scripts
- **binCount.py** – Demonstrates how to control multiple LEDs connected to GPIO output pins. This program turns on five LEDs simultaneously for five seconds and then safely cleans up the GPIO configuration.
- **ButtonLED.py** – Reads input from a physical button and controls an LED in response. When the button is pressed, the LED turns off; when released, the LED turns on. Includes a clean shutdown routine on keyboard interrupt.
- **intPullUp.py** – Shows how to use internal pull-up resistors with GPIO inputs.
- **myDim.py** – Implements PWM (Pulse Width Modulation) to dim an LED using button inputs.
- **myRGBbutton.py** – Demonstrates how to control an RGB LED using three separate buttons. Each button toggles one color channel (red, green, or blue) on or off independently. The program continuously monitors button states, updates the LED colors in real time, and performs a safe GPIO cleanup when interrupted.

## Concepts Covered
- GPIO pin modes (`BOARD` vs `BCM`)
- Input and output pin configuration
- PWM and brightness control
- Button input handling
- Pull-up and pull-down resistors

## Hardware Needed
- LEDs
- Resistors
- Push buttons
- Breadboard and jumper wires

---

https://github.com/user-attachments/assets/a840ca55-7319-4776-a2ed-ef5967af9028

---
