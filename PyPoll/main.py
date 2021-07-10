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
    #print(votes)

    for canditae in votes:
       
        first = format((canditae[0][1])*100/(sum(count.values())))
        second = format((canditae[1][1])*100/(sum(count.values())))
        third = format((canditae[2][1])*100/(sum(count.values())))
        fourth = format((canditae[3][1])*100/(sum(count.values())))

    print(first)
    print(second)
    print(third)
    print(fourth)
        


