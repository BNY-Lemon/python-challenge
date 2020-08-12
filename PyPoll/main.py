# Dependencies
import os
import csv

#create path to file
election_data_filepath =  os.path.join("Resources","election_data.csv")

# Looking for the following:
total_votes = 0
candidates = []
tracking_votes = {}

# Read csv
with open(election_data_filepath) as csv_file:
	#create csv reader
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
	# print the csv reader object
    for row in csv_reader:
        if row[2] not in tracking_votes.keys():
            #adding a candidate to a candidate arry if it is not there
            #candidates.append(row[2])
            #initialize a candidate in the dictionnary with 0 votes 
            tracking_votes[row[2]] = 1
            print(tracking_votes)
        else:
            tracking_votes[row[2]] += 1
            #print(tracking_votes)

# print(tracking_votes['Khan'])
# print(tracking_votes.keys())
# output to text file