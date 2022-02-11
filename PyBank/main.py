#import file

import os
import csv
#path to the csvfile
csvpath = os.path.join('budget_data.csv')
#initializing the variables 
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0
# Open the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# calculating the total number of months and total revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Calculate change from this month to previous months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #calculating the greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]
            
        #calculating the greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]  
      
    # calculating the average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # printing all values
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print('Average Change: ${:.2f}'.format(average_change))
    print(f"Greatest increase in profits: {greatest_inc_month} ${max(changes)}")
    print(f"Greatest decrease in profits: {greatest_dec_month} ${min(changes)}")


#Exported txt file
output_file = os.path.join('Fin_Analysis.txt')
PyBank = open(output_file,"w+")
PyBank.write("Financial Analysis")
PyBank.write('\n'+"---------------------------------")
PyBank.write('\n'+f"Total Months: {total_months}")
PyBank.write('\n'+f"Total Amount: ${total_revenue}")
PyBank.write('\n'+'Average Change: ${:.2f}'.format(average_change))
PyBank.write('\n'+f"Greatest increase in profits:  {greatest_inc_month} ${max(changes)}")
PyBank.write('\n'+f"Greatest decrease in profits:  {greatest_dec_month} ${min(changes)}")

 
    