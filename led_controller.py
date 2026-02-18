import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import json
import os

# --- Config path setup ---
APP_NAME = "KLTechnology"
APP_FOLDER = "LEDController"

appdata_path = os.path.join(
    os.getenv("LOCALAPPDATA"),
    APP_NAME,
    APP_FOLDER
)

os.makedirs(appdata_path, exist_ok=True)

CONFIG_FILE = os.path.join(appdata_path, "config.json")

ser = None  # global serial object

# --- Load/save config ---
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

config = load_config()

# --- Serial functions ---
def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def connect_serial(auto=False):
    global ser, config
    port = port_var.get()
    baud = baud_var.get()

    if not port:
        if not auto:  # only show message if not auto-connecting
            messagebox.showerror("Error", "Select a COM port first")
        return

    try:
        ser = serial.Serial(port, baud, timeout=1)
        if not auto:
            messagebox.showinfo("Connected", f"Connected to {port} at {baud} baud")

        # Enable controls
        brightness_slider.config(state="normal")
        btn_on.config(state="normal")
        btn_off.config(state="normal")

        # Save config
        config["port"] = port
        config["baud"] = baud
        save_config(config)

        # Apply last brightness if available
        if "brightness" in config:
            brightness_slider.set(config["brightness"])
            send_command(f"BRIGHTNESS {config['brightness']}")

    except Exception as e:
        if not auto:
            messagebox.showerror("Connection Failed", str(e))
        else:
            print("Auto-connect failed:", e)

def send_command(cmd):
    global ser, config
    if ser and ser.is_open:
        ser.write((cmd + "\n").encode("utf-8"))
    else:
        print("Not connected, ignoring command:", cmd)

def set_brightness(value):
    val = int(float(value))
    send_command(f"BRIGHTNESS {val}")
    # Save brightness
    config["brightness"] = val
    save_config(config)

# --- GUI Setup ---
root = tk.Tk()
root.title("WS2812B LED Controller")
root.geometry("400x400")
root.resizable(False, False)

# COM Port selection
tk.Label(root, text="COM Port:").pack(pady=5)
port_var = tk.StringVar()
port_combo = ttk.Combobox(root, textvariable=port_var, values=list_serial_ports())
port_combo.pack()

# Set last used port if available
if "port" in config:
    port_var.set(config["port"])

# Refresh COM ports button
def refresh_ports():
    port_combo["values"] = list_serial_ports()
tk.Button(root, text="Refresh Ports", command=refresh_ports).pack(pady=2) 

# Baud rate selection
tk.Label(root, text="Baud Rate:").pack(pady=5)
baud_var = tk.IntVar(value=config.get("baud", 115200))
baud_combo = ttk.Combobox(root, textvariable=baud_var, values=[9600, 115200])
baud_combo.pack()

# Connect button
tk.Button(root, text="Connect", command=connect_serial).pack(pady=10)

# ON/OFF buttons
frame = tk.Frame(root)
frame.pack(pady=10)
btn_on = tk.Button(frame, text="Turn ON", width=10, command=lambda: send_command("ON"), state="disabled")
btn_on.grid(row=0, column=0, padx=5)
btn_off = tk.Button(frame, text="Turn OFF", width=10, command=lambda: send_command("OFF"), state="disabled")
btn_off.grid(row=0, column=1, padx=5)

# Brightness slider
tk.Label(root, text="Brightness:").pack(pady=5)
brightness_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", command=set_brightness, state="disabled")
brightness_slider.pack(fill="x", padx=20, pady=10)

# Auto-connect if config exists
if "port" in config and "baud" in config:
    root.after(100, lambda: connect_serial(auto=True))

# --- Add bottom-left label ---
footer_label = tk.Label(root, text="© 2025, KLTECHNOLOGY | LED CONTROLLER", font=("Arial", 10))
footer_label.pack(side="bottom", anchor="w", padx=10, pady=5)

root.mainloop()
