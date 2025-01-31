import serial
from serial import SerialException

class Arduino:
    def __init__(self) -> None:
        self.arduino = None
        self.baudrate = None
    def connect(self, port: str, baudrate: int) -> None | SerialException:
        try:
            self.arduino = serial.Serial(port, self.baudrate, timeout=1)
            return None
        except serial.SerialException as error:
            return error

    def read(self) -> str | None:
        return self.arduino.readline().decode('utf-8').strip()

    def write(self, data: str) -> None:
        self.arduino.write(data.encode())