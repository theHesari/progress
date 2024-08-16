## Data Analysis and Visualization

This project provides a Python script that performs basic statistical analysis on a given dataset and visualizes the results using bar charts and histograms. The script is designed to help users understand the distribution and key statistical properties of their data.

### Files in the Project

- **`main.py`**: The main Python script that contains the functions for data analysis and visualization.

### Features

1. **Statistical Analysis**: 
    - **Mean**: The average of all data points. It provides a central value that represents the dataset.
    - **Median**: The middle value when data points are sorted. It is useful for understanding the data's central tendency, especially when there are outliers.
    - **Standard Deviation (std_dev)**: Measures the dispersion of data points around the mean. A higher standard deviation indicates more spread out data.
    - **Quartiles (Q1, Q2, Q3)**: Values that divide the dataset into quarters. Q1 (25th percentile), Q2 (50th percentile, also the median), and Q3 (75th percentile) help in understanding the data distribution.
    - **Interquartile Range (IQR)**: The difference between Q3 and Q1. It is used to detect outliers in the dataset.
    - **Outliers**: Data points that fall below the lower bound or above the upper bound calculated using the IQR. Outliers can indicate variability in the data or errors.

2. **Data Visualization**:
    - **Bar Chart**: 
        - Displays the values associated with each category. 
        - Useful for comparing different categories directly.
    - **Histogram**: 
        - Shows the frequency distribution of the dataset.
        - Useful for understanding how data points are spread across different ranges.

### How to Use

1. **Install Dependencies**:
    - Ensure you have `numpy` and `matplotlib` installed:
      ```bash
      pip install -r requirements.txt
      ```

2. **Running the Script**:
    - You can run the script using:
      ```bash
      python main.py
      ```

3. **Output**:
    - The script will print the results of the statistical analysis, including the mean, median, standard deviation, quartiles, and outliers.
    - It will also display two plots:
      - A **Bar Chart** showing the values of each category.
      - A **Histogram** displaying the frequency distribution of the dataset.

## Sample Output

When you run the script with the provided sample data, the following output is generated:

### Data Analysis Results:

```plaintext
Mean: 72.0
Median: 72.5
Std_dev: 15.20
Q1: 61.25
Q2: 72.5
Q3: 83.75
Outliers: []
```

### Visual Output:

- **Bar Chart**: A bar chart visualizing the values of each category in the dataset.
- **Histogram**: A histogram showing the frequency distribution of the data points.

![visual output](Intoduction/main.py)
