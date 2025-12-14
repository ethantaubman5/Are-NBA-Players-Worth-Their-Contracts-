#Data Analysis
#All imports used
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import unicodedata
import numpy as np 
import matplotlib.pyplot as plt

#Defines folders
processed_folder = os.path.join("data", "processed")
file_path = os.path.join(processed_folder, "Final_Combined_25_26_Stats_And_Salaries.csv")
#Loads the csv
adding = pd.read_csv("Final_Combined_25_26_Stats_And_Salaries.csv")

#Creates the performance metric
adding["PERFORMANCE"] = (
    (1 * adding["PpG"]) 
    + (1.2 * adding["ApG"])
    + (0.8 * adding["RpG"]) 
    + (2 * adding["SpG"])
    + (2 * adding["BpG"]) 
    + (0.15 * adding["ORtg"])
    - (0.10 * adding["DRtg"])
    + (5 * adding["TS%"])
    + (4 * adding["eFG%"])
    - (2 * adding["TOpG"]) 
) * (adding["GP"] / adding["GP"].max()) * (adding["MpG"] / adding["MpG"].max())

#Creates efficiency metric
adding["EFFICIENCY"] = adding["PERFORMANCE"] / (adding["SALARY"] / 1000000)

#Descriptive stats are shown 
adding.describe()

#Creates z score
adding["PERF_Z"] = (adding["PERFORMANCE"] - adding["PERFORMANCE"].mean()) / adding["PERFORMANCE"].std()

#Modeling for the expected salary
adding["LOG_SALARY"] = np.log(adding["SALARY"])
m, b = np.polyfit(adding["PERFORMANCE"], adding["LOG_SALARY"], 1)

#Gets the expected salary
adding["EXPECTED_SALARY"] = np.exp(m * adding["PERFORMANCE"] + b)

#Creates the value metric
adding["VALUE"] = adding["SALARY"] - adding["EXPECTED_SALARY"]

#Rounds all the metrics
adding["PERFORMANCE"] = adding["PERFORMANCE"].round(3)
adding["EFFICIENCY"] = adding["EFFICIENCY"].round(3)
adding["EXPECTED_SALARY"] = adding["EXPECTED_SALARY"].round(3)
adding["VALUE"] = adding["VALUE"].round(3)
adding["PERF_Z"] = adding["PERF_Z"].round(3)

#Prints the new table
print(adding)

#Saves to csv
adding.to_csv(file_path, index = False)