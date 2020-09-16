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
            sender_account = accounts[sender]
        else:
            sender_account = create_account(sender)
            #assigns name to an account
            accounts[sender] = sender_account

        if recipient in accounts:
            reciever_account = accounts[recipient]
        else:
            reciever_account = {'Holder': recipient, 'Balance': Decimal(0), 'Transaction' : []}
            accounts[recipient] = reciever_account

        amount = Decimal(row['Amount'])
        sender_account['Balance'] = sender_account['Balance'] - amount
        reciever_account['Balance'] = reciever_account['Balance'] + amount
        transaction = row
        sender_account['Transaction'].append(transaction)
        reciever_account['Transaction'].append(transaction)

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

#List[Account]
#prints a list of every transaction, with the date and narrative for an account when given the account name
#pass in holder
def List(name):
    account = accounts[name]
    transaction = account['Transaction']
    for single_trans in transaction:
        print(single_trans)
List(name = 'Jon A')
