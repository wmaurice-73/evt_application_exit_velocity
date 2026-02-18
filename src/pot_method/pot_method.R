#install.packages("ReIns")
#install.packages("readxl")
#install.packages("ismev")
#install.packages("POT")
#install packages if required

library(ggplot2)
library(ismev)
library(ReIns)
library(readxl)
library(POT)

#this file contains the POT application 
#install and import the required packages. The first few lines import the data
#the relative path should work if you downloaded the entire github repo
#if you cannot find the ev_combined_R.csv file using this script, change the path to where you store this file
#the rest of this file then does all the calculations


df <- read.csv2(
  #change the file path according to where you store EV_combined_R.csv
  "../data/processed/ev_combined_R.csv",
  header = TRUE,
  stringsAsFactors = FALSE
)

#transform the data into a numeric vector such that the ismev package can work with it
data = as.numeric((df[[1]]))

#plot the mean excess to pick theshold, to obtain a continuous version of the plot, use the mean_excess_plot.py file
MeanExcess(data, xlim = c(108,120),ylim = c(1,4))
#the mean excess function suggests to pick the threshold 114.75
u = 114.75

#number of data larger than the threshold
n = sum(data > u)

#fitting a gpd and plotting diagnostics, we have 2478/11 = 225 observations per year
gp_fit = gpd.fit(xdat = data, threshold = u, show = F, npy = 225)

#extract the fitted parameters
gamma = gp_fit$mle[2]
sigma = gp_fit$mle[1]

print(paste("The fitted parameters are: gamma =", gamma, "and sigma =", sigma))

#force that the return period diagnostics plot is labeled with integers
options(scipen = 999)

#plotting diagnostics
gpd.diag(gp_fit)

#calculate confidence bounds for the shape parameter gamma
gamma_uci = gamma + 1.96*sqrt(((1+gamma)^2)/n)
gamma_lci = gamma - 1.96*sqrt(((1+gamma)^2)/n)

print(paste("The 0.95 confidence interval for gamma is:(",gamma_lci,",",gamma_uci,")"))

#Next we calculate the estimated asymptotic variance to estimate confidence bound
#Minv is the Matrix M^{-1} from Theorem 4.5
Minv <- matrix(c((1+gamma)^2, -(1+gamma)*sigma, -(1+gamma)*sigma, 2*(1+gamma)*sigma^2), nrow = 2, ncol = 2, byrow = TRUE)
print(Minv)
#grad is the gradient from Theorem 4.7
grad <- c(sigma / (gamma^2), -1 / gamma)
print(grad)

#calculate the standarderror from grad and Minv
var = grad %*% Minv%*% grad
se = sqrt(var/n)
print(paste("The standard error can be estimated with: ",se))

#estimated endpoint
endpoint = u - sigma/gamma
print(paste("The endpoint estimate is given by: ",endpoint))

#upper 95% confidence bound of the endpoint
ci_e = endpoint + 1.96*se
print(paste("The upper 0.95 confidence bound for the endpoint is given by: ",ci_e))

