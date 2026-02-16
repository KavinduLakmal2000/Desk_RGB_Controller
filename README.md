# KL LED Desk Controller

A simple desktop LED controller built using **Arduino Pro Mini** and **WS2812B LED strip**, controlled via a custom Python desktop application.

This project allows you to:
- Turn LEDs ON / OFF
- Adjust brightness (0–255)
- Auto-connect to last used COM port
- Save settings locally

---

## 🖥 Software Features

- Windows desktop application (built with Tkinter)
- Serial communication using PySerial
- Brightness control slider
- Config file auto-save (`config.json`)
- Remembers last used COM port and brightness
- Clean and simple UI

---

## 🔌 Hardware Used

- Arduino Pro Mini (5V / 16MHz)
- WS2812B LED Strip
- USB to TTL Converter (FTDI / CH340 / CP2102)
- External 5V Power Supply (recommended for longer strips)

---

## 🧠 How It Works

The desktop application communicates with the Arduino over Serial.

Commands sent:

- `ON`
- `OFF`
- `BRIGHTNESS <value>`

Example:
The Arduino reads serial input and updates the LED strip accordingly.

👨‍💻 Author

KLTechnology
2025

![alt text](image.png)