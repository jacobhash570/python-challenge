import os
import csv

months = []

month_count = 0

os.chdir(os.path.dirname(__file__))

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #print(csv_header)

    for row in csv_reader:
        month_count += 1

        print (month_count)