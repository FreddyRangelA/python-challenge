import os
import csv

#open resource folder
mainPyBank_csv = os.path.join("..","PyBank","Homework_03-Python_PyBank_Resources_budget_data.csv")

with open(mainPyBank_csv) as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=",")
    
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    
    monthsCount = 0
    profitTotal = 0
    previousChange=0
    averageChange_list=[]
    avrageChange = 0
    monthChange_List = []

    for row in csv_reader:
        
        monthsCount +=1
        profitTotal= profitTotal+ int(row[1])

        #Average in Change
        averageChange = int(row[1])-previousChange #substracting the previous value to the next value
        #print(averageChange)
        previousChange= int(row[1]) #assigning previous value to the current row
        averageChange_list.append(averageChange)
        print (sum(averageChange_list))
           
       
        #monthChange_List = [monthChange_List]+[row[0]]
       


        #revenueAverage=sum(averageChange_list)/len(averageChange_list)





        #print(row[1])
   
         
           
        #print(row)
    print(f'the total months: {monthsCount}')
    print(f'profit total: {profitTotal}')
    #print(f'Average in Change: {revenueAverage}')





    