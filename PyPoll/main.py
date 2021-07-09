import os
import csv

votes_candidates = []

election_data_csv_path = os.path.join("Resources", "election_data.csv")

with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(csv_header)
    
    for row in csv_reader:
        votes_candidates.append(row[2])

    sorted_candiates = sorted(votes_candidates)
    print(sorted_candiates)
        


