# import modules
import os
import csv
import collections
# read the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#declare varialbe

total_vote_count = 0

khan_vote = 0

correy_vote = 0

li_vote = 0

tooley_vote = 0

#load the csv file in dictionary

with open(csvpath, newline="") as csvfile:
    
    reader = csv.DictReader(csvfile) 
     
# run the loop to count vote number for 4 candidates
    for row in reader:
        

        candidate = (row["Candidate"])

        voter_id = (int(row["Voter ID"]))

        Count = (row["County"])

        if "Khan" == candidate:

            khan_vote = khan_vote + 1

        if "Li" == candidate:

            li_vote = li_vote +1

        if "Correy" == candidate:

            correy_vote = correy_vote+1

        if "O'Tooley" == candidate:

            tooley_vote = tooley_vote+1

    
#total vote and vote percentage count
    total_vote_count = khan_vote + li_vote + correy_vote + tooley_vote
    
    khan_percent = format(khan_vote/total_vote_count,'0.3%')

    li_percent = format(li_vote / total_vote_count  , '0.3%')

    correy_percent = format( correy_vote/total_vote_count, '0.3%')

    tooley_percent = format(tooley_vote/total_vote_count , '0.3%')

    maxvote = max(khan_vote,li_vote,correy_vote,tooley_vote)

# find out the winner 

if maxvote == khan_vote:
    winner = "Khan"
elif maxvote == li_vote:
    winner = "Li"
elif maxvote == correy_vote:
    winner = "Correy"
elif maxvote == tooley_vote:
    winner = "Tooley"


 


print("Election Results")
print("----------------------------")
print("Total Votes: ", str(total_vote_count))
print("----------------------------")
print ("Khan: ", str(khan_percent),"(",str(khan_vote),")")
print ("Correy: ", str(correy_percent),"(",str(correy_vote),")")
print ("Li: ", str(li_percent),"(",str(li_vote),")")
print ("O'Tooley: ", str(tooley_percent),"(",str(tooley_vote),")")
print("----------------------------")
print("Winner: ",winner)

    


        
    













        


    

    


  
   


    

