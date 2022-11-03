This Simple Script reads the csv files in the csv Folder, for each csv present, it loops through each row and creates a json object then create a sha256 hash of the json object before adding it to the end of each row of each csv and then outputs each csv file in a output Folder.

Requirements Python 3

How to Run
git clone https://github.com/ibkay998/HNG-SHA256.git

put all the csv you want to generate hash for in the csv folder

Ensure your csv file is of the format
Serial Number,Filename,Description,Gender,UUID
otherwise it will not give you the correct response

type in the console "python main.py"
your output folder should have the updated csv