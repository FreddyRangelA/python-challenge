import os
import csv

mainPyPoll = os.path.join("..","PyPoll","Homework_03-Python_PyPoll_Resources_election_data.csv")

with open(mainPyPoll) as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=",")
    csv_header= next(csv_file)

    votesCount=0
    candidateCount=0
    candidateName_list=[]
    candidateName_dict={}
 
    for row in csv_reader:
        votesCount +=1 #giveme the number of total votes
        
        candidateName = row[2] #column reffering to canditates names

        
        #returns a list with the candidates
        if len(candidateName_list)==0:                                #Adding the first name to the list.

            candidateName_list= candidateName_list+[candidateName]
            candidateName_dict[candidateName] =1
            
        else:                                                         # condition that avoids repeating names.
            if candidateName not in candidateName_list:
                candidateName_list= candidateName_list+[candidateName]
                candidateName_dict[candidateName]=1
            else:
                candidateName_dict[candidateName]+=1
       
    print(f'Election Results')
    print(f'-----------------------')
    print(f'Total voters: {votesCount}')
    print(f'-----------------------')   

    for candidateName in candidateName_list:
 
        votesPercent =round((candidateName_dict[candidateName]/votesCount)*100,4)
        print(f'{candidateName}:  {votesPercent}%  ({candidateName_dict[candidateName]})')
    
    winner=max(candidateName_dict, key=candidateName_dict.get)
    print(f'-----------------------')   
    print(f'winner: {winner}')
    print(f'-----------------------')   
    