import time
from arduino import Arduino
from data_extraction import *
from file_processing import save_to_file, read_and_combine_data
from file_processing import process_file
from plot import plot, plot_combined_data
title_name = "s10_230"
save_path = "test"
# save_path = r'C:\Users\kwjay\Documents\GitHub\Controller\data\signal_filter\data\\' + title_name
def run():
    arduino = Arduino()
    arduino.connect('COM7', 115200)
    time.sleep(2)
    arduino.write('1\n')
    arduino.write('200\n')
    arduino.write('3\n')
    data = extract_data(arduino, 3)
    arduino.write('3\n')
    arduino.write('1\n')
    arduino.write('0\n')
    arduino.disconnect()
    save_to_file(save_path, data)

def run_plus(tempo:str):
    arduino = Arduino()
    arduino.connect('COM7', 115200)
    time.sleep(2)
    arduino.write('1\n')
    arduino.write(tempo + '\n')
    data_str = extract_data(arduino, 3)
    data = [float(freq.split()[0]) for freq in data_str]
    arduino.write('1\n')
    arduino.write('0\n')
    arduino.disconnect()
    if len(data) == 0:
        return 0
    average = sum(data) / len(data)
    return average

def plotting():
    data = process_file(save_path)
    plot(data, save_path, 'xd')

def analise():
    data = []
    for i in range(130,148):
        print(i)
        new_data = run_plus(str(i))
        data.append(str(new_data))
        print(data)
    save_to_file('Characteristics', data)

run()
plotting()
# import os
# directory = r"C:\Users\kwjay\Documents\GitHub\Controller\data\ICR_prescaler\data"
# file_paths = [
#     os.path.join(directory, f)
#     for f in os.listdir(directory)
#     if f.startswith("p1_150") and os.path.isfile(os.path.join(directory, f))
# ]
# df = read_and_combine_data(*file_paths)
# plot_combined_data(df)