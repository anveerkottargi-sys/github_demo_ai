import pandas as pd
import matplotlib.pyplot as plt

def plot_data(file_path):
    # Read the CSV file into a DataFrame and this is a csv file
    data = pd.read_csv(file_path)

    # Check if the necessary columns are present
    if 'x' not in data.columns or 'y' not in data.columns:
        
        return

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'], marker='o', linestyle='+')
    plt.title('Data Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()
