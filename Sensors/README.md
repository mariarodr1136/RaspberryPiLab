# Sensors

This section contains examples of reading sensor data and displaying information using Raspberry Pi GPIO pins and an LCD. Each script demonstrates how to interface with different types of sensors and output devices.

## Included Scripts

- **echoLocation.py** – Measures distance using an ultrasonic sensor (HC-SR04).  
- **tiltTest.py** – Detects tilt motion using a tilt sensor.  
- **sos.py** – Calculates the speed of sound in miles per hour (MPH) using timing data from an ultrasonic sensor (HC-SR04).  
- **pir-motion.py** – Detects motion using a Passive Infrared (PIR) sensor and prints alerts in real time.  
- **lcdDisplay.py** – Demonstrates how to display text on an I2C LCD1602 screen. Continuously prints messages like "Hello, World!" and "RPi LCD1602".  
- **LCD1602.py** – Provides low-level functions to control an LCD1602 via I2C, including initialization, writing text, clearing the screen, and enabling the backlight.  
- **tempLCD.py** – Reads temperature and humidity from a DHT11 sensor and displays the values on the LCD1602. Includes a button to switch between Celsius and Fahrenheit modes.  
- **tempHumidity.py** – Reads temperature and humidity from a DHT11 sensor and prints the values to the terminal.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/c30a05f2-884c-4a36-9dce-bc1718a4a768" alt="IMG_4979" width="600" height="700">
</p>

---

## Concepts Covered

- Reading digital input values from sensors  
- Measuring distance using sound waves  
- Detecting tilt and motion  
- Sensor calibration and real-time data reading  
- Displaying information on an I2C LCD screen  
- Switching between measurement modes (Celsius/Fahrenheit) using a button  

## Hardware Needed

- HC-SR04 ultrasonic distance sensor  
- Tilt switch sensor  
- PIR motion sensor  
- DHT11 temperature and humidity sensor  
- LCD1602 I2C display  
- Breadboard and jumper wires  
- Push button (for switching temperature units in `tempLCD.py`)

