import matplotlib.pyplot as plt
import pandas as pd

class Plotter:
    def __init__(self, input_path):
        self.input_path = input_path
    def process_file(self, file_path):
        with open(file_path, "r") as file:
            raw_data = file.readlines()
            data = []
            for row in raw_data:
                frequency, time = row.strip().split(" ")
                data.append({
                    "FREQUENCY": float(frequency),
                    "TIME": int(time)
                })
        return pd.DataFrame(data)