#Your task is to create a Python script that analyzes the votes and calculates each of the following:
  #* The total number of votes cast
  #* A complete list of candidates who received votes
  #* The percentage of votes each candidate won
  #* The total number of votes each candidate won
  #* The winner of the election based on popular vote.

#----------------------------------------------

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#skip headers in counts
    first_row = next(csvreader)
#sum the total of column 2 to get the net total
#https://stackoverflow.com/questions/10657965/add-all-values-in-a-csv-column-in-python
num_rows = 0
for row in open(csvpath):
    num_rows += 1
print("The total number of votes cast is:", num_rows)

#-------------------------------------------------------------------------------------
  
#make a list out of row 2 to show candidates
#assistance from tutor
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader) 
    poll_info = {}
    num_rows = 0
    for row in csvreader:
        num_rows += 1
        candidate = row[2]
        votes = 1
        if candidate not in poll_info:
            poll_info[candidate]=votes
        else: 
            poll_info[candidate] += 1
    winner = max(poll_info, key=poll_info.get)
    for candidate in poll_info:
        print(f'{candidate} : {((poll_info[candidate]/num_rows)*100):.2f}% ({poll_info[candidate]})')
    print('The winner is:', winner)
#-----------------------------------------------


output_path = os.path.join ("new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text2:

    # Write the first row (column headers)
    text2.write(f'Election Results\n')
    text2.write(f'The total number of votes cast is: {num_rows}\n')
    for candidate in poll_info:
        text2.write(f'{candidate} : {((poll_info[candidate]/num_rows)*100):.2f}% ({poll_info[candidate]})\n')
    text2.write(f'The winner is: {winner}')
  

    