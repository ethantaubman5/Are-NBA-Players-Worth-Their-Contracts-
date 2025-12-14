#Filtering min games
#Min games set to 5
min_game = 5

#Creates the filter
filtered = adding[adding["GP"] >= min_game]

#Data visualization Scatter Plot
#Creates the scatter plot
scatter = plt.scatter(
    filtered["PERFORMANCE"], filtered["SALARY"], c = filtered["VALUE"], s = filtered["GP"] * 5, cmap = "RdYlGn", alpha = 0.7)

#Creates the color bar 
plt.colorbar(scatter, label = "Contract Value")

#Gives the title and axis label
plt.title("Player Performance Vs. Salary")
plt.xlabel("Performance Score")
plt.ylabel("Salary")

#Adjusts the spacing automatically
plt.tight_layout()

#Displays the graph
plt.show()

#Data visualization Histogram of player distrbution
#Creats histogram
plt.hist(filtered["VALUE"], bins = 30, edgecolor = "black", alpha = 0.7, density = False)

#Creates a line at 0 
plt.axvline(0, color = "black", linestyle = "--")

#Gives the chart a title and axis labels
plt.title("Distribution of Player Value")
plt.xlabel("Overpaid is Positive and Underpaid is Negative")
plt.ylabel("Value")

#Adjusts the spacing automatically
plt.tight_layout()

#Displays the graph
plt.show()

#Visualization Bargraph of top 10 overpaid and underpaid
#Creates the top 10 overpaid players 
top_overpaid = filtered.sort_values("VALUE", ascending = False).head(10)

#Creates the bar graph
plt.barh(top_overpaid["NAME"], top_overpaid["VALUE"], edgecolor = "black")

#Gets the highest value at the top
plt.gca().invert_yaxis()

#Creates the title and axis labels
plt.title("Top 10 Overpaid Players")
plt.xlabel("Value")

#Adjusts the spacing automatically
plt.tight_layout()

#Displays the graph
plt.show()

#Creates top 10 underpaid players
top_underpaid = filtered.sort_values("VALUE").head(10)

#Creats bar graph
plt.barh(top_underpaid["NAME"], top_underpaid["VALUE"], edgecolor = "black")

#Gets the lowest value on top
plt.gca().invert_yaxis()

#Gets the title and axis labels
plt.title("Top 10 Overpaid Players")
plt.xlabel("Value")


#Adjusts the spacing automatically
plt.tight_layout()

#Displays the graph
plt.show()

#Visualization Boxplot of positions by value
#Sets up the positions for the box plot
positions = sorted(filtered["POS"].unique())
data_to_plot = [filtered[filtered["POS"] == pos]["VALUE"] for pos in positions]

#Creates the boxplot
plt.boxplot(data_to_plot, tick_labels = positions)

#Creates the title and axis labels
plt.title("Player Value by Position")
plt.xlabel("Position")
plt.ylabel("Value")

#Adjusts the spacing automatically
plt.tight_layout()

#Displays the graph
plt.show()

#Visualization Barchart showing team value
#Sets up team value
team_value = filtered.groupby("TEAM")["VALUE"].sum().reset_index()
team_value = team_value.sort_values("VALUE", ascending = False)

#Generates the bar graph
plt.barh(team_value["TEAM"], team_value["VALUE"], edgecolor = "black")

#Gets the highest value on top
plt.gca().invert_yaxis()

#Gets the titles and axis labels
plt.title("Total Player Value by Team")
plt.xlabel("Total Team Value")
plt.ylabel("Team")

#Adjusts the spacing automatically
plt.tight_layout()

#Displays the graph
plt.show()