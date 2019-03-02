

# import modules
import os
import csv

# read the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
month =[]
profit_Loss =  []


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #count months in csvfile
    
    for row in csvreader:
        month.append(row[0])
        profit_Loss.append(float(row[1]))


totalmonth = len (month)
print (totalmonth)

totalrevenue = sum (profit_Loss)   
print (totalrevenue)