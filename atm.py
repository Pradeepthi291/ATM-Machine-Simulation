class ATM:
    def __init__(self):
        # Initialize the ATM with default values
        self.balance = 1000  # Default account balance
        self.pin = '1234'  # Default PIN
        self.transaction_history = []  # List to keep track of transactions

    def account_balance_inquiry(self):
        """Displays the current balance."""
        print(f"Current balance: ${self.balance:.2f}")
        self.transaction_history.append("Balance inquiry")

    def cash_withdrawal(self, amount):
        """Allows the user to withdraw cash if the amount is available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! You withdrew ${amount:.2f}.")
            self.transaction_history.append(f"Withdrawal: ${amount:.2f}")
        else:
            print("Insufficient funds.")
            self.transaction_history.append("Failed withdrawal attempt")

    def cash_deposit(self, amount):
        """Allows the user to deposit cash into their account."""
        self.balance += amount
        print(f"Deposit successful! You deposited ${amount:.2f}.")
        self.transaction_history.append(f"Deposit: ${amount:.2f}")

    def pin_change(self, old_pin, new_pin):
        """Allows the user to change their PIN if the old PIN is correct."""
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN change")
        else:
            print("Incorrect old PIN. PIN change failed.")

    def transaction_history_inquiry(self):
        """Displays the transaction history."""
        if self.transaction_history:
            print("Transaction history:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

# Main function to interact with the ATM
def main():
    atm = ATM()
   
    while True:
        print("\nATM Menu:")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")
       
        choice = input("Enter your choice (1-6): ")
       
        if choice == '1':
            atm.account_balance_inquiry()
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            atm.cash_withdrawal(amount)
        elif choice == '3':
            amount = float(input("Enter amount to deposit: $"))
            atm.cash_deposit(amount)
        elif choice == '4':
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.pin_change(old_pin, new_pin)
        elif choice == '5':
            atm.transaction_history_inquiry()
        elif choice == '6':
            print("Exiting the ATM. Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()   

