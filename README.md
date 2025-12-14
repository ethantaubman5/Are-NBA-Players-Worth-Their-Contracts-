# Are-NBA-Players-Worth-Their-Contracts-?
## Team Members:
- Ethan Taubman, Github Username: ethantaubman5

## Project Description
This project aims to analyze whether NBA players contracts are overpaid or underpaid by comparing the player's salary with basic and advanced basketball metrics during the 2025-26 season. The goal of this project is to identify if the individual player is overpaid or underpaid and to see on team level to see if players together are overpaid or underpaid. 

## Virtual Environment Setup
- 1.) Open command prompt 
- 2.) Make sure Python is downloaded by typing python --version (if not download the latest version from the Python website)
- 3.) Download the githib repository by downloading in the zip from GitHub
- 4.) Check where the downloaded zip is located
- 5.) Move the zip file to a folder you can easily access
- 6.) Then click extract all
- 7.) Navigate to the main folder and copy the address of the project and then type "cd" then copied address

## Create a Virtual Environment
- 1.) Create the virtual environment by typing in the command prompt "python -m venv venv"
- 2.) Activate the virtual environment by typing in the command prompt "venv\Scripts\activate"
- 3.) Install the required packages by typing in the command prompt "pip install -r requirements.txt"
- 4.) When you are done working type "deactivate" in the command prompt

## Data Folders
- "data/raw/" contains the raw dataset of the salaries and stats of the players
- "data/processed/" contains the cleaned and merged dataset of salaries and stats for each player

## Running the code
- 1.) Once you finished the first steps you can type "python src/get_data.py" (This gets the data of the salaries and stats and merging them together. Also gets the data into data/raw/)
- 2.) Then type "python src/clean_data.py" (This cleans merged dataset while also putting it in data/processed/) 
- 3.) Then type "python src/run_analysis.py" (Computes the new metrics of performance, efficiency, expected salary and value)
- 4.) Then type "python src/visualize_results.py" (Displays the visualizations of the scatterplot, bar charts, and histogram)
- 5.) Click the X button on top of the visualization to go to the next visualization (there are only 6 graphs)
