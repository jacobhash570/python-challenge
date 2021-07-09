import os
import csv
from typing import Counter

candidates = []
votes = []

election_data_csv_path = os.path.join("Resources", "election_data.csv")

with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(csv_header)
    
    for row in csv_reader:
        #print(row)
        candidates.append(row[2])

    sorted_candiates = sorted(candidates)
    #print(sorted_candiates)

    count = Counter(sorted_candiates)
    votes.append(count.most_common())
    print(votes)
        


