"""Helper functions for loading accounts and validating PIN number."""

import csv
from pathlib import Path
import sys


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('data/accounts.csv')
    accounts = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts


def validate_pin(pin):
    """Verifies that PIN is 6 digits long."""

    # @TODO: Verifies length of pin is 6 digits, prints validations message and returns True. Else returns False.
    if len(pin) == 6:
        print("Your pin is the correct length")
        return True
    else:
        print("The pin you have entered is not 6 digits long")
        return False

def update_accounts(account):
    """Writes account information from CSV to list."""
    csvpath = Path('data/accounts.csv')
    input = open(csvpath, 'rb')
    output = open(csvpath, 'wb')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0] != account["pin"]:
            writer.writerow(row)
    account_writer =csv.DictWriter(csvpath)
    account_writer.writerow(account)
    input.close()
    output.close()
