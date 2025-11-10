# Raspberry Pi Hardware Experiments 🧠

Welcome to my Raspberry Pi hardware experiments repository!  

This repository is a **work in progress** focused on mastering **hardware interfacing**, **sensor integration**, and **embedded systems programming** with the Raspberry Pi.

It showcases a growing collection of experiments and mini-projects using a variety of electronic components — including ultrasonic sensors, PIR motion detectors, servo motors, ADC modules, LCD displays, RFID readers, and more.

Each module is designed to demonstrate how software and hardware interact to power real-world applications such as **environmental monitoring**, **home automation**, **IoT systems**, and **robotic control**.

By progressively combining these components, this project aims to develop a robust understanding of **electronics**, **signal processing**, and **real-time data acquisition**, forming the foundation for advanced Raspberry Pi and embedded engineering projects.

The ultimate goal of this repository is to serve as a comprehensive, hands-on resource for building **integrated multi-sensor and actuator systems**, enabling complex prototypes and automation solutions while documenting the learning journey with each component and experiment.

---

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/Hardware-Raspberry%20Pi-C51A4A?logo=raspberrypi&logoColor=white) ![GPIO](https://img.shields.io/badge/Module-RPi.GPIO-EE0000) ![Sensors](https://img.shields.io/badge/Category-Sensors-00A86B) ![ADC0834](https://img.shields.io/badge/Chip-ADC0834-FFA500) ![Electronics](https://img.shields.io/badge/Skills-Electronics-yellow) ![Breadboard](https://img.shields.io/badge/Component-Breadboard-lightgrey) ![Python3](https://img.shields.io/badge/Version-Python%203.7+-blue) ![VS Code](https://img.shields.io/badge/Editor-VS%20Code-0078D7?logo=visualstudiocode) ![Git](https://img.shields.io/badge/Version%20Control-Git-F05032?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/Repo-GitHub-181717?logo=github) ![Linux](https://img.shields.io/badge/OS-Linux-lightgrey?logo=linux) ![GPIOZero](https://img.shields.io/badge/Library-GPIOZero-009688) ![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557C) ![SensorsKit](https://img.shields.io/badge/Kit-Sensor%20Modules-orange)

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/2db21b23-a1fe-4959-a9e9-745a955dbc6d" alt="IMG_4893" width="600" height="600">
</p>

---

## 🛠️ Hardware & Kit Details

**Hardware Platform:**
- **Raspberry Pi 4 Model B**  

**Learning Kit:**
- **SunFounder Raphael Ultimate Starter Kit**
  - Provides a wide variety of sensors, actuators, displays, and components for hardware experimentation
  - Comes with detailed example code and guides to facilitate hands-on learning
  - Ideal for prototyping embedded systems and electronics projects

All experiments in this repository are built using components from this kit, ensuring reproducibility for users with the same hardware.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5d860645-a026-41f3-bd59-f1d61252a14b" alt="IMG_4152" width="600" height="600">
</p>

---

## 📂 Repository Structure
```
RaspberryPiLab/
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
│   ├── sos.py                    # Calculates the speed of sound (MPH) using ultrasonic sensor timing
│   ├── pir-motion.py             # Detects motion using a PIR (Passive Infrared) sensor
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

<p align="center">
  <img src="https://github.com/user-attachments/assets/26564b1f-20fd-4b65-bfa2-ecd2772ea7b7" alt="IMG_4517" width="400">
</p>

---

## 🛠️ Hardware Used

### Core Components
- ✅ Raspberry Pi 4 Model B (4GB)
- ✅ Breadboard & jumper wires
- ✅ Breadboard power module  
- 40-Pin GPIO cable  
- ✅ T-shape extension board  
- 9V battery  

### Input & Control Devices
- ✅ Push button
- Slide switch  
- Micro switch  
- Keypad  
- Rotary encoder  
- ✅ Joystick module  
- ✅ Tilt switch sensor  
- Touch sensor  
- Obstacle avoidance sensor  
- Reed switch (speed sensor)  
- ✅ PIR motion sensor  
- DHT-11 temperature & humidity sensor  

### Output Devices
- ✅ LEDs (Red, Green, Blue)
- ✅ RGB LED  
- LED bar graph  
- 7-segment display (single)  
- 4-digit 7-segment display  
- Dot matrix display  
- 12C LCD 1602 display  
- Speaker  
- Audio amplifier module  
- Fan  
- Relay module  

### Communication & Identification
- MFRC522 RFID reader module  
- Camera module  

### Sensors
- ✅ Ultrasonic sensor (HC-SR04)  
- Thermistor  
- Photoresistor (LDR)  
- MPU6050 accelerometer & gyroscope  

### Motors & Drivers
- ✅ Servo motor (SG90)
- ✅ Potentiometer
- Motor (DC)  
- L293D motor driver IC  

### Integrated Circuits & Components
- ✅ ADC0834 chip
- 2x 74HC595 shift registers  
- Transistors (5x 8550 PNP / 5x S8050 NPN)  
- Diodes (IN4007, Zener)  
- Capacitors: 5x 10 μF, (10+10)x 104/103 pF  
- ✅ Resistors (assorted, includes 220 Ω)  

### Miscellaneous
- Passive & active buzzers (2+2x)  
- ✅ Various sensors (temperature, light, etc.)  
- Caps (10x 6×6 mm tactile caps)  

---
  
<p align="center">
  <img src="https://github.com/user-attachments/assets/df8b5af0-1c7e-4860-91a9-af29790351d9" width="600" height="600">
</p>


---

## 📘 Learning Objectives

- Understand GPIO pin control
- Learn how to interface sensors and actuators
- Practice Python for embedded systems
- Build confidence in troubleshooting hardware and software integration


---


## 💡 Future Directions

- Add I2C and SPI communication tutorials
- Include camera and image processing projects
- Explore IoT integration with AWS and MQTT


---

⭐ If you find this repository useful, consider starring it!
