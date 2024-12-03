import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Create first line of best fit (using all data)
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Predict sea level for all years up to 2050
    years_all = np.arange(1880, 2051)
    y_pred_all = fit1.intercept + fit1.slope * years_all

    # Create second line of best fit (using data from 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    fit2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    # Predict sea level from 2000 to 2050
    years_2000 = np.arange(2000, 2051)
    y_pred_2000 = fit2.intercept + fit2.slope * years_2000

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Plot the best fit lines
    plt.plot(years_all, y_pred_all, color='red', label="Fit (1880-2050)")
    plt.plot(years_2000, y_pred_2000, color='black', linestyle='--', label="Fit (2000-2050)")

    # Customize x-ticks
    plt.xticks(range(1850, 2075+1, 25))

    # Add legend
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()