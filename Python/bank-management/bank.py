class Bank:
    ACCOUNT = [
        {'number': 0,
         'balance': 0,
         }
    ]

    def __init__(self, account_number=None):
        self.account_number = account_number

    def create_account(self):
        new_account = {
            'number': len(self.ACCOUNT) + 1,
            'balance': 0,
        }
        self.ACCOUNT.append(new_account)
        return new_account

    def deposit(self, deposit_amount):
        if isinstance(deposit_amount, int):
            for account in self.ACCOUNT:
                if account['number'] == self.account_number:
                    account['balance'] += deposit_amount
                    return f'Rs.{deposit_amount} has been credited in your account {self.account_number}!'
            return 'Account not found'
        raise TypeError("Amount should be integer")

    def withdraw(self, withdraw_amount):
        if isinstance(withdraw_amount, int):
            for account in self.ACCOUNT:
                if account['number'] == self.account_number:
                    if account['balance'] > withdraw_amount:
                        account['balance'] -= withdraw_amount
                        return f'Rs.{withdraw_amount} has been debited in your acc {self.account_number}!'
                    return "You don't have enough balance"
            return "Account not found"
        raise TypeError("Amount should be integer")

    def balance_enquiry(self):
        for account in self.ACCOUNT:
            if account['number'] == self.account_number:
                return f"Total Balance: Rs.{account['balance']}"
        return 'Account not found'
