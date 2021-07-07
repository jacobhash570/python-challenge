import os
import csv

election_data_csv_path = os.path.join("Resources", "election_data.csv")

with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(csv_header)
        


