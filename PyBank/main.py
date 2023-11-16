#Imported the modules that are going to be needed for this challenge
import os
import csv

#Set the path to be able to use the CSV file
budget_csv = os.path.join("Resources","budget_data.csv")

#Set the variables that are going to be used later 
total_net = 0
total_months = 0
change_list = []
greatest_increase_change = 0
greatest_increase_change_month = ""
greatest_decrease_change = 0
greatest_decrease_change_month = ""

#Opened up the CSV file, set the encoder, and also set the split to be able differentiate the rows
with open(budget_csv, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        #Set date equal to row 0 and set the profit loss to row 1 and set it to be an int
        #Having the total net equal the profit loss plus the total net to be able to find the total at the end of the script
        #Total months = total months plus 1 makes it so that we can find the total amount of months 
        date = row[0]
        profit_loss = int(row[1])
        total_net = total_net + profit_loss
        total_months = total_months + 1
        
        #With this if statement if the total months are greater than one the net change equals the profit loss - previous profit loss
        #That is done so that we can find the greatest increase and the greatest decrease
        if(total_months > 1):
            net_change = profit_loss - previous_profit_loss
            change_list.append(net_change)

            #Having the greatest increase change compared to the net change and if the net change is greater it changes the greatest increase change to equal the net change
            #Then the greatest increase change month equal the date to be able to tie the month to the change
            if(net_change > greatest_increase_change):
                greatest_increase_change = net_change
                greatest_increase_change_month = date
            
            #Having the greatest decrease change compared to the net change and if the net change is greater it changes the greatest decrease change to equal the net change
            #Then have the greatest decrease change month equal the date to be able to tie the month to the change
            if (net_change < greatest_decrease_change):
                greatest_decrease_change = net_change
                greatest_decrease_change_month = date
        
        #Set the prvious loss to the profit loss to be able to have it loop in the with statement
        previous_profit_loss = profit_loss

    #Setting the average change by suming the change list and then taking then taking the whole list and dividing by the list
    average_change = sum(change_list) / len(change_list)

    #Priting the end result of it all to make sure that it works before it is written down on a txt file
    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Month: {total_months}')
    print(f'Total Net: {total_net}')
    print(f'Average Change: {average_change:.2f}')
    print(f'({greatest_increase_change_month}) ${greatest_increase_change}')
    print(f'({greatest_increase_change_month}) ${greatest_increase_change}')

#Set the path for the txt file to be written in 
output_path = os.path.join("Analysis","Analysis.txt")

#Set the path to be used to write the txt file
with open(output_path, 'w') as txtfile:

    #Writing to the txt file with the end results
    txtfile.write('Finacial Analysis\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Month: {total_months}\n')
    txtfile.write(f'Total Net: {total_net}\n')
    txtfile.write(f'Average Change: {average_change:.2f}\n')
    txtfile.write(f'({greatest_increase_change_month}) ${greatest_increase_change}\n')
    txtfile.write(f'({greatest_increase_change_month}) ${greatest_increase_change}\n')
