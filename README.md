# EVT Application – Exit Velocity

This repository contains all code used for my master's thesis, in which I apply Extreme Value Theory (EVT) to estimate the maximum exit velocity possibly achievable in baseball.

---

## Data

The `data/` folder contains:

- **Raw data**  
  Downloaded from: https://baseballsavant.mlb.com/  
  Includes all batters with at least one batted ball event per season  
  Seasons covered: **2015–2025**

- **Processed data**  
  Generated using:
```
  data_processing/process.py
```

  The processed dataset contains only the **maximum exit velocity per player** over the observed time period.

---

## Methods

### 1. Peaks Over Threshold (POT) Method

- File: `pot_method.R`
- Uses processed data
- Estimates the right endpoint via the **Peaks Over Threshold (POT)** approach
- Threshold selection via empirical **Mean Excess Plot**

Since the built-in R function `MeanExcess()` produces only a discrete plot,
the file
```
mean_excess_plot.py
```

can be used to generate a continuous version.

---

### 2. Semi-Parametric Method

- File: `semi_parametric_method.py`
- Uses the **moment estimator** for the shape parameter
- Produces diagnostic plots:
  - Selection of appropriate k values
  - Final endpoint estimates

---

### 3. Additional Plots

- File: `plots.py`
- Generates all thesis figures outside of Chapter 6

---

## Installation & Setup (Python)

Clone the repository and open the project folder in your IDE.

### 1. Create a virtual environment
```bash
python -m venv venv
```

### 2. Activate the environment

**Windows:**
```bash
venv/Scripts/activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```
