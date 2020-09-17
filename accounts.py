#Import libraries
import logging
logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)
import csv
from decimal import Decimal
from datetime import datetime

class Transaction:
    def __init__(self,date,sender,recipient,narrative,amount):
        self.date = date
        self.sender = sender
        self.recipient = recipient
        self.narrative = narrative
        self.amount = amount


class Account:
    def __init__(self,holder):
        self.holder = holder
        self.balance = Decimal(0)
        self.transaction = []


accounts = {}
with open('DodgyTransactions2015.csv', newline='') as f:
    logging.info('CSV file opened!')
    contents = csv.DictReader(f)
    row_count = 1
    for row in contents:
        bad_row = False
        row_count = row_count + 1
        unformatted_date = row['Date']
        logging.info('unformatted_date: %s', unformatted_date)

        try:
            date = datetime.strptime(unformatted_date, '%d/%m/%Y').date()
        except ValueError as e:
            bad_row = True
            print('Exception raised: %s. Conversion of %s to date format has failed. '
                  'Please check if input supports this format.'% (e, unformatted_date))
            date = None

        sender = row['From']
        logging.info('sender: %s', sender)
        recipient = row['To']
        logging.info('recipient: %s', recipient)
        narrative = row['Narrative']
        logging.info('narrative: %s', narrative)
        unformatted_amount = row['Amount']
        logging.info('unformatted_amount: %s', unformatted_amount)

        try:
            amount = Decimal(unformatted_amount)
        except BaseException as e:
            bad_row = True
            print('Exception raised: %s. '
                  'Type conversion of %s to decimal has failed.'
                  ' Please check if input can be cast to a decimal'% (e, row['Amount']))
            amount = None

        logging.info('amount: %s', amount)

        if sender in accounts:
            sender_account = accounts[sender]
            logging.info('Sender name of %s recognised as belonging to one of the known accounts.', sender)
        else:
            sender_account = Account(holder=sender)
            accounts[sender] = sender_account
            logging.info('New account created for %s', sender)

        if recipient in accounts:
            receiver_account = accounts[recipient]
            logging.info('Recipient name of %s recognised as belonging to one of the known accounts.', recipient)
        else:
            receiver_account = Account(holder=recipient)
            accounts[recipient] = receiver_account
            logging.info('New account created for %s', recipient)

        if bad_row:
            print('Row %s in CSV file contains an incorrect data type'% row_count)
            continue

        sender_account.balance = sender_account.balance - amount
        logging.info('£%s leaves account of %s', amount, sender_account.holder)
        receiver_account.balance = receiver_account.balance + amount
        logging.info('£%s is sent to account of %s', amount, receiver_account.holder)
        transaction = Transaction(date,sender,recipient,narrative,amount)
        sender_account.transaction.append(transaction)
        logging.info('New transaction of £%s recorded in account of %s', amount, sender_account.holder)
        receiver_account.transaction.append(transaction)
        logging.info('New transaction of £%s recorded in account of %s', amount, receiver_account.holder)

#List All
#prints each Holder and the amount they owe or are owed
def List_All():
    for holder,account in accounts.items():

        balance = account.balance
        if balance < 0:
            print(holder + ' owes: ' + str(abs(balance)))
        else:
            print(holder + ' is owed: ' + str(balance))

#List[Account]
#prints a list of every transaction, with the date and narrative for an account when given the account name
#To run from command line:  python -c "import accounts; accounts.List(name ='Jon A')"
def List(name):
    account = accounts[name]
    transaction = account.transaction
    for single_trans in transaction:
        print(single_trans.date, single_trans.sender, single_trans.recipient, single_trans.narrative, single_trans.amount)
