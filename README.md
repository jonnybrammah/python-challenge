# python-challenge

This is a repo containing code in the file *main.py* which does two distinct things.
- PyBank, which looks through a csv file containing a set of finanical data bout a company, sorts through it and returns key financial information, and
- PyPoll, which looks through a set of poll data (again in a csv file), sorts through it and returns information about votes cast for each candidate and the results.
In both cases, both codes read the csv files from a "Resources" folder and return results both to the terminal and into a text file in the "analysis" folder.

Both codes are explained in more detail below:

# PyBank

## Code Explanation

In the PyBank code, a series of lists are created in order to store key information like the monthly profit or loss and the change between subsequent months.
The file is then read and a for loop counts the number of rows, and sums the information in the profit/loss column and stores it as a variable called "total". In the same for loop, each row's profit or loss is stored in the "monthlyprofitloss" list.

Calculations are then performed:
- The change in monthly profit or loss stores the change in profit or loss between every two subsequent indices in the "monthlyprofitloss" list and stores it as a new list. 
- The average of this "monthlychange" list is determined by summing all indices, and dividing by the number of indices.
- The maximum profit is determined by finding the index in the "monthlychange" list associated with the greatest positive change (max).
- The maximum loss is determined by finding the index in the "monthlychange" list associated with the greatest loss (min, since this will be a negative, indicating a loss).

Finally, all of this information is written to the terminal through a series of print statements, and then written to a text file called "budget_text_file.txt" found in the analysis folder. The results can also be seen here:

**Financial Analysis**

- Total Months: 86 
- Total: $22564198
- Average Change: $-8311.11
- Greatest Increase in Profits: Aug-16 ($1862002)
- Greatest Decrease in Profits: Feb-14 ($-1825558)


## Discussion of Results

This shows us that the total amount of money gained by the company over the 86 months analyzed was about $22.5 million dollars. The average change from month-to-month is slightly negative (at roughly -$8000) but it is important to remember this is the _change between months_ and there are still more months where a profit is made than a loss is incurred.

The month with the greatest increase in profits was August 2016 with a profit of $1.86 million.
The month with the greatest loss was February 2014 with a loss of -$1.83 million.

# PyPoll

## Code Explanation

In the PyPoll code, similarly a number of lists are created to store the information from the csv file, which contains a column for ballotid, a column for county, and a column for the candidate voted for. All of these are created as lists.
The file is read and each row is appended to each corresponding list. The number of total ballots cast is counted by the length of any of these lists and stored as a variable entitled "totalballots".

Another list is also defined to store unique candidate names, entitled "candidatenames" and a for loop runs through the list of votes and stores each unique name in the "candidatenames" list.

Another foor loop then runs through the votes list and counts the number of times each candidate name appears, and stores that count in a new list called "candidate_votes_number" and also calculates the percentage they attained using the totalballots variable defined earlier.

Since these three lists are moved through in the same order the number of votes stored in index 1 (for example) of the votes list will correspond the candidate stored in index 1 of candidate_names. This means the results can be viewed by later printing a statement like "candidate_names[1] scored candidate_votes_number[1] votes" (obviously with improved syntax).

A loop determines the index in the candidate_votes_number list associated with the greatest number of votes, which can be used later to call the winning name and their number of votes.

All of this is then printed to the terminal, using a for loop to show each candidate and their respective number of votes and percentage of vote attained, and the "winning_index" to print the winner.

Finally, all of this is then written into a text file called "election_results_text_file.txt" found in the analysis folder, but those results can also be found below:

**Election Results** 
 
- Total Votes: 369711
  - Charles Casper Stockham: 23.049% (85213)
  - Diana DeGette: 73.812% (272892)
  - Raymon Anthony Doane: 3.139% (11606)

- Winner: Diana DeGette


## Discussion of Results

The results here are fairly clear. The winner of the election was Diana DeGette with an overwhelming 74% of the vote, which was just over 270,000 votes from a total of roughly 370,000.
The second place candidate was Charles Casper Stockham with roughly 23% of the vote, and the third place candidate was Raymon Anthony Doane with just over 3% of the vote.
