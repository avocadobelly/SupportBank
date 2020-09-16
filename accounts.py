#Import libraries
import csv
from decimal import Decimal

#Create Account:
#Creates generic SupportBank account
def create_account(holder):
    account = {'Holder' : holder, 'Balance' : Decimal(0), 'Transaction' : [] }
    return account

accounts = {}
with open('Transactions2014.csv', newline='') as f:
    contents = csv.DictReader(f)
    for row in contents:
        sender = row['From']
        recipient = row['To']
        if sender in accounts:
            from_account = accounts[sender]
        else:
            from_account = create_account(sender)
            accounts[sender] = from_account
        if recipient in accounts:
            to_account = accounts[recipient]
        else:
            to_account = {'Holder': recipient, 'Balance': Decimal(0), 'Transaction' : []}
            accounts[recipient] = to_account
        transaction = row
        amount = Decimal(row['Amount'])
        from_account['Balance'] = from_account['Balance'] - amount
        to_account['Balance'] = to_account['Balance'] + amount
        from_account['Transaction'].append(transaction)
        to_account['Transaction'].append(transaction)

#List All
#prints each Holder and the amount they owe or are owed
def List_All():
    for holder,account in accounts.items():

        balance = account['Balance']
        if balance < 0:
            print(holder + ' owes: ' + str(abs(balance)))
        else:
            print(holder + ' is owed: ' + str(balance))
List_All()
