# CP210x USB UART Bridge Blink Test

This Python script is designed to check if a CP210x USB UART Bridge is alive by blinking its associated LED. The script communicates with the bridge over a serial connection and toggles the LED on and off in a loop.

## Requirements

- Python 3
- PySerial library (`pip install pyserial`)
- CP210x USB UART Bridge connected to the specified serial port

## Usage

replace the tty device name /dev/ttyUSB0

tty name can be found using: plug your device and run the command sudo dmesg 

Install the PySerial library:

   ```bash
   pip install pyserial


