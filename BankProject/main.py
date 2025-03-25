from bank import Bank
from customer import Customer
from current_account import CurrentAccount
from saving_account import SavingAccount
from atm import ATM
from atm_transaction import ATMTransaction

def main():
    # Create a bank
    my_bank = Bank("My Bank")

    # Create customers
    customer1 = Customer("Alice", 1)
    customer2 = Customer("Bob", 2)

    # Add customers to the bank
    my_bank.add_customer(customer1)
    my_bank.add_customer(customer2)

    # Create accounts for customers
    current_account1 = CurrentAccount("CA123", 1000)
    saving_account1 = SavingAccount("SA123", 500)

    # Add accounts to customers
    customer1.add_account(current_account1)
    customer1.add_account(saving_account1)

    # Create an ATM
    atm = ATM("Downtown")

    # Perform transactions
    print("Initial Balances:")
    print(f"Alice's Current Account Balance: {current_account1.balance}")
    print(f"Alice's Saving Account Balance: {saving_account1.balance}")

    # Deposit into current account
    atm.perform_transaction(current_account1, "deposit", 200)
    print(f"Alice's Current Account Balance after deposit: {current_account1.balance}")

    # Withdraw from saving account
    atm.perform_transaction(saving_account1, "withdraw", 100)
    print(f"Alice's Saving Account Balance after withdrawal: {saving_account1.balance}")

    # Attempt to withdraw more than the balance
    try:
        atm.perform_transaction(saving_account1, "withdraw", 500)
    except ValueError as e:
        print(f"Error: {e}")

    # Display all customers
    print("\nCustomers in the bank:")
    for customer in my_bank.get_customers():
        print(f"Customer ID: {customer.customer_id}, Name: {customer.name}")

if __name__ == "__main__":
    main()