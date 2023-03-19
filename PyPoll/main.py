# Python Challenge - Week 3 - PyPoll

# Import Modules
import os
import csv

# Set path for election_data.csv
polls_csv = os.path.join('Resources', 'election_data.csv')

# declare and initialize variables
total_votes = 0
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidates_percent = [0, 0, 0]
candidates_votes = [0, 0, 0]
election_winner = 0

# Read in csv file
with open(polls_csv, 'r') as csvfile:

    # Split the data with commas delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set header
    header = next(csvreader)

    # Loop through data
    for row in csvreader:

        # Read in the current candidate
        curcand = str(row[2])

        total_votes += 1

        for i in range(len(candidates)):

            if candidates[i] == curcand:
                candidates_votes[i] += 1

for x in range(len(candidates)):
    candidates_percent[x] = round(((candidates_votes[x] / total_votes) * 100),3)
    if candidates_votes[x] > candidates_votes[election_winner]:
        election_winner = x


# Print Results
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
for y in range(len(candidates)):

    print(str(candidates[y]) + ": " + str(candidates_percent[y]) + "% (" + str(candidates_votes[y]) + ")")
print("--------------------------")
print("Winner: " + candidates[election_winner])
print("--------------------------")