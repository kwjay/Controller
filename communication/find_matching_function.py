import numpy as np
import matplotlib.pyplot as plt

def process_characteristics(file_path):
    x = np.array([])
    y = np.array([])
    with open(file_path, 'r') as file:
        data = file.readlines()
        for i in range(128 ,len(data)):
            x = np.append(x, i)
            print(x)
            y = np.append(y, float(data[i]))

    coeffs = np.polyfit(x, y, 1)
    poly_func = np.poly1d(coeffs)

    # Generate fitted values
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = poly_func(x_fit)

    # Plot
    plt.scatter(x, y, label="Original Data")
    plt.plot(x_fit, y_fit, label=f"Poly Fit: {poly_func}", color="red")
    plt.legend()
    plt.show()
process_characteristics("Characteristics")