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
            #adding a candidate to a candidate array if it is not there
            candidates.append(row[2])
            #initialize a candidate in the dictionnary with 0 votes 
            tracking_votes[row[2]] = 1
            total_votes += 1
        else:
            tracking_votes[row[2]] += 1
            total_votes += 1

tracking_votes["OTooley"] = tracking_votes.pop("O'Tooley")
winner = max(tracking_votes, key=tracking_votes.get)
# Output
print_string = "Election Results\n" \
	"-------------------------\n" \
    f"Total Votes: {total_votes}\n" \
    "-------------------------\n" \
    f"Khan: {(tracking_votes['Khan'] / total_votes):.3%} ({tracking_votes['Khan']})\n" \
    f"Correy: {(tracking_votes['Correy'] / total_votes):.3%} ({tracking_votes['Correy']})\n" \
    f"Li: {(tracking_votes['Li'] / total_votes):.3%} ({tracking_votes['Li']})\n" \
    f"O'Tooley: {(tracking_votes['OTooley'] / total_votes):.3%} ({tracking_votes['OTooley']})\n" \
    "-------------------------\n" \
    f"Winner: {winner}\n" \
    "-------------------------" 
    
    
print(print_string)

# Output to text file
with open(os.path.join("Analysis", "output.txt"), "w") as file:
	file.write(print_string)