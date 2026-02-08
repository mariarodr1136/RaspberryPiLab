
# Projects 🚨

This section features complete Raspberry Pi projects that integrate multiple sensors, actuators, and logic to demonstrate real-world embedded applications. Each project combines concepts from the **GPIO_Basics**, **Sensors**, and **ADC_Examples** sections, providing a bridge between experimentation and system-level prototyping.

---

## 🪴 LeafMedic: Embedded Computer Vision & Machine Learning System ([Full Project →](https://github.com/mariarodr1136/LeafMedic))

### 🔍 Overview

**LeafMedic** is an **edge AI application** for real-time plant disease detection, fully deployed on a **Raspberry Pi**. The system captures leaf images, preprocesses them dynamically, and runs an optimized **MobileNet model** with **TensorFlow Lite** for on-device inference. A **PyQt5 GUI** displays confidence-ranked predictions along with treatment recommendations, turning raw sensor input into actionable insights.

This project demonstrates **machine learning deployment**, **hardware-software integration**, and **production-oriented edge AI design** on embedded systems.

---

![plant_interface](https://github.com/user-attachments/assets/c501b2ca-56cf-416e-9695-41256759b555)

![raspberry_camera](https://github.com/user-attachments/assets/15d97414-3576-4c9f-a7a4-f7bfc30e8eaa)


---

### ⚙️ Features

* Real-time **plant disease detection** on Raspberry Pi using an optimized **MobileNet model**, achieving **90%+ classification accuracy** across 16 crops.  
* Integrated **camera acquisition**, **dynamic preprocessing**, and a **PyQt5 GUI** displaying predictions with treatment guidance.  
* Modular, **production-ready edge AI system** with fast (~145ms) inference and scalable architecture.  
* Supports batch processing of images for offline analysis.  
* Educational and extensible: learn embedded ML, computer vision, and GUI design.

---

### 🧠 Concepts Applied

* Embedded **machine learning deployment** with TensorFlow Lite  
* **Camera interfacing** and real-time image acquisition  
* Modular **software architecture** for scalable edge AI systems  
* **GUI development** using PyQt5 for real-time user feedback  
* On-device **preprocessing and inference optimization**  

---

### 🔌 Components

* **Raspberry Pi 4 Model B** (4GB recommended)  
* Camera Module (Arducam 5MP OV5647 or compatible)  
* Monitor or display for GUI (1200×800 recommended)  
* MicroSD card and 5V 3A power supply  
* Python libraries: `tensorflow`, `PyQt5`, `opencv-python`, `picamera2`, `numpy`

---

⭐ *Check out the full LeafMedic project here: [GitHub Repository →](https://github.com/mariarodr1136/LeafMedic)*

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

---

### 🧠 Concepts Applied

* GPIO input/output handling
* Analog sensor interfacing (LDR via ADC0834)
* Conditional logic combining multiple sensors
* Real-time signal monitoring and event-based control

---

### 🔌 Components

* Raspberry Pi 4 (or compatible model)
* PIR Motion Sensor (HC-SR501)
* Photoresistor (LDR)
* ADC0834 A/D converter
* Active buzzer or LED
* Breadboard and jumper wires

---

### 🧰 Circuit Schematic

![Screenshot 2025-11-13 at 2 04 27 PM](https://github.com/user-attachments/assets/d24910f3-d3f1-4f5a-bd85-091dc9dd6369)
> *Note: The motion detector (not shown) connects directly to 3V3, GPIO23, and GND*

---

## 🔐 Keypad-LCD Password Security System with Motion Sensor (`kpLib-thread-al.py`)

### 🔍 Overview

The **Keypad-LCD Password Security System with Motion Sensor** is an interactive authentication and monitoring project. It uses a **4×4 matrix keypad**, an **I2C LCD1602** display, and a **PIR motion sensor** to provide real-time alerts. Users can **arm**, **disarm**, or **change the password**, while the system continuously monitors for movement.

This project demonstrates **multi-component integration**, **threading**, **sensor monitoring**, and **user-interface design** for embedded systems.

---

https://github.com/user-attachments/assets/8592c76b-0675-4af8-9bb4-92534b10c209

---

### ⚙️ Features

* Continuously reads keypad input using a background **thread**
* Supports three command modes:

  * **A + password** → *ARM system* (displays **INTRUDER ALERT** if motion detected)
  * **B + password** → *DISARM system* (disables all sensors)
  * **C + password** → *ENTER PASSWORD CHANGE mode* (set a new custom password)
* Real-time motion detection using a **PIR sensor**
* Displays status and alerts on the **LCD1602**
* Responsive UI — screen updates immediately based on user input and sensor readings
* Clean program exit with `Ctrl+C` or `*` key

---

### 🧠 Concepts Applied

* Multithreading for non-blocking keypad input
* User authentication and state management
* LCD1602 text output and UI design
* Real-time embedded interaction loops
* Event-driven logic combining keypad input and motion sensor
* Basic GPIO input handling for PIR motion detection

---

### 🔌 Components

* Raspberry Pi 4 (or compatible model)
* 4×4 Matrix Keypad
* LCD1602 (I2C interface, address 0x27)
* PIR Motion Sensor (HC-SR501)
* Jumper wires & breadboard

---

⭐ *More projects will be added soon — stay tuned for IoT integration, remote monitoring, and camera-based automation systems!*
