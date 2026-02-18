import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np

#This file is the implementation of the semi - parametric procedure

#this function calculates the moment estimator for a given k with data df
def moment_estimator(k: int, df: pd.DataFrame):
    n = len(df)
    
    #select the relevant values and convert to float
    values = df.iloc[n-k-1:n]
    
    #take logarithms
    logs = np.log(values)
    
    #differences from the smallest value (logs[0])
    diffs = logs[1:] - logs.iloc[0] 
    
    # M_n^(1) and M_n^(2)
    Mn1 = np.mean(diffs)
    Mn2 = np.mean(diffs**2)
    
    #calculate the actual moment estimator
    yM = Mn1 + 1 - 0.5 * (1 / (1 - (Mn1**2 / Mn2)))
    
    return float(yM)

#The location estimator is simply the order statistic X_{n-k,n}
def location_estimator(k: int, df: pd.DataFrame):
    n = len(df)
    return float(df.iloc[n-k-1,0])

#this function calculates the scale estimator for given k with data df 
def scale_estimator(k: int, df: pd.DataFrame):
    n = len(df)
    
    #select the relevant values and convert to float
    values = df.iloc[n-k-1:n]
    
    #take logarithms
    logs = np.log(values)
    
    #differences from the smallest value (logs[0])
    diffs = logs[1:] - logs.iloc[0] 
    
    # M_n^(1) and M_n^(2)
    Mn1 = np.mean(diffs)
    Mn2 = np.mean(diffs**2)

    gammahat = 1 - 0.5 * (1 / (1 - (Mn1**2 / Mn2)))
    orderstat = float(df.iloc[n-k-1,0])

    return float(orderstat*Mn1*(1-gammahat))

#combining everything to calculate the endpoint estimator
def endpoint_estimator(k: int, df: pd.DataFrame):
    return location_estimator(k, df) - (scale_estimator(k,df)/moment_estimator(k,df))

#calculates the approximative variance of the endpoint estimator for given shape and scale parameters 
def var_ee_fixed_parameters(gamma: float, scale: float):
    return ((scale**2)*((1-gamma)**2)*(1-3*gamma+4*gamma**2))/((gamma**4)*(1-2*gamma)*(1-3*gamma)*(1-4*gamma))

#calculates the endpoint estimator for fixed gamma but scale and location still depening on k
def endpoint_estimator_fixed_gamma(k: int, gamma: int, df: pd.DataFrame):
    return location_estimator(k, df) - (scale_estimator(k,df)/gamma)

#print the moment_estimator against k, with k between kmin% and kmax% of the sample size 
#ylim is the range that will be displayed
def me_plot(kmin: float, kmax:float, df: pd.DataFrame, ylim: tuple | None = None):
    #calculation of moment estimator for varying k happens here
    x = np.arange(int(math.ceil(kmin*len(df))), int(kmax*math.ceil(len(df))),1)
    plt.figure()
    y1 = [moment_estimator(xi,df) for xi in x]
    plt.plot(x,y1,lw=0.6, color = 'black')
    
    plt.xlabel("k")
    plt.ylabel(r'$\hat{\gamma}_M$', rotation = 0, labelpad=10)
    if ylim is not None:
        plt.ylim(ylim)
    plt.show()

#print the moment_estimator for k being in between kmin% and kmax% of the sample size and the chosen estimator (median), here called mediangamma
#ylim is the range that will be displayed
def me_plot_ce(kmin: float, kmax:float, df: pd.DataFrame, mediangamma: float, ylim: tuple | None = None):
    #calculation of moment estimator for varying k happens here
    x = np.arange(int(math.ceil(kmin*len(df))), int(kmax*math.ceil(len(df))),1)
    plt.figure()
    y1 = [moment_estimator(xi,df) for xi in x]
    plt.plot(x,y1,lw = 0.8, color = 'black')
    #print a horizontal line at the height of mediangamma
    plt.axhline(
        y=mediangamma,
        lw=0.6,
        linestyle='--',
        color='dimgrey')

    plt.xlabel("k")
    plt.ylabel(r'$\hat{\gamma}_M$', rotation = 0, labelpad=10)
    if ylim is not None:
        plt.ylim(ylim)
    plt.tick_params(axis='both', labelsize=7)
    #uncomment the following line if you want to save the image
    #plt.savefig("me_plot.pdf", bbox_inches="tight")
    plt.show()

#print the endpoint_estimator for k being in between kmin% and kmax% of the sample size and using fixed gamma
def ee_plot_fixed_gamma(kmin:float, kmax:float, gamma: int, df: pd.DataFrame, ylim: tuple | None = None):
    x = np.arange(int(math.ceil(kmin*len(df))), int(kmax*math.ceil(len(df))),1)
    plt.figure()
    y1 = [endpoint_estimator_fixed_gamma(xi, gamma, df) for xi in x]
    plt.plot(x,y1, color = "black", lw = 0.8)
    if ylim is not None:
        plt.ylim(ylim)
    plt.tick_params(axis='both', labelsize=7)
    #uncomment the following line if you want to save the image
    #plt.savefig("ee_plot_ce.pdf", bbox_inches="tight")
    plt.show()

#print the endpoint_estimator for k being in between kmin% and kmax% of the sample size and using fixed gamma
#and also plot the chosen estimate which is the median of all estimates for ks chosen between klower and kupper
def ee_plot_fixed_gamma_ce(kmin:float, kmax:float, gamma: int, medianendpoint: float, df: pd.DataFrame, ylim: tuple | None = None):
    x = np.arange(int(math.ceil(kmin*len(df))), int(kmax*math.ceil(len(df))),1)
    plt.figure()
    y1 = [endpoint_estimator_fixed_gamma(xi, gamma, df) for xi in x]
    plt.plot(x,y1, color = "black", lw = 0.8)
    if ylim is not None:
        plt.ylim(ylim)
    plt.axhline(
        y=medianendpoint,
        lw=0.5,
        linestyle='--',
        color='dimgrey')
    plt.tick_params(axis='both', labelsize=7)
    #uncomment the following line if you want to save the image
    #plt.savefig("ee_plot_ce.pdf", bbox_inches="tight")
    plt.show()

#compare the endpoint estimation results for using a fixed gamma vs k being varied also for the moment estimator
def ee_plot_compare_fixed_gamma(kmin:float, kmax:float, fix:float, df: pd.DataFrame, ylim: tuple | None = None):
    x = np.arange(int(math.ceil(kmin*len(df))), int(kmax*math.ceil(len(df))),1)
    plt.figure()
    #calculate endpoint for varying k as well as for fixed gamma
    y1 = [endpoint_estimator_fixed_gamma(xi,fix,df) for xi in x]
    y2 = [endpoint_estimator(xi, df) for xi in x]
    plt.plot(x,y1, color = "black", lw = 0.6)
    plt.plot(x,y2, color = "black", linestyle = "--", lw = 0.6)
    if ylim is not None:
        plt.ylim(ylim)
    plt.tick_params(axis='both', labelsize=7)
    #uncomment the following line if you want to save the image
    #plt.savefig("eecompare.pdf", bbox_inches="tight")
    plt.show()


#load the combined and smooth data. The csv file can be generated using the combine_and_smooth file
df_25_sorted = pd.read_csv("./data/processed/ev_combined_python.csv")

#Moment estimator plot against k
me_plot(0.001,0.25,df_25_sorted,(-0.45,0.05))
           
#create the median of gamma over some number of ks, here ranging from 115 to 200 since the me_plot looks stable in that region
ks = np.arange(115, 200) 
x = np.array([moment_estimator(k, df_25_sorted) for k in ks])
mediangamma = np.median(x) 
print("The median estimate for the moment estimator is given by: " + str(mediangamma)) #-0.2308862817137589

#Moment estimator plot against k but also displaying the chosen estimate
me_plot_ce(0.001,0.25,df_25_sorted,mediangamma,(-0.45,0.05))


#plot the endpoint estimator for runnning k versus taking our fixed median estimate
ee_plot_compare_fixed_gamma(0.01,0.2,mediangamma,df_25_sorted,(120,130))

#plot the endpoint estimator using the fixed mediangamma, the plot stabilizes for k = 107
ee_plot_fixed_gamma(0.01,0.25,mediangamma,df_25_sorted,(120,130))

#calculate the mean endpoint in the chosen interval 107 to 190
ks_endpoint = np.arange(107,190)
y = np.array([endpoint_estimator_fixed_gamma(k,mediangamma, df_25_sorted) for k in ks_endpoint])
medianendpoint = np.median(y)
print("The median of the endpoint estimates is given by: " + str(medianendpoint)) #124.7137107826764

#endpoint estimate plot for median gamma with chosen median endpoint estimate
ee_plot_fixed_gamma_ce(0.01,0.2,mediangamma,medianendpoint, df_25_sorted,(120,130))

#calculate the scale estimator for k = 136
scale = scale_estimator(136,df_25_sorted)
print("The scale estimate is given by: " + str(scale)) #2.2023574649550923

#calculate the standarderror using the mediangamma estimate
se = math.sqrt(var_ee_fixed_parameters(mediangamma, scale)/136)
print("The standard error using the fixed mediangamma estimate is given by: " + str(se)) #2.759392291561523

#calcuate the standarderror using moment estimator with k = 136 
se_2 = math.sqrt(var_ee_fixed_parameters(moment_estimator(136,df_25_sorted), scale)/136)
print("The standard error using the moment estimator is given by: " + str(se_2)) #2.5643850886638475

#give upper confidence bound for fixed estimate of gamma
upperbound = medianendpoint + 1.96*se
print("The upper 0.95 confidence bound using the fixed mediangamma estimate is given by: " + str(upperbound)) #130.122119674137

#give upper confidence bound for moment estimator with k = 136
upperbound_2 = medianendpoint + 1.96*se_2
print("The upper 0.95 confidence bound using the moment estimator is given by: " + str(upperbound_2)) #129.73990555645753
