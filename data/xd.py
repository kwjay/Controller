
import matplotlib.pyplot as plt
import numpy as np

# List the names of your data files here.
path = r"pid\\data\\on_load\\PlA\\no_pid_200v7"
second_path = r"pid\\data\\on_load\\PLA\\pid_200v10"
file_names = [ path, second_path]
plt.figure(figsize=(10, 6))


for file in file_names:
    try:
        # Load the data from the file.
        # Each file is assumed to have at least one column:
        # Column 0: Frequency in Hz
        data = np.loadtxt(file, usecols=(0, 1))
    except Exception as e:
        print(f"Error loading {file}: {e}")
        continue

    # Ensure data is two-dimensional even if there is only one row.
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # Extract the frequency values from the first column.
    frequency = data[:, 0]

    # Filter out consecutive duplicate frequency values.
    # Create a mask that is True for the first value and for any value that differs from its immediate predecessor.
    if len(frequency) > 1:
        keep_mask = np.insert(np.diff(frequency) != 0, 0, True)
        frequency_filtered = frequency[keep_mask]
    else:
        frequency_filtered = frequency

    # Use array indices (after filtering) as "lp".
    lp = np.arange(len(frequency_filtered))
    if "no_pid" in file:
        label = "Sygnał bez regulacji"
    else:
        label = "Sygnał z regulacją PID"
    # Plot frequency vs. lp.
    plt.plot(lp, frequency_filtered, marker='', linestyle='-', label=label)
plt.axhline(y=315, color='red', linestyle='--', label='Oczekiwana częstotliwość')
# Customize the plot.
plt.xlim(right=5000, left=0)
plt.title("")
plt.xlabel("Lp")
plt.ylabel("Częstotliwość (Hz)")
plt.legend(loc='lower right')
plt.savefig("PID PLA")
plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
#
# # Sample data: two lists of float values.
# test_A = [80.423,75.136,74.510,72.706,78.877,71.589,75.203,76.337,77.214,77.715]
# test_B = [85.847,81.080,84.890,83.797,81.078,84.056,83.570,81.065,86.114,81.648]
#
#
#
# # Instead of computing the standard deviation from multiple measurements,
# # we define a fixed error of 0.01 for each bar.
# mean_A = np.mean(test_A)
# std_A  = np.std(test_A, ddof=1)
# mean_B = np.mean(test_B)
# std_B  = np.std(test_B, ddof=1)
#
# # Instrument error (fixed error of ±0.01 g)
# instrument_error = 0.01
#
# # Combine the instrument error and the standard deviation (assuming they are independent).
# # This gives the total error for each test.
# total_error_A = np.sqrt(std_A**2 + instrument_error**2)
# total_error_B = np.sqrt(std_B**2 + instrument_error**2)
#
# # Prepare the data for plotting.
# labels = ['Bez regulacji', 'Z regulacją']
# means  = [mean_A, mean_B]
# errors = [total_error_A, total_error_B]
#
# # Create positions for the bars.
# x_positions = np.arange(len(labels))
# bar_width = 0.4
#
# # Create the grouped bar chart.
# plt.figure(figsize=(8, 6))
# bars = plt.bar(x_positions, means, yerr=errors, width=bar_width,
#                capsize=10, color=['C0', 'C1'])
#
# # Customize the plot.
# plt.xticks(x_positions, labels)
# plt.xlabel('Wyniki dozowania PP')
# plt.ylabel('Waga (grams)')
# plt.title('')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.savefig('PP WEIGHT')
# plt.show()