import matplotlib.pyplot as plt
import pandas as pd

def plot(data: pd, save_path:str, title_name:str, color='b', y_bottom=0, y_top=700,) -> str:
    plt.figure(figsize=(8, 6))
    plt.plot(data["TIME"], data["FREQUENCY"], color, label="signal", marker="", )
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.ylim(y_bottom,y_top)
    plt.title(title_name)
    plt.grid(True)
    # plt.savefig(save_path)
    plt.show()
    return save_path

def plot_combined_data(df):
    plt.figure(figsize=(10, 6))
    for col in df.columns:  # Skip 'X' column
        plt.plot(df['X'], df[col], label=col, marker="")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.ylim(140, 180)
    plt.title("Compare")
    plt.grid(True)
    plt.show()