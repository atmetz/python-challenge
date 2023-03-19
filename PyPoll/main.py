# Python Challenge - Week 3 - PyPoll

# Import Modules
import os
import csv

# Set path for election_data.csv
polls_csv = os.path.join('Resources', 'election_data.csv')

# declare and initialize variables
total_votes = 0
candidates = []
candidates_percent = []
candidates_votes = []
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

        # Set caninlist to false
        caninlist = False

        # Increment total votes by 1
        total_votes += 1

        # Loop through candidates list
        for i in range(len(candidates)):

            # If the current candidate is in the list, increase their votes by 1
            if candidates[i] == curcand:
                candidates_votes[i] += 1
                caninlist = True

        # Check if candidate is in the list. If they are not, add to list
        if caninlist != True:
            candidates.append(curcand)
            candidates_percent.append(0)
            candidates_votes.append(1)

# Calculate percentage of votes for each candidate, and the winner based on number of votes
for x in range(len(candidates)):
    candidates_percent[x] = round(((candidates_votes[x] / total_votes) * 100),3)
    if candidates_votes[x] > candidates_votes[election_winner]:
        election_winner = x


# Print Results
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
# Loop through all candidates and print results
for y in range(len(candidates)):
    print(str(candidates[y]) + ": " + str(candidates_percent[y]) + "% (" + str(candidates_votes[y]) + ")")
print("--------------------------")
print("Winner: " + candidates[election_winner])
print("--------------------------")

# Set path for budget_data.csv
analysis_txt = os.path.join('Analysis', 'analysis.txt')

# Write to text file
with open(analysis_txt, 'w') as txtfile:
    # Print Results
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write("Total Votes: " + str(total_votes) + "\n")
    txtfile.write("--------------------------\n")
    # Loop through all candidates and print results
    for y in range(len(candidates)):
        txtfile.write(str(candidates[y]) + ": " + str(candidates_percent[y]) + "% (" + str(candidates_votes[y]) + ")\n")
    txtfile.write("--------------------------\n")
    txtfile.write("Winner: " + candidates[election_winner])