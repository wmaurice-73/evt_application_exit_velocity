# evt_application_exit_velocity
This repo contains all the code that was used for my master thesis, where I apply extreme value theory to estimate to maximum Exit Velocity possibly achievable.

The data folder contains the raw data taken from https://baseballsavant.mlb.com/, as well as the processed data. The processed data can be obtained using the process.py file from the data_processing folder.
The raw data contains information about batters with at least one batted ball event per season for each season from 2015 - 2025. 

The processed data only contains the best exit velocity each player has obtained within these years

The pot_method.R file uses the processed data to estimate the right endpoint of the data using the peaks over threshold approach. We chose a threshold via a graphical procedure, using the empirical mean excess plot.
Since the prebuilt R function MeanExcess only produces a discrete plot, one can use the mean_excess_plot.py file to generate the continuous plot appearing in the thesis.

The semi_parametric_method.py file  uses the processed data to estimate the right endpoint of the data using a semi-parametric approach. We use the moment estimator to estimate the shape parameter. The file also produces all the plots we used to choose ranges of k for our used estimators and to display our results.

The plots.py file produces all the figures appearing in the thesis outside of Chapter 6.

To make use of the python files, clone the repository and open the project folder in your IDE.
First, create a virtual environment
python -m venv venv
Then activate the environment using
venv\Scripts\activate
And lastly install all the required libraries
pip install -r requirements.txt

The pot_method.R file can be used without any further instructions. Just make sure you install the required libraries if necessary. The commands and the required libraries can be found within the file.
