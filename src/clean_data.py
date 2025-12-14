#Cleaning the table
#Reads csv
clean = pd.read_csv("Combined_25_26_Stats_And_Salaries.csv")

#Drops the columns that duplicated or not needed
clean.drop(columns = ["TEAM_x", "CUR", "RANK", "Rk"], inplace = True)

#Renames columns
clean.rename(columns = {"TEAM_y": "TEAM", "2025-26": "SALARY"}, inplace = True)

#Removes the dollar sign and commas in salary
clean["SALARY"] = (
    clean["SALARY"]
    .astype(str)
    .str.replace("$", "", regex = False)
    .str.replace(",", "", regex = False))

#If there is no data fill it with 0
clean = clean.fillna(0)

#If position is 0 then put as inactive
clean.loc[clean["POS"] == 0, "POS"] = "INACTIVE"

#Deletes the first damian lillard
clean = clean[~((clean["NAME"] == "Damian Lillard") & (clean["TEAM"] == "MIL"))]

#Adds salary to the players with no salaries but has stats
clean.loc[clean["NAME"] == "Jeremiah Robinson-Earl", "SALARY"] = "2305852"
clean.loc[clean["NAME"] == "Damian Lillard", "SALARY"] = "36620603"
clean.loc[clean["NAME"] == "Chris Livingston", "SALARY"] = "636434"

#Removes duplicates
clean = clean.drop_duplicates()

#Orders the table for better reading
clean = clean[["NAME", "TEAM", "POS", "SALARY"] + clean.columns.difference(["NAME", "TEAM", "POS", "SALARY"]).tolist()]

#Saves as a csv 
clean.to_csv("Final_Combined_25_26_Stats_And_Salaries.csv", index = False)
