import os
import csv

mainPyPoll = os.path.join("..","PyPoll","Homework_03-Python_PyPoll_Resources_election_data.csv")

with open(mainPyPoll) as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=",")
    csv_header= next(csv_file)

    votesCount=0
    candidateCount=0
    candidateName_list=[]
    for row in csv_reader:
        votesCount +=1 #giveme the number of total votes
        
        candidateName = row[2] #column reffering to canditates names

        
        #returns a list with the candidates
        if len(candidateName_list)==0:                                #Adding the first name to the list.
            
            candidateName_list= candidateName_list+[candidateName] 
            
        else:                                                         # condition that avoids repeating names.
            if candidateName not in candidateName_list:
                candidateName_list= candidateName_list+[candidateName]

        #if candidateName in row[2]:
            #candidateCount= row[2].count(candidateName)

    


    print(f'Election Results')
    print(f'-----------------------')
    print(f'Total voters: {votesCount}')
    print(f'-----------------------')
    print(f' {candidateName_list}')
    print(f' {candidateCount}')
    #print(f'Greatest Increase in Profits: {dateMaxaverage} {maxMonth}')
    #print(f'Greatest Decress in Profits: {dateMinAverage} {minMonth}')
