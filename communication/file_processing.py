import pandas as pd

def process_file(file_path: str) -> pd:
    with open(file_path, "r") as file:
        raw_data = file.readlines()
        data = []
        for row in raw_data:
            print(row)
            data_row = row.strip().split(" ")
            if len(data_row) == 2:
                frequency, time = data_row
                data.append({
                    "FREQUENCY": float(frequency),
                    "TIME": int(time)
                })
    return pd.DataFrame(data)

def save_to_file(file_path: str, data: list) -> str:
    with open(file_path, "w") as file:
        file.writelines(f"{line}\n" for line in data[:-1])
        file.write(data[-1])
    return file_path


def read_and_combine_data(*file_paths):
    combined_df = pd.DataFrame()
    print(file_paths)
    for file_path in file_paths:
        data = []
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split()  # Split by spaces
                    try:
                        x_val = float(parts[0])  # First value as float
                        y_val = int(parts[1])  # Second value as int
                        data.append((x_val, y_val))
                    except (ValueError, IndexError):
                        print(f"Skipping invalid line in {file_path}: {line}")

        # Convert to DataFrame
        df = pd.DataFrame(data, columns=['X', file_path])

        # Merge data based on X values
        if combined_df.empty:
            combined_df = df
        else:
            combined_df = pd.merge(combined_df, df, on='X', how='outer')

    return combined_df