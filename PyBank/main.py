import os
import csv

month_count = 0
net_total = 0
previous_month = 0
current_month = 0
change = 0

months = []
profit_loss_changes = []

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #print(csv_header)

    for row in csv_reader:
        print(row)
        month_count += 1

        #print (month_count)

        current_total = int(row[1])
        net_total += current_total

        #print(net_total)

        if (months == 1):
            previous_month = current_month
            continue

        else: 
            change = current_month - previous_month

            months.append(row[0])
            #print(months)

            profit_loss_changes.append(change)
            #print(profit_loss_changes)

            previous_month = current_month