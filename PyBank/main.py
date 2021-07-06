import os
import csv

months = []
profit_loss_changes = []

month_count = 0
net_total = 0
previous_month = 0
current_month = 0
change = 0

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #print(csv_header)

    for row in csv_reader:
        # print(row)
        month_count += 1
        #print (month_count)

        current_month = int(row[1])
        net_total += current_month
        #print(current_month)

        if (month_count == 1):
            previous_month = current_month
            continue

        else: 
            change = current_month - previous_month

            months.append(row[0])
            #print(months)

            profit_loss_changes.append(change)
            #print(profit_loss_changes)

            previous_month = current_month

    sum_change = sum(profit_loss_changes)
    average_change = round(sum_change/(month_count - 1))
    #print(average_change)

    increase_change = max(profit_loss_changes)
    #print(increase_change)
    decrease_change = min(profit_loss_changes)
    #print(decrease_change)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {month_count}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Decrease: {increase_change}")
print(f"Greatest Decrease {decrease_change}")