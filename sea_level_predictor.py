import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(df['Year'].min(), 2051)
    y_values = [intercept + slope * x for x in x_values]
    plt.plot(x_values, y_values, color='red', label='Line of Best Fit')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_values_recent = range(df_recent['Year'].min(), 2051)
    y_values_recent = [intercept_recent + slope_recent * x for x in x_values_recent]
    plt.plot(x_values_recent, y_values_recent, color='green', label='Recent Line of Best Fit')




    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()