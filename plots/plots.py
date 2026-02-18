import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genextreme
from scipy.stats import genpareto

#The code from here until line 55 generates the Figure showing the green excesses over a threshold
#generate some "data"
x = np.arange(1, 11)
values = np.array([2.1, 3.4, 1.8, 6.9, 8.3, 2.7, 10.1, 3.0, 4.4, 6.8])
u = 4.5

fig, ax = plt.subplots(figsize=(8, 4))

#vertical lines (oberservations)
for xi, v in zip(x, values):
    ax.vlines(xi, 0, v, linewidth=1, color="0.5")

#threshold line
ax.axhline(u, linestyle="-", linewidth=0.5, color="black")
ax.text(0.2, u, "u", va="center")


#calculate number of exceedences
exceed_idx = [i for i, v in zip(x, values) if v > u]
Nu = len(exceed_idx)

#draw excesses green
k = 0
for xi, v in zip(x, values):
    if v > u:
        k += 1
        ax.vlines(xi, u, v, linewidth=3, color="green")

        label = f"$Y_{{{k}}}$"

        ax.text(xi - 0.1, (u + v) / 2,
                label,
                ha="right", va="center")

#mae axes and texts look clean
for xi, v in zip(x, values):
    ax.text(xi, v + 0.15, f"$X_{{{xi}}}$", ha="center", va="bottom")

ax.set_xticks([])
ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xlim(0.5, 10.5)
ax.set_ylim(0, max(values) + 1)

plt.tight_layout()
#uncomment the next line if you want to save the figure
#plt.savefig("./plots/exceedances.pdf", bbox_inches="tight")
#plt.show()


#The code from here until line 80 plots gev densities for frechet, gumbel and weibull case
# Common parameters
mu = 0     #location
sigma = 1  #scale

#x-axis for plotting
x = np.linspace(-5, 5, 500)
#shape parameters
xis = [0.5, 0, -0.5]
labels = [r'$\gamma=0.5$ (Fréchet)', r'$\gamma=0$ (Gumbel)', r'$\gamma=-0.5$ (Weibull)']
linestyles = ['-', '--', ':']
colors = ['black', 'dimgrey', 'grey']  # grayscale

plt.figure(figsize=(8,5))

for xi, label, ls, color in zip(xis, labels, linestyles, colors):
    pdf = genextreme.pdf(x, c=-xi, loc=mu, scale=sigma)  # SciPy uses c=-xi
    plt.plot(x, pdf, label=label, color=color, lw=1, linestyle=ls)

plt.legend()
plt.grid(True)
#uncomment the next line if you want to save the plot
#plt.savefig("./plots/densities_gev.pdf", bbox_inches="tight")
#plt.show()


#The code from here until line 106 plots different densitites corresponding to the weibull case
# Common parameters
mu = 0     # location
sigma = 1  # scale

# x-axis for plotting
x = np.linspace(-5, 5, 500)

#shape parameters
xis = [-0.1, -0.5,-1]
labels = [r'$\gamma=-0.1$', r'$\gamma=-0.5$', r'$\gamma=-1$']
linestyles = ['-', '--', ':']
colors = ['black', 'dimgrey', 'grey']  # grayscale

plt.figure(figsize=(8,5))

for xi, label, ls, color in zip(xis, labels, linestyles, colors):
    pdf = genextreme.pdf(x, c=-xi, loc=mu, scale=sigma)  # SciPy uses c=-xi
    plt.plot(x, pdf, label=label, color=color, lw=1, linestyle=ls)

plt.legend()
plt.grid(True)
#uncomment the next line if you want to save the plot
#plt.savefig("./plots/densities_weibull.pdf", bbox_inches="tight")
#plt.show()



#The code from here until line 134  plots different GPD densities
# Shape and scale parameters
xis = [-0.5, -0.5, -0.25, -0.25]
scales = [1, 2, 1, 2]
labels = [r'$\gamma=-0.5, \sigma=1$', r'$\gamma=-0.5, \sigma=2$', 
          r'$\gamma=-0.25, \sigma=1$', r'$\gamma=-0.25, \sigma=2$']
linestyles = ['-', '--', '-.', ':']
colors = ['black', 'black', 'grey', 'grey']

plt.figure(figsize=(8,5))

for xi, sigma, label, ls, color in zip(xis, scales, labels, linestyles, colors):
    # GPD support: x in [0, -sigma/xi] for xi < 0
    x_max = -sigma/xi  # xi < 0
    x = np.linspace(0, x_max, 500)
    
    pdf = genpareto.pdf(x, c=xi, scale=sigma)
    plt.plot(x, pdf, label=label, color=color, lw=1, linestyle=ls)

plt.legend()
plt.xlim(0,8)
plt.grid(True)
plt.tight_layout()
#uncomment the next line if you want to save the plot
#plt.savefig("./plots/densitites_gpd.pdf", bbox_inches="tight")
plt.show()