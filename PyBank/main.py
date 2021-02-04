import os
import csv

#open resource folder
mainPyBank_csv = os.path.join("..","PyBank","Homework_03-Python_PyBank_Resources_budget_data.csv")

monthsCount = 0
profitTotal = 0
previousChange=0
averageChange_list=[]
avrageChange = 0
monthChange_List = []
averageChangerRow=0

with open(mainPyBank_csv) as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=",")
    
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    
   
    maxaverage=0
    minAverage=0
    for row in csv_reader:
        
        monthsCount +=1
        profitTotal= profitTotal+ int(row[1])

        #Average in Change
        averageChange = int(row[1])-previousChange #substracting the previous value to the next value

         # Greatest Increase in Profits
        if averageChange > maxaverage:
            maxaverage = averageChange
            dateMaxaverage=row[0]
        else:                               #Greatest Decress in Profits
            if averageChange< minAverage:
                minAverage =averageChange
                dateMinAverage=row[0]

        previousChange= int(row[1]) #assigning the current row to the previous value
        if monthsCount != 1:        #excluding the first month value since there is no changes
            averageChange_list=averageChange_list+[averageChange]
        
    revenueAverage=round((sum(averageChange_list)/len(averageChange_list)), 2) 
    maxMonth = max(averageChange_list)
    minMonth = min(averageChange_list)


    print(f'Finacial Analisys')
    print(f'-----------------------')
    print(f'the total months: {monthsCount}')
    print(f'profit total: {profitTotal}')
    print(f'Average in Change: {revenueAverage}')
    print(f'Greatest Increase in Profits: {dateMaxaverage} {maxMonth}')
    print(f'Greatest Decress in Profits: {dateMinAverage} {minMonth}')




    