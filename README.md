# python-challenge
PyBank:
The import os and import csv modules are going to be used through out the script
Set the path for the budget_csv by using the os module with os.path.join to be able to find the data that is being worked with

Set the variables for the script to be able to start with a base line, and to be able to have them set to have int, lists, str

Using a with statement to open up the path for the csv file, setting the encoder, and setting the variable to make it cleaner to read
With using the vairable from the with statement to be able to set the delimiter to be able to set rows moving forward
Set the header to not count it within the calculations moving onward
Starting with the row for loop to be able to have the date and the profit_loss to their respective rows within the CSV file
Using total_net we are able to combine the "profit_loss", so that later the total can be found

For the greatest increase change making sure that the net change is greater than it so that when it is no longer greater the highest number has been found, then it equal the net change 
During this if statement it also pairs it with the date attached to the greatest increase change by tying the greatest increase change month = date

For the greatest decrease change is similar to the increase but the net change is meant to be smaller than the greatest decrease change until there is nothing lower, then it equal the net change
During this if statement as before it also pair it with the date attached to the greatest increase change by tying the greatest decrease change month = date

Still within the for loop, setting the previous profit loss = profit loss to be able to have it loop within the statement to have it loop back to the for statement

Calculating the average change by equaling it to the sum of the change list divided by the len of the change list

Then printing out the results to find the total months, total net, average change to the 2nd decimal then the greatest increase and decrease change with their respective months
Printing it first to make sure that all is ran correctly before it has been writtent to the txt file

Set a path for the analysis text file to be written in using output_path as the variable

Set a with statement to have the path output_path used with the vairable txtfile

Then with using the txtfile.write and using the print portion of the code without the print function to make it consistent with the print function, but within the "" putting \n to be able to write it in the txt file and move it to the next line.

Py Poll:
The import os and import csv modules are going to be used through out the script
Set the path for the election_csv by using the os module with os.path.join to be able to find the data that is being worked with

Set the vairables for the script to be able to start with a base line, and to be able to have them set to have int, lists, str

Using a with statement to open up the election_csv path with encoder 'r' to set as csvfile
Setting csvreader to the path of csvfile to be able to set the delimiter to , so that the csv file can be split into rows in the later lines
header = next(csvreader) so that it doesnt use the headers within the csv file for the calculations later used
Using the for loop function for row within the csvreader (so that the header can be skipped) 

Then starting with gathering the total votes for the candidate within the row[2]

Using the if statment to be able to find the specific candidate within the list of candidates (as candidates = the list and the candidate is the str) adding 1 to the candidate to be able to count up the votes for that candidate and if the candidates dont equal by having a different candidate on the other side of the equal sign it sets it to the amount of votes that they had

Set print to push out the total votes to not interfere with the later calculations

With the next for loop using the candidate and votes to be able to set percentages to find the candidate with the highest percent of votes
The if statement following the for loop is used to find the highest percent of votes to be able to pair that with the respective winner

then setting another print for the winner to make sure all looks good before it is set to write to the txt file

Set a with statement to have the path output_path used with the vairable txtfile

Then with using the txtfile.write and using the print portion of the code without the print function to make it consistent with the print function, but within the "" putting \n to be able to write it in the txt file and move it to the next line.
