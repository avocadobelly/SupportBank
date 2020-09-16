#Import libraries
import csv

with open('Transactions2014.csv', newline='') as f:
    contents = csv.reader(f)
    for row in contents:
        print(row)
print('completed')


