#Import libraries
import csv
from decimal import Decimal

accounts = {}
with open('Transactions2014.csv', newline='') as f:
    contents = csv.DictReader(f)
    for row in contents:
        print(row)
        From = row['From']
        To = row['To']
        if From in accounts:
            from_account = accounts[From]
        else:
            from_account = {'Holder': From, 'Balance': Decimal(0), 'Transaction' : []}
            accounts[From] = from_account
        if To in accounts:
            to_account = accounts[To]
        else:
            to_account = {'Holder': To, 'Balance': Decimal(0), 'Transaction' : []}
            accounts[To] = to_account
        transaction = row
        amount = Decimal(row['Amount'])
        from_account['Balance'] = from_account['Balance'] - amount
        to_account['Balance'] = to_account['Balance'] + amount
        from_account['Transaction'].append(transaction)
        to_account['Transaction'].append(transaction)
print(accounts)
