import serial
import time

def blink_test():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600)

        for i in range(25):
            ser.write(b'1')  # Assuming '1' toggles the LED, modify if needed
            time.sleep(0.1)
            ser.write(b'0')
            time.sleep(0.1)
            print(f"\rBlink {i + 1}", end='', flush=True)

        print("\nScript executed successfully. CP210x USB UART Bridge is alive (:")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    blink_test()
