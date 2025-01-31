import serial
from serial import SerialException

class Arduino:
    def __init__(self) -> None:
        self.arduino = None
    def connect(self, port: str, baudrate: int) -> None | SerialException:
        try:
            self.arduino = serial.Serial(port, baudrate, timeout=1)
            return None
        except serial.SerialException as error:
            return error

    def disconnect(self) -> None:
        self.arduino.close()

    def ready(self) -> bool:
        return self.arduino.in_waiting > 0
    def read(self) -> str | None:
        return self.arduino.readline().decode('utf-8').strip()

    def write(self, data: str) -> None:
        self.arduino.write(data.encode())