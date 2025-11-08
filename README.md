# Raspberry Pi Tutorial Codes⚡️

Welcome to my Raspberry Pi tutorial repository!  

This repo contains all the code examples, scripts, and small projects I've written while experimenting with the Raspberry Pi.  

Each folder includes a dedicated tutorial or project — from simple GPIO basics to sensor integrations and mini automation systems.

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/Hardware-Raspberry%20Pi-C51A4A?logo=raspberrypi&logoColor=white) ![GPIO](https://img.shields.io/badge/Module-RPi.GPIO-EE0000) ![Sensors](https://img.shields.io/badge/Category-Sensors-00A86B) ![ADC0834](https://img.shields.io/badge/Chip-ADC0834-FFA500) ![Electronics](https://img.shields.io/badge/Skills-Electronics-yellow) ![Breadboard](https://img.shields.io/badge/Component-Breadboard-lightgrey) ![Python3](https://img.shields.io/badge/Version-Python%203.7+-blue) ![VS Code](https://img.shields.io/badge/Editor-VS%20Code-0078D7?logo=visualstudiocode) ![Git](https://img.shields.io/badge/Version%20Control-Git-F05032?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/Repo-GitHub-181717?logo=github) ![Linux](https://img.shields.io/badge/OS-Linux-lightgrey?logo=linux) ![GPIOZero](https://img.shields.io/badge/Library-GPIOZero-009688) ![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557C) ![SensorsKit](https://img.shields.io/badge/Kit-Sensor%20Modules-orange)

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/2db21b23-a1fe-4959-a9e9-745a955dbc6d" alt="IMG_4893" width="600" height="600">
</p>

---

## 🧠 Overview

This repository serves as a **learning archive** and **reference hub** for anyone exploring embedded systems and hardware programming with the Raspberry Pi.

You'll find beginner-friendly examples in **Python**, plus explanations on how to connect and test each component.

---

## 🛠️ Hardware & Kit Information

**Hardware Platform:**
- **Raspberry Pi 4 Model B** 

**Learning Kit:**
- **SunFounder Raphael Ultimate Starter Kit**
  - This comprehensive kit includes a wide variety of components perfect for learning electronics and programming
  - Contains sensors, actuators, displays, and essential components for building projects
  - Comes with detailed tutorials and example code to get started

All projects and tutorials in this repository are built using components from this kit, making it easy to follow along if you have the same setup.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5d860645-a026-41f3-bd59-f1d61252a14b" alt="IMG_4152" width="600" height="600">
</p>

---


## 📂 Repository Structure
```
RaspberryPiTutorials/
│
├── GPIO_Basics/
│   ├── buttonLED.py              # Basic button-controlled LED
│   ├── intPullUp.py              # Input with internal pull-up resistor
│   ├── binCount.py               # Sequential LED blinking example
│   ├── myDim.py                  # PWM LED dimmer using buttons
│   ├── myRGBbutton.py            # RGB LED controlled by multiple buttons
│   └── README.md
│
├── Sensors/
│   ├── echoLocation.py           # Ultrasonic distance sensor (HC-SR04)
│   ├── tiltTest.py               # Tilt sensor reading
│   └── README.md
│
├── ADC_Examples/
│   ├── anIn.py                   # Basic analog input using ADC0834
│   ├── joyStick.py               # Joystick X/Y reading via ADC0834
│   ├── potServo.py               # Potentiometer controlling a servo motor
│   ├── RGBmix.py                 # RGB LED color mixing via analog inputs
│   └── README.md
│
└── Projects/
    ├── motion_alarm_system.py    # (future project placeholder)
    ├── rgb_led_controller.py     # (future project placeholder)
    └── README.md
```

---

## ⚙️ Requirements

Make sure you have the following installed on your Raspberry Pi:

- Raspberry Pi OS 
- Python 3 
- `RPi.GPIO` or `gpiozero` module  
- `lgpio` (for advanced GPIO control)
- `time`, `os`, `sys` (standard libraries)

To install missing packages:
```bash
sudo apt update
sudo apt install python3-gpiozero
```

---

### 🔧 Understanding the Raspberry Pi GPIO Pinout
<p align="center">
  <img src="https://github.com/user-attachments/assets/911d0daa-3e0d-46dd-9a93-f1c28372f181" alt="Screenshot 2025-10-29 at 4 56 40 PM" width="885" height="503">
</p>
> This diagram helps identify the GPIO pins used for digital I/O, ADC modules, and external components in these projects.

---

## 🚀 How to Run

1. Clone this repository:
```bash
git clone https://github.com/<your-username>/RaspberryPiTutorials.git
cd RaspberryPiTutorials
```

2. Open any tutorial folder, for example:
```bash
cd GPIO_Basics
```

3. Run the script with:
```bash
python3 buttonLED.py
```

---

## 🧩 Topics Covered

- GPIO setup and cleanup
- Digital input/output
- PWM and LED control
- Button debouncing
- Reading analog sensors with ADC0834
- Servo motor control
- Basic hardware debugging

---

## 🛠️ Hardware Used

- Raspberry Pi 4 Model B (4GB)
- Breadboard & jumper wires
- LEDs (Red, Green, Blue)
- 220Ω resistors
- Push button
- ADC0834 chip
- Potentiometer
- Servo motor (SG90)
- Various sensors (temperature, light, etc.)

---
  
<p align="center">
  <img src="https://github.com/user-attachments/assets/df8b5af0-1c7e-4860-91a9-af29790351d9" width="600" height="600">
</p>


---

## 📘 Learning Goals

- Understand GPIO pin control
- Learn how to interface sensors and actuators
- Practice Python for embedded systems
- Build confidence in troubleshooting hardware and software integration


---

## 💡 Future Plans

- Add I2C and SPI communication tutorials
- Include camera and image processing projects
- Explore IoT integration with AWS and MQTT


---

⭐ If you found this helpful, consider starring the repo!
