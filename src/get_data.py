#All imports used
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import unicodedata
import numpy as np 
import matplotlib.pyplot as plt
import os

raw_folder = os.path.join("data", "raw")

#URL Scraping for Player Stats
#Stores url
URL = "https://www.nbastuffer.com/2025-2026-nba-player-stats/"

#Sends the request and and gets the html
response = requests.get(URL)

#Allows for page to be searched
soup = BeautifulSoup(response.text, "html.parser")

#Looks for table then tr on the web page
table = soup.find("table")
rows = table.find_all("tr")

#Empty list to store the data
data = []

#For loop to get the data
for row in rows:
    cols = [c.get_text(strip = True) for c in row.find_all(["td", "th"])] #Gets the data and strips white space
    data.append(cols) #Adds the new data in 

#First row as headers and the rest become entries
Stats = pd.DataFrame(data[1:], columns = data[0])

#Saves as a csv
Stats.to_csv(os.path.join(raw_folder, "25_26_NBA_Stats_Table.csv"), index = False)

#CSV for Salaries
#Reads the csv
Salaries = pd.read_csv(os.path.join(raw_folder, "NBA_Salaries.csv"))

#Renames the columns
Salaries.rename(columns = {"Player": "NAME", "Tm": "TEAM"}, inplace = True)

#Drops the future salary columns
Salaries.drop(columns = ["2026-27", "2027-28", "2028-29", "2029-30","2030-31", "Guaranteed"], inplace = True)

#Gets rid of accents and special charcaters
Salaries["NAME"] = Salaries["NAME"].apply(
    lambda x:unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode("ascii"))

#Changes name so they can match
Salaries["NAME"] = Salaries["NAME"].replace("OG Anunoby", "O.G. Anunoby")
Salaries["NAME"] = Salaries["NAME"].replace("Robert Williams", "Robert Williams III")
Salaries["NAME"] = Salaries["NAME"].replace("Alex Sarr", "Alexandre Sarr")
Salaries["NAME"] = Salaries["NAME"].replace("Ron Holland", "Ronald Holland II")
Salaries["NAME"] = Salaries["NAME"].replace("Walter Clayton", "Walter Clayton Jr.")
Salaries["NAME"] = Salaries["NAME"].replace("Tristan Da Silva", "Tristan da Silva")
Salaries["NAME"] = Salaries["NAME"].replace("DaRon Holmes", "DaRon Holmes II")
Salaries["NAME"] = Salaries["NAME"].replace("Xavier Tillman Sr.", "Xavier Tillman")
Salaries["NAME"] = Salaries["NAME"].replace("GG Jackson II", "GG Jackson")
Salaries["NAME"] = Salaries["NAME"].replace("Craig Porter Jr.", "Craig Porter")

#Prints the table
print(Salaries)

#Combine the two tables
#Merges the two tables based on name 
Merged_Data = pd.merge(Stats, Salaries, on = "NAME", how = "right")

#Saves to csv
Merged_Data.to_csv(os.path.join(raw_folder,"Combined_25_26_Stats_And_Salaries.csv"), index = False)