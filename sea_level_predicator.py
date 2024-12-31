import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_predicted1 = slope1 * years_extended + intercept1
    plt.plot(years_extended, sea_level_predicted1, color="red", label="Best fit line: 1880-2050")

    # Create second line of best fit using data from year 2000
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = pd.Series(range(2000, 2051))
    sea_level_predicted2 = slope2 * years_2000 + intercept2
    plt.plot(years_2000, sea_level_predicted2, color="green", label="Best fit line: 2000-2050")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data
    plt.savefig("sea_level_plot.png")
    return plt.gca()
