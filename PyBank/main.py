# Python Challenge - Week 3

# Import Modules
import os
import csv

# Set path for bduget_data.csv
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Declare variables and initialize
months = 0
total = 0
change = 0
greatinc = 0
greatdec = 0
greatincmon = ""
greatdecmon = ""


# Read in csv file
with open(budget_csv, 'r') as csvfile:

    # Split the data with commas delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set header
    header = next(csvreader)

    # Loop through data
    for row in csvreader:

        # Read in the current month and profit/loss
        curmon = str(row[0])
        curpl = int(row[1])

        # Count total months
        months += 1

        # Add profit/losses to total
        total += curpl

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average Change: $")
print("Greatest Increase in Profits:")
print("Greatest Decrease in Profits:")