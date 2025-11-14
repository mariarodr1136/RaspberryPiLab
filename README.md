# Raspberry Pi Hardware Experiments 🧠

Welcome to my Raspberry Pi hardware experiments repository!  

This hands-on collection of Raspberry Pi hardware projects is designed to teach **hardware interfacing**, **sensor integration**, and **embedded systems programming**, featuring experiments and mini-projects with a wide range of components, including **ultrasonic sensors, PIR motion detectors, servo motors, ADC modules, LCD displays, RFID readers, buzzers, and more**. Each project demonstrates how **software and hardware interact** to create real-world applications such as **environmental monitoring**, **home automation**, **IoT systems**, and **robotic control**, making this repository ideal for anyone looking to **build practical skills in electronics, signal processing, and real-time data acquisition** while developing a strong foundation in **Raspberry Pi embedded engineering**.

---

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/Hardware-Raspberry%20Pi-C51A4A?logo=raspberrypi&logoColor=white) ![GPIO](https://img.shields.io/badge/Module-RPi.GPIO-EE0000) ![Sensors](https://img.shields.io/badge/Category-Sensors-00A86B) ![ADC0834](https://img.shields.io/badge/Chip-ADC0834-FFA500) ![Electronics](https://img.shields.io/badge/Skills-Electronics-yellow) ![Breadboard](https://img.shields.io/badge/Component-Breadboard-lightgrey) ![Python3](https://img.shields.io/badge/Version-Python%203.7+-blue) ![VS Code](https://img.shields.io/badge/Editor-VS%20Code-0078D7?logo=visualstudiocode) ![Git](https://img.shields.io/badge/Version%20Control-Git-F05032?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/Repo-GitHub-181717?logo=github) ![Linux](https://img.shields.io/badge/OS-Linux-lightgrey?logo=linux) ![GPIOZero](https://img.shields.io/badge/Library-GPIOZero-009688) ![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557C) ![SensorsKit](https://img.shields.io/badge/Kit-Sensor%20Modules-orange)


---

<p align="center">
  <img src="https://github.com/user-attachments/assets/f96ba1ca-2a25-4d48-aa68-5eef31c667cf" alt="IMG_4517" width="1000">
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

---

![IMG_5084](https://github.com/user-attachments/assets/0251e93a-90b5-409a-94c3-4f7581f677ca)

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
│   ├── passive-beep.py           # Demonstrates PWM control of a passive buzzer
│   ├── active-beep.py            # Demonstrates digital on/off control of an active buzzer
│   ├── keypad.py                 # Reads one specific row/column pair
│   ├── keypad2.py                # Scans entire keypad matrix and prints key pressed
│   ├── kpLib.py                  # Keypad class library (full row/column scan + multi-key input)
│   ├── kp-read.py                # Demonstration program using the keypad class
│   └── README.md                 # Documentation for all GPIO_Basics scripts
│
├── Sensors/
│   ├── echoLocation.py           # Ultrasonic distance sensor (HC-SR04)
│   ├── tiltTest.py               # Tilt sensor reading
│   ├── sos.py                    # Calculates the speed of sound (MPH) using ultrasonic sensor timing
│   ├── pir-motion.py             # Detects motion using a PIR (Passive Infrared) sensor
│   ├── lcdDisplay.py             # Displays text on an LCD1602 via I2C
│   ├── LCD1602.py                # Low-level library for controlling LCD1602
│   ├── tempLCD.py                # Reads DHT11 sensor and displays temperature/humidity on LCD
│   ├── tempHumidity.py           # Reads DHT11 sensor and prints temperature/humidity to terminal
│   ├── tempBuzzerAlarm.py        # Monitors temperature and humidity, displays on LCD, and triggers buzzer alerts
│   └── README.md                 # Documentation for all Sensor scripts
│
├── ADC_Examples/
│   ├── anIn.py                   # Basic analog input using ADC0834
│   ├── photon-detect.py          # Reads LDR light intensity via ADC0834
│   ├── joyStick.py               # Joystick X/Y reading via ADC0834
│   ├── potServo.py               # Potentiometer controlling a servo motor
│   ├── RGBmix.py                 # RGB LED color mixing via analog inputs
│   └── README.md                 # Documentation for all ADC_Examples scripts
│
└── Projects/
    ├── motion-dark-alarm.py      # Motion and light detection alarm with buzzer alert
    └── README.md                 # Documentation for all Projects scripts
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
git clone https://github.com/mariarodr1136/RaspberryPiTutorials.git
cd RaspberryPiLab
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

![IMG_5085](https://github.com/user-attachments/assets/dfd09dc2-cda8-4642-8f19-ca4e95483955)

---

## 🛠️ Hardware Used

### Core Components
- ✅ Raspberry Pi 4 Model B (4GB)
- ✅ Breadboard & jumper wires
- ✅ Breadboard power module  
- ✅ 40-Pin GPIO cable  
- ✅ T-shape extension board  
- 9V battery  

### Input & Control Devices
- ✅ Push button
- Slide switch  
- Micro switch  
- ✅ Keypad  
- Rotary encoder  
- ✅ Joystick module  
- ✅ Tilt switch sensor  
- Touch sensor  
- Obstacle avoidance sensor  
- Reed switch (speed sensor)  
- ✅ PIR motion sensor  
- ✅ DHT-11 temperature & humidity sensor  

### Output Devices
- ✅ LEDs (Red, Green, Blue)
- ✅ RGB LED  
- LED bar graph  
- 7-segment display (single)  
- 4-digit 7-segment display  
- Dot matrix display  
- ✅ 12C LCD 1602 display  
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
- ✅ Photoresistor (LDR)  
- MPU6050 accelerometer & gyroscope  

### Motors & Drivers
- ✅ Servo motor (SG90)
- ✅ Potentiometer
- Motor (DC)  
- L293D motor driver IC  

### Integrated Circuits & Components
- ✅ ADC0834 chip
- 2x 74HC595 shift registers  
- ✅ Transistors (5x 8550 PNP / 5x S8050 NPN)  
- Diodes (IN4007, Zener)  
- Capacitors: 5x 10 μF, (10+10)x 104/103 pF  
- ✅ Resistors (assorted, includes 220 Ω)  

### Miscellaneous
- ✅ Passive & active buzzers (2+2x)  
- ✅ Various sensors (temperature, light, etc.)  
- Caps (10x 6×6 mm tactile caps)  

---
  
<p align="center">
  <img src="https://github.com/user-attachments/assets/c91c5757-9f6c-4a9a-9716-8a39a1fd7029" alt="IMG_4974" width="600" height="600">
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
