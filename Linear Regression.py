                                                             # SIMPLE LINEAR REGRESSION

# x = size of the house  (independent variable)
# y = cost of the house  (dependent variable)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import prettytable as tab

# Function to estimate coefficients (slope and intercept)
def estimate_coefficients(x, y):
    n = np.size(x)  # Get the number of data points
    mean_x, mean_y = np.mean(x), np.mean(y)  # Calculate the mean (average) of x and y
    SS_xy = np.sum(x * y) - n * mean_x * mean_y  # Sum of the product of deviations of x and y from their means
    SS_xx = np.sum(x * x) - n * mean_x * mean_x  # Sum of the square of deviations of x from its mean
    b1 = SS_xy / SS_xx  # Calculate the slope of the regression line
    b0 = mean_y - b1 * mean_x  # Calculate the intercept of the regression line
    return b0, b1  # Return the intercept and slope

# Function to plot regression line and table
def plot_regression_line_and_table(x, y, b):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})
    # Create a figure and two subplots. ax1 is for the plot, ax2 is for the regression results
    # figsize=(10, 8) sets the size of the figure
    # gridspec_kw={'height_ratios': [3, 1]} sets the relative height of the subplots (3 for the plot, 1 for the results)

    ax1.scatter(x, y, color='r', marker="o")  # Create a scatter plot of x vs y with red circles
    y_pred = b[0] + b[1] * x  # Calculate the predicted y values using the regression equation
    ax1.plot(x, y_pred, color='g')  # Plot the regression line in green
    ax1.set_xlabel('Size')  # Label the x-axis as "Size"
    ax1.set_ylabel('Cost')  # Label the y-axis as "Cost"
    ax1.set_title('Regression Line')  # Set the title of the plot

    ss_tot = np.sum((y - np.mean(y))**2)  # Total sum of squares (variation of y values from their mean)
    ss_res = np.sum((y - y_pred)**2)  # Residual sum of squares (variation of y values from the regression line)
    r_squared = 1 - (ss_res / ss_tot)  # Calculate the R-squared value, which indicates how well the regression line fits the data

    # Create a string containing the regression results
    regression_results = (
        f'Regression Results:\n\n'
        f'R-squared: {r_squared:.4f}\n'
        f'b0 (intercept): {b[0]:.4f}\n'
        f'b1 (slope): {b[1]:.4f}\n'
        f'Regression equation: y = {b[0]:.4f} + {b[1]:.4f}x'
    )
    
    ax2.axis('off')  # Hide the axes of the second subplot
    ax2.text(0.5, 0.5, regression_results, ha='center', va='center', fontsize=12, bbox=dict(facecolor='wheat', alpha=0.5))
    # Display the regression results in the second subplot, centered with a wheat-colored background

    plt.tight_layout()  # Adjust the layout to prevent overlap
    plt.show()  # Display the plot

     # Display data table using PrettyTable
    table = tab.PrettyTable()
    table.field_names = ["Size (x)", "Cost (y)"]  # Define the column headers
    for size, cost in zip(x, y):
        table.add_row([size, cost])  # Add each data point as a row in the table

    print("\nData Table:\n")
    print(table)  # Print the table

# Function to read CSV data
def read_csv_data(file_path):
    df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
    x = df['Size'].values  # Extract the 'Size' column as a numpy array
    y = df['Cost'].values  # Extract the 'Cost' column as a numpy array
    return x, y  # Return the x and y arrays

# Main execution block
if __name__ == "__main__":
    csv_file_path = input("Please enter the path to your CSV file: ")  # Ask the user to input the path to the CSV file
    
    try:
        x, y = read_csv_data(csv_file_path)  # Read the data from the CSV file
        b = estimate_coefficients(x, y)  # Estimate the regression coefficients
        plot_regression_line_and_table(x, y, b)  # Plot the regression line and display the results
    except FileNotFoundError:  # Handle the error if the file is not found
        print(f"Error: The file '{csv_file_path}' was not found.")
    except pd.errors.EmptyDataError:  # Handle the error if the CSV file is empty
        print(f"Error: The file '{csv_file_path}' is empty.")
    except KeyError as e:  # Handle the error if a required column is missing
        print(f"Error: The column {e} is missing in the CSV file.")
    except Exception as e:  # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")






