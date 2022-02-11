#Imported Dependencies
import os
import csv
#Established Variables
candidates = {}
elec_csvpath = os.path.join('election_data.csv')

vote_total = 0
winning_votes = 0
winner = None

#Collected Candidate Names and tallied their votes
with open(elec_csvpath) as election_file:
    elec_csvreader = csv.reader(election_file, delimiter = ',')

    elec_csvheader = next(election_file)

    for row in elec_csvreader:
        vote_total += 1
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] += 1

#Begin Printing Results
print(
    f'Election Results\n'
    f'-----------------------------------\n'
    f'Total Votes: {vote_total}\n'
    f'-----------------------------------'
)

#Calculated each Candidate's Vote Percentage and the Winning Candidate
for candidate,total_can_votes in candidates.items():
    vote_percentage = ('{:.3f}'.format((total_can_votes/vote_total) * 100))
    if total_can_votes >= winning_votes:
        winning_votes = total_can_votes
        winner = candidate
    print(
        f'{candidate}: {vote_percentage}% ({total_can_votes})'
        
    )

# Finished Printing Results
print(
    f'-----------------------------------\n'
    f'Winner: {winner}\n'
    f'-----------------------------------'
)

# Consolidated Results
print(
    f'Election Results\n'
    f'-----------------------------------\n'
    f'Total Votes: {vote_total}\n'
    f'-----------------------------------'
)

for candidate,total_can_votes in candidates.items():
    vote_percentage = ('{:.3f}'.format((total_can_votes/vote_total) * 100))
    if total_can_votes >= winning_votes:
        winning_votes = total_can_votes
        winner = candidate
    print(
        f'{candidate}: {vote_percentage}% ({total_can_votes})'
        
    )
    

print(
    f'-----------------------------------\n'
    f'Winner: {winner}\n'
    f'-----------------------------------'
)

#Exported txt file
output_file = os.path.join('election_results.txt')

PyPoll = open(output_file, "w+")
PyPoll.writelines(
    f'Election Results\n'
    f'-----------------------------------\n'
    f'Total Votes: {vote_total}\n'
    f'-----------------------------------\n')
for candidate,total_can_votes in candidates.items():
    PyPoll.writelines(
        f'{candidate}: {vote_percentage}% ({total_can_votes})\n'       
    )
PyPoll.writelines(
    f'-----------------------------------\n'
    f'Winner: {winner}\n'
    f'-----------------------------------'
) 


