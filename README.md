# CP210x USB UART Bridge Blink Test

This Python script is designed to check if a CP210x USB UART Bridge is alive by blinking its associated LED. The script communicates with the bridge over a serial connection and toggles the LED on and off in a loop.

## Requirements

- Python 3
- PySerial library (`pip install pyserial`)
- CP210x USB UART Bridge connected to the specified serial port

## Usage

1. Install the PySerial library:

   ```bash
   pip install pyserial
   ```bash

   1. replace the tty device name /dev/ttyUSB0
   tty name can be checked using ```bash sudo dmesg ```bash
