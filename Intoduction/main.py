import numpy as np
import matplotlib.pyplot as plt


def analyze_data(data):
    # Convert the dictionary values to a NumPy array
    data_np = np.array(list(data.values()))

    # Calculate statistics
    stats = {
        'mean': np.mean(data_np),
        'median': np.median(data_np),
        'std_dev': np.std(data_np),
        'q1': np.percentile(data_np, 25),
        'q2': np.percentile(data_np, 50),  # Median
        'q3': np.percentile(data_np, 75),
    }

    # Calculate IQR and outliers
    iqr = stats['q3'] - stats['q1']
    lower_bound = stats['q1'] - 1.5 * iqr
    upper_bound = stats['q3'] + 1.5 * iqr
    stats['outliers'] = data_np[(data_np < lower_bound) | (data_np > upper_bound)]

    return stats


def visualize_data(data):
    # Convert the dictionary values to a NumPy array
    labels, values = zip(*data.items())

    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Bar Chart')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Plotting the histogram
    plt.subplot(1, 2, 2)
    plt.hist(values, bins=5, color='salmon', edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show both plots
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = {
        'A': 55, 'B': 65, 'C': 75, 'D': 85,
        'E': 95, 'F': 45, 'G': 60, 'H': 70,
        'I': 80, 'J': 90
    }

    analysis_results = analyze_data(data)
    print("Data Analysis Results:")
    for key, value in analysis_results.items():
        print(f"{key.capitalize()}: {value}")

    visualize_data(data)
