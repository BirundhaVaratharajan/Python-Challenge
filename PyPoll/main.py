#Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

#import Directories
import os
import csv

#defining variables 
Total_votes =0 
Candidate =""
winner = ""
# cadiate name list
Candidate_namelist = [] 
# Dictionary to store the complete list of candidate and their total number of received votes
Candidate_vote_count = {} 

#getting the current directory
csvmatch = os.getcwd()
#  Path to collect election data from the Resources folder
csvpath = os.path.join(csvmatch,'PyPoll','Resources','election_data.csv')

print(csvpath)
# from the election data file 
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile)
	csv_header = next(csvreader)
	for row in csvreader:
		Total_votes +=1
		Candidate = row[2]
		if Candidate not in Candidate_namelist:
			Candidate_namelist.append(Candidate)	
			Candidate_vote_count[Candidate] =0
		
		Candidate_vote_count[Candidate] = Candidate_vote_count[Candidate]+1 
		
 #finding winner 
winner = max(Candidate_vote_count,key= Candidate_vote_count.get)
		
 #printing the Election results in Terminal       
print("Election Results\n")
print("----------------------------------------\n")
print(f"Total Votes:  {Total_votes}\n")
print("----------------------------------------")
# Finding vote percentage for each candidate 
for row in Candidate_namelist:
	print(f"{row}: {round((Candidate_vote_count[row]/Total_votes)*100, 3)} % ({Candidate_vote_count[Candidate]:,}) ")
print("----------------------------------------\n")
print(f"Winner: {winner}\n")
print("----------------------------")


# writing the financial analysis report to a text file
budget_file = os.path.join('Pypoll',"analysis", "Election Results.txt")
with open(budget_file, "w") as outfile:

    outfile.write(" Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes:  {Total_votes}\n")
    outfile.write("----------------------------\n")
    # Finding vote percentage for each candidate 
    for row in Candidate_namelist:
        outfile.write(f"{row}: {round((Candidate_vote_count[row]/Total_votes)*100, 3)} % ({Candidate_vote_count[Candidate]:,}) \n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("----------------------------\n")
