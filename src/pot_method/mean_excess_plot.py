import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import genpareto
from matplotlib.ticker import MultipleLocator

#define the mean excess function
def mean_excess(df: pd.DataFrame, u:float):
    return np.mean(df[df > u]-u)

#apply the mean excess function to our data
df_25_sorted = pd.read_csv("./data/processed/ev_combined_python.csv")

#evaluate the mean excess function for an interval of threshhold values u
u_vals = np.arange(110, 120, 0.01)
y = [mean_excess(df_25_sorted,u) for u in u_vals]

#plot the mean excess function against u
plt.plot(u_vals, y,lw=0.6, color = "black")
plt.xticks(np.arange(110, 120, 1))
# Set minor ticks (invisible markers) at 0.25 distance
ax = plt.gca() # Get Current Axis
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
# Turn on the grid for the x-axis
plt.grid(axis='x', which='both', linestyle='-', alpha=0.5)
plt.grid(True)
plt.show()


