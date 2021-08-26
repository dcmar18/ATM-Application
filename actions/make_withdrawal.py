"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Withdrawal Dialog."""

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.

    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.

    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
 
    amount = questionary.text("How much would you like to withdraw?").ask()
    amount = float(amount)

    if amount > 0.0:
        account["balance"] = account["balance"] - amount
        print(f"Your withdraw was successful.")
        return account
    else:
        sys.exit("This is not a valid withdrawal amount. Please try again.")