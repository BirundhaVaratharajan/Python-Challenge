# Python script that analyzes the records to calculate each of the following values:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period
#--------------------------------------------------------------------------------------------------------
#import Directories
import os
import csv

Total_Months = 0
Net_Total_Profitloss = 0
Current_profitloss = 0
Prev_profitloss =0 
change = 0
dates = []
PLChange = []

# Path to collect the budget data from the Resources folder
#csvpath =  os.path.join("..", "Resources", "budget_data.csv")
csvmatch = os.getcwd()

csvpath = os.path.join(csvmatch,'Resources','budget_data.csv')
print(csvpath)
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile)
	csv_header = next(csvreader)
	print(csv_header)
	for row in csvreader:
		Total_Months +=1
		Current_profitloss = int(row[1])
		Net_Total_Profitloss += Current_profitloss
		if(Total_Months==1):
			Prev_profitloss = Current_profitloss	
		else:
			change = Current_profitloss -Prev_profitloss
			dates.append(row[0])
			PLChange.append(change)
			Prev_profitloss = Current_profitloss
	#print(Total_Months)
#average of profit loss changes for entire period
Sum_PL_Change = sum(PLChange)
Average_PLChanges = round(Sum_PL_Change/(Total_Months-1),2)
print(Average_PLChanges)

# Finding The greatest increase and decrease in profits (date and amount) over the entire period
greatest_increase =max(PLChange)
greatest_decrease = min(PLChange)

#Getting the index of greatest increase and decrease 
greatest_increase_Index = PLChange.index(greatest_increase)
greatest_decrease_Index = PLChange.index(greatest_decrease)
greatest_increase_month = dates[greatest_increase_Index]
greatest_decrease_month = dates[greatest_decrease_Index]

# Printing the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {Total_Months}")
print(f"Total:  ${Net_Total_Profitloss}")
print(f"Average Change:  ${Average_PLChanges}")
print(f"Greatest Increase in Profits:  {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {greatest_decrease_month} (${greatest_decrease})")

# writing the financial analysis report to a text file
budget_file = os.path.join("analysis", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {Total_Months}\n")
    outfile.write(f"Total:  ${Net_Total_Profitloss}\n")
    outfile.write(f"Average Change:  ${Average_PLChanges}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_increase_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_decrease_month} (${greatest_decrease})\n")

