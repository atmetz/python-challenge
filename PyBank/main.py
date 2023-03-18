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
totchange = 0
greatinc = 0
greatdec = 0
prevpl = 0
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

        # Calculate monthly change
        change = prevpl - curpl

        totchange += change

        # Check for postive change
        if change >= 0:

            # Check if current months profit/loss is greater than the current greatest profit/loss
            if curpl > greatinc:

                # Set the current profit/loss as the greatest and the current month as the greatest month
                greatinc = curpl
                greatincmon = curmon

        else:

            # Check if current months profit/loss is greater than the current greatest profit/loss
            if curpl < greatdec:

                # Set the current profit/loss as the greatest and the current month as the greatest month
                greatdec = curpl
                greatdecmon = curmon

        # Set previous months profit/loss for comparison
        prevpl = curpl

# Calculate average monthly change
average = round((totchange / months), 2)

# Print Financial Analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + greatincmon + " ($" + str(greatinc) + ")")
print("Greatest Decrease in Profits: " + greatdecmon + " ($" + str(greatdec) + ")")