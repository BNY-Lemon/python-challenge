# Dependencies
import os
import csv

#create path to file
budget_data_filepath =  os.path.join("Resources","budget_data.csv")

# What we are looking for
total_months = 0
total = 0.00
profit_loss_list = []
monthly_change = []
previous_month = 0.00
greatest_increase = {}
greatest_decrease = {}

def Average(custom_list):
	sum_var = 0
	for i in range(len(custom_list)):
		sum_var += custom_list[i]
	return sum_var / len(custom_list)

# Read csv
with open(budget_data_filepath) as csv_file:
	#create csv reader
	csv_reader = csv.reader(csv_file)
	next(csv_reader, None)
	# print the csv reader object
	for row in csv_reader:
		current_month = int(row[1])
		total_months += 1
		total += current_month
		profit_loss_list.append(int(row[1]))
		current_change = current_month - previous_month
		monthly_change.append(current_change)
		previous_month = current_month
		if total_months == 1:
			greatest_increase['Month'] = row[0]
			greatest_increase['Value'] = current_change
			greatest_decrease['Month'] = row[0]
			greatest_decrease['Value'] = current_change
			del monthly_change[0]
		elif current_change > greatest_increase['Value']:
			greatest_increase['Month'] = row[0]
			greatest_increase['Value'] = current_change
		elif current_change < greatest_decrease['Value']:
			greatest_decrease['Month'] = row[0]
			greatest_decrease['Value'] = current_change

# Output
print_string = "Financial Analysis\n" \
	"----------------------------\n" \
	f"Total Months: {total_months}\n" \
	f"Total: ${total:.0f}\n" \
	f"Average Change: ${Average(monthly_change):.2f}\n" \
	f"Greatest Increase in Profits: {greatest_increase['Month']} (${greatest_increase['Value']:.0f})\n" \
	f"Greatest Decrease in Profits: {greatest_decrease['Month']} (${greatest_decrease['Value']:.0f})\n"

print(print_string)