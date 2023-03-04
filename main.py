#PYBANK CODE BELOW:

#import the fun things
import os
import csv

#define a list that will hold the date, the monthly profit and loss (both to be read from csv file)
date = []
monthlyprofitloss = []

#define a list that will hold the change between months (to be calculated from other lists)
monthlychange = []

#tell the computer where to find the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#read the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    #define two integers that will hold the overall total, and will count the number of months
    total = 0
    totalmonths = 0

    #for each row in the sheet
    for row in csvreader:
        
        #increase the count of total months by 1
        totalmonths = totalmonths + 1
        #increase the overall total by the amount in the profit/losses column
        total = total + int(row[1])

        #read from the file and create the lists for the dates and monthlyprofit/losses
        date.append(row[0])
        monthlyprofitloss.append(int(row[1]))

#calculate the monthly change between consecuitive months
monthlychange = [monthlyprofitloss[i+1]-monthlyprofitloss[i] for i in range (len(monthlyprofitloss)-1)]

#calculate the average of the elements in the monthly change list (round to 2 decimal places)
averagemonthlychange = round(sum(monthlychange)/len(monthlychange),2)

#find the index in the monthly change list associated with the maximum change and the minimum change
maxmonthlyprofit_index = monthlychange.index(max(monthlychange))
maxmonthlyloss_index = monthlychange.index(min(monthlychange))

#print the basics
print(f"Financial Analysis \n -------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${total}")
print(f"Average Change: ${averagemonthlychange}")

#print the date row with the index one greater than the index of the largest monthly profit or loss
#(to make up for the fact this list is one item fewer since it's change between items in another list)
#then print the monthlychange row with the index of the largest monthly profit and loss
print(f"Greatest Increase in Profits: {date[maxmonthlyprofit_index+1]} (${monthlychange[maxmonthlyprofit_index]})")
print(f"Greatest Decrease in Profits: {date[maxmonthlyloss_index+1]} (${monthlychange[maxmonthlyloss_index]})")

#Specify the file to write to
output_path = os.path.join("analysis", "budget_text_file.txt")

#Open the txtfile, and write the same information as previously printed
with open(output_path, 'w') as txtfile:
    txtwriter = txtfile.write
    txtfile.write("Financial Analysis \n-------------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${averagemonthlychange}\n")
    txtfile.write(f"Greatest Increase in Profits: {date[maxmonthlyprofit_index+1]} (${monthlychange[maxmonthlyprofit_index]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date[maxmonthlyloss_index+1]} (${monthlychange[maxmonthlyloss_index]})\n")

#Celebrate


#PYPOLL CODE BELOW:

#import all the fun stuff again
import os
import csv

#Create lists to hold information from the csv file
ballotid = []
county = []
candidate = []

#Specify the file to read from

csvpath = os.path.join('Resources', 'election_data.csv')

#read the csv file

with open(csvpath, 'r', encoding = 'UTF-8', newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    #for each row in the csv file, store the information in each column as a separate list
    for row in csvreader:
        ballotid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#the total number of ballots cast is equal to the length of any of these lists
totalballots = len(ballotid)

#identify unique candidates by appending each candidate name to a list 
#by running through the items in the candidate list and appending the name
#to a new list if it hasn't appeared before in the candidate list
candidate_names = []
for x in candidate:
    if x not in candidate_names:
        candidate_names.append(x)


#define two lists, one to store the candidate votes as a number
#and another to store the candidate votes as a percentage
candidate_votes_number = []
candidate_votes_percent = []

#run through the original candidate list and count the instances of each candidate name
#then append that value to a list to store it 
#then calculate the percentage and store that in a list too
for i in range(len(candidate_names)):
    count = candidate.count(candidate_names[i])
    candidate_votes_number.append(count)
    candidate_votes_percent.append(round((count/totalballots)*100, 3))

#since all of these lists (candidate_names, candidate_votes_number, and candidate_votes_percent)
#are all storing information in the same order, the index for a candidate in candidate_names
#will be the same index as their number of votes in candidate_vote_number
#so if we know the index with the maximum number of votes, we can use that index
#in any of these lists

#calculate the winning index by comparing the number of votes for every index
#in a list and recording the index associated with the maximum
winning_index = 0
for i in range(len(candidate_votes_number)):
    if candidate_votes_number[i] > candidate_votes_number[winning_index]:
        winning_index = i

#print all the results
print("Election Results\n-------------------------")
print(f"Total Votes: {totalballots}")
print("-------------------------")

#print the name, vote percentage, and vote total for each candidate
for i in range(len(candidate_names)):
    print(f"{candidate_names[i]}: {candidate_votes_percent[i]}% ({candidate_votes_number[i]})")

#print the winner by printing the index assocaited with largest number of votes in candidate_votes_number but inside the candidate_names list
print("-------------------------")
print(f"Winner: {candidate_names[winning_index]}")
print("-------------------------")

#Specify the file to write to
output_path = os.path.join("analysis", "election_results_text_file.txt")

#Open the txtfile, and write the same information as previously printed
with open(output_path, 'w') as txtfile:
    txtwriter = txtfile.write
    txtfile.write("Election Results \n-------------------------\n")
    txtfile.write(f"Total Votes: {totalballots}\n")
    txtfile.write("-------------------------\n")
    for i in range(len(candidate_names)):
        txtfile.write(f"{candidate_names[i]}: {candidate_votes_percent[i]}% ({candidate_votes_number[i]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {candidate_names[winning_index]}\n")
    txtfile.write("-------------------------")

#Celebrate or commiserate with your chosen candidate
