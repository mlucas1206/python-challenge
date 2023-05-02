#Import libraries
import os, csv

#set path
budgetpath = os.path.join('Resources','budget_data.csv')

#--------------------------

#read csv file and place content in variables
with open(budgetpath, 'r') as budgetfile:
    budget_iter = csv.reader(budgetfile, delimiter=',')
    
    #header skip
    header = next(budget_iter)

    #transfer to lists
    budgetlist = []
    for x in budget_iter:
        budgetlist.append(x)

#--------------------------

#grab months and total profit
#number of months
period = len(budgetlist)

#net total amount of Proft/Loss
netincome = 0
for x in budgetlist:
    netincome += int(x[1])

#changes in profits or loss average (end value - begin value)/length
average = (int(budgetlist[(period-1)][1]) - int(budgetlist[0][1]))/(period-1)

#--------------------------

#greatest inc/dec
prev = int(budgetlist[0][1]) #this is previous amount variable. Used first row amount
change = [] #make a list of inc/dec

#fill list of inc/dec
for x in budgetlist:
   change.append(int(x[1]) - prev)
   prev = int(x[1])

#pull greatest inc/dec details
inc = max(change)
dec = min(change)

   #grab date by indexing amounts (list[row][column])
inc_date = budgetlist[change.index(inc)][0]
dec_date = budgetlist[change.index(dec)][0]

#--------------------------

#print results
result = (f'Financial Analysis\n\
----------------------------\n\
Total Months: {period}\n\
Total: ${netincome}\n\
Average Change: ${round(average,2)}\n\
Greatest Increase in Profits: {inc_date} (${inc})\n\
Greatest Decrease in Profits: {dec_date} (${dec})')
print(result)

#--------------------------

#create new txt file and place results
with open('analysis/results.txt', 'w') as txtfile:
    txtfile.write(result)
