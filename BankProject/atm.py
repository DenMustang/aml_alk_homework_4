class ATM:
    def __init__(self, location):
        self.location = location

    def perform_transaction(self, account, transaction_type, amount):
        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)