## Chip-007 Project

### Description
This Simple Python Script reads the csv files in the csv folder and for each csv present, it loops through each row and creates a json object after which it then creates a sha256 hash of the json object before adding it to the end of each row of each csv and then outputs each csv file in a output folder.

### Requirements 
For this program to run all you need is Python 3

### How to Run
1. Clone the repository to your local machine.

2. Put all the csv you want to generate hash for in the csv folder.

3.Ensure your csv file is of the format Serial Number,Filename,Description,Gender,UUID as the top rows of the csv.
therwise it will not give you the correct response

4.Type in the console "python main.py".
5.The output folder should have the updated csv.

### References
If you need to see the schema of the csv check below.
- [Schema](https://docs.google.com/spreadsheets/d/1b5H3bp_9-YVjTYQNjLeokXJewrcPfgUo_MYvYXtaUno/edit#gid=0)

