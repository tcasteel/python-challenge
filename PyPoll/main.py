#Import the modules that will be needed
import os
import csv

#Setting the path for the csv file
election_csv = os.path.join("Resources","election_data.csv")

#Setting the variables that are going to used
total_votes = 0
candidates = {}
winner_votes = 0
winner = ""

#Grabbed the csv file, and have it split to be able to differentiate the rows
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:

        #Having the total votes work with the candidates to be able to calculate who has the most votes
        total_votes = total_votes + 1
        candidate = row[2]

        #Setting an if statement for candidate within the list of candidates to be able to collect the votes for that specific candidate
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

#Did the first set of printing it out before moving on to the next set of calculations
print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------')

#Setting a for loop to be able to determine the percentages for the votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes})')

    #If statement to be able to tell the winner by the for loops percentages
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#Printing out the winner portion of the script now that the winner code is above, to make sure that its working before it gets written to the txt file
print('---------------------------')
print(f'Winner: {winner}')
print('---------------------------')

#Set the path for the txt file to be written in 
output_path = os.path.join('Analysis', 'Analysis.txt')

#Set the path to be used to write the txt file
with open(output_path, 'w') as txtfile:

    #Writing to the txt file with the end results
    txtfile.write('Election Results\n')
    txtfile.write('---------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('---------------------------\n')

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f'{candidate}: {percentage:.3f}% ({votes})\n')

    txtfile.write('---------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('---------------------------\n')
