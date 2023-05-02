#import
import os,csv

#set paths
electionpath = os.path.join('Resources','election_data.csv')

#-----------------------------------

#read csv file and place content in variables
with open(electionpath, 'r') as elecfile:
    elec_iter = csv.reader(elecfile, delimiter =',')
    
    #header skip
    header = next(elec_iter)

    #transfer to lists 369711 items
    eleclist = []
    for x in elec_iter:
        eleclist.append(x)

#-----------------------------------

#votes casted
votes = len(eleclist)

#get candidates
candidates = []
votelist = []
for x in eleclist:
    if x[2] not in candidates:
        candidates.append(x[2])

    #make a list of names
    votelist.append(x[2])

#-----------------------------------

#percentage and votecount
count = []
win_perc = []
for x in range(len(candidates)): #from 0 - 2 (3 candidates)
    count.append(votelist.count(candidates[x]))
    win_perc.append(round(count[x]/votes *100,3))

#-----------------------------------

#get winner
winner = candidates[count.index(max(count))] #max of count index in candidates

#-----------------------------------

#print results

result=[]
result.append(f'Election Reults\n\
-------------------------\n\
Total Votes: {votes}\n\
-------------------------\n')
      
#print per candidate
for x in range(len(candidates)):
    result.append(f'{candidates[x]}: {win_perc[x]}% ({count[x]})\n')

result.append(f'-------------------------\n\
Winner: {winner}\n\
-------------------------')

#print looped with txt file write

#-----------------------------------

#write to txt file
#create new txt file and place results
with open('analysis/results.txt', 'w') as txtfile:
    for x in result:
        print(x)
        txtfile.writelines(x)

#-----------------------------------