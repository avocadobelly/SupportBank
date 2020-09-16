#Import libraries
import csv
from decimal import Decimal

#Create Account Class:
#Creates generic SupportBank account

class Account:
    def __init__(self,holder):
        self.holder = holder
        self.balance = Decimal(0)
        self.transaction = []

accounts = {}
with open('Transactions2014.csv', newline='') as f:
    contents = csv.DictReader(f)
    for row in contents:
        sender = row['From']
        recipient = row['To']
        if sender in accounts:
            sender_account = accounts[sender]
        else:
            sender_account = Account(holder = sender)
            #assigns name to an account:
            accounts[sender] = sender_account

        if recipient in accounts:
            reciever_account = accounts[recipient]
        else:
            reciever_account = Account(holder = recipient)
            accounts[recipient] = reciever_account

        amount = Decimal(row['Amount'])
        sender_account.balance = sender_account.balance - amount
        reciever_account.balance = reciever_account.balance + amount
        transaction = row
        (sender_account.transaction).append(transaction)
        (reciever_account.transaction).append(transaction)

#List All
#prints each Holder and the amount they owe or are owed
def List_All():
    for holder,account in accounts.items():

        balance = account.balance
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
    transaction = account.transaction
    for single_trans in transaction:
        print(single_trans)
List(name = 'Jon A')
