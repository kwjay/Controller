import time
from arduino import Arduino
from data_extraction import *
from file_processing import save_to_file, read_and_combine_data
from file_processing import process_file
from plot import plot, plot_combined_data
# title_name = "p07i0005d01_200"
title_name = "pid_200v10"
# # save_path = "test"
save_path = r'C:\Users\kwjay\Documents\GitHub\Controller\data\pid\data\on_load\PP\\' + title_name
def run():
    arduino = Arduino()
    arduino.connect('COM7', 115200)
    time.sleep(2)
    arduino.write('2\n')
    arduino.write('1\n')
    arduino.write('200\n')
    data = extract_data(arduino, 30)
    time.sleep(1)
    arduino.write('2\n')
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

def plotting(given_path):
    data = process_file(given_path)
    plot(data, given_path, 'xd', y_bottom=0, y_top=700)

def analise():
    data = []
    for i in range(130,148):
        print(i)
        new_data = run_plus(str(i))
        data.append(str(new_data))
        print(data)
    save_to_file('Characteristics', data)

run()
plotting(save_path)
# save_path = r'C:\Users\kwjay\Documents\GitHub\Controller\data\pid\data\\' + title_name
# plotting(save_path)
# title_name = "p05i0d0_230"
# save_path = r'C:\Users\kwjay\Documents\GitHub\Controller\data\pid\data\\' + title_name
# plotting(save_path)
# title_name = "p1i0d0_230"
# save_path = r'C:\Users\kwjay\Documents\GitHub\Controller\data\pid\data\\' + title_name
# plotting(save_path)
# import os
# directory = r"C:\Users\kwjay\Documents\GitHub\Controller\data\ICR_prescaler\data"
# file_paths = [
#     os.path.join(directory, f)
#     for f in os.listdir(directory)
#     if f.startswith("p1_150") and os.path.isfile(os.path.join(directory, f))
# ]
# df = read_and_combine_data(*file_paths)
# plot_combined_data(df)