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
- **Raspberry Pi 4 Model B** (4GB)

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
│   ├── blink_led.py
│   ├── button_input.py
│   └── README.md
│
├── Sensors/
│   ├── temperature_sensor.py
│   ├── light_sensor.py
│   └── README.md
│
├── ADC_Examples/
│   ├── ADC0834_example.py
│   ├── potentiometer_read.py
│   └── README.md
│
└── Projects/
    ├── rgb_led_controller.py
    ├── motion_alarm_system.py
    └── README.md
```

---

## ⚙️ Requirements

Make sure you have the following installed on your Raspberry Pi:

- Raspberry Pi OS 
- Python 3 (usually preinstalled)  
- `RPi.GPIO` or `gpiozero` module  
- `lgpio` (for advanced GPIO control)
- `time`, `os`, `sys` (standard libraries)

To install missing packages:
```bash
sudo apt update
sudo apt install python3-gpiozero
```

---

## 🚀 How to Run

1. Clone this repository:
```bash
git clone https://github.com/<your-username>/raspberry-pi-tutorials.git
cd raspberry-pi-tutorials
```

2. Open any tutorial folder, for example:
```bash
cd GPIO_Basics
```

3. Run the script with:
```bash
python3 blink_led.py
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
