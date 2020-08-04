# Dependencies
import os
import csv

#create path to file
budget_data_filepath =  os.path.join("..","Resources","budget_data.csv")

#read csv
with open(budget_data_filepath) as csv_file:
	#create csv reader
	csv_reader = csv.reader(csv_file)
	# print the csv reader object
	for row in csv_reader:
		print(row)