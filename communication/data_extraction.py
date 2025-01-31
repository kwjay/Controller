from arduino import Arduino
import time

def extract_data(arduino: Arduino, run_time=5) -> list:
    data = []
    time_end = time.time() + run_time
    while time.time() < time_end:
        if arduino.ready():
            data.append(arduino.read())
    return data