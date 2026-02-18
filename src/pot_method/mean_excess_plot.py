import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import genpareto
from matplotlib.ticker import MultipleLocator

#we define the mean excess function
def mean_excess(df: pd.DataFrame, u:float):
    return np.mean(df[df > u]-u)

#apply the mean excess function to our data
df_25_sorted = pd.read_csv("./data/processed/ev_combined_python.csv")

#evaluate the mean excess function for an interval of threshhold values u
u_vals = np.arange(110, 120, 0.01)
y = [mean_excess(df_25_sorted,u) for u in u_vals]

#we plot the mean excess function against u
plt.plot(u_vals, y,lw=0.6, color = "black")
plt.xticks(np.arange(110, 120, 1))
# Set minor ticks (invisible markers) at 0.25 distance
ax = plt.gca() # Get Current Axis
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
# Turn on the grid for the x-axis, applying it to 'both' major and minor ticks
plt.grid(axis='x', which='both', linestyle='-', alpha=0.5)
plt.grid(True)
plt.show()

#we want to compare the if our choice of u supports the GPD model, hence we add a linear function y_linear = a*u + b to the plot
#y_linear schould have slope gamma(1-gamma), b has to be adjusted such that the line intersects the mean excess plot at the desired choice of u
a = -0.244  
b = 29.9
y_linear = a * u_vals + b

#plot both functions in one plot
plt.plot(u_vals, y_linear, lw=0.4, linestyle="--", color = "grey")
plt.plot(u_vals, y,lw=0.6, color = "black")
plt.xticks(np.arange(110, 120, 1))
# Set minor ticks (invisible markers) at 0.25 distance
ax = plt.gca() # Get Current Axis
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
# Turn on the grid for the x-axis, applying it to 'both' major and minor ticks
plt.grid(axis='x', which='both', linestyle='-', alpha=0.5)
plt.grid(True)
plt.tick_params(axis='both', labelsize=7)
#uncomment the next line if you want to save the plot
#plt.savefig("./src/pot_method/meanexcess_plot.pdf", bbox_inches="tight")
plt.show()
