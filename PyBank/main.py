#Your task is to create a Python script that analyzes the records to calculate each of the following:

    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
#--------------------------------------------------------------------------------------

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#skip headers in counts
    header = next(csvreader)

#--------------------------------------------------------------------------------------

#count the number of rows in the csv file to get the number of months
#https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
num_rows = 0
for row in open(csvpath):
    num_rows += 1
print("the total number of months is:", num_rows)

#--------------------------------------------------------------------------------------

#sum the total of column 2 to get the net total
#list comprehension?
#https://stackoverflow.com/questions/10657965/add-all-values-in-a-csv-column-in-python
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        Value_sum = sum([int(row[1])])
    print("The total value of Profits/Losses is:", Value_sum)

#-------------------------------------------------------------------------------------
  
  #get average of profits/losses 
    average = (Value_sum / num_rows)
    print("The average of Profits/Losses is:", average)

#--------------------------------------------------------------------------------------

#find greatest value
#https://stackoverflow.com/questions/35329573/finding-max-value-in-a-column-of-csv-file-python
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
          maxnum = max(csvreader, key=lambda row: int(row[1]))
print("The single greatest increase was:", maxnum)

#--------------------------------------------------------------------------------------

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
          minnum = min(csvreader, key=lambda row: int(row[1]))
print("The single greatest decrease was:", minnum)