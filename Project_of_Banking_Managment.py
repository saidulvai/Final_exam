class User:
    account_counter = 1

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = User.account_counter
        self.transaction_history = []
        self.loan_taken = 0
        User.account_counter += 1

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded. Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, loan_amount):
        if self.loan_taken < 2:
            self.balance += loan_amount
            self.loan_taken += 1
            self.transaction_history.append(f"Loan taken: ${loan_amount}")
        else:
            print("You have already taken the maximum number of loans.")

    def transfer_amount(self, recipient, amount):
        if recipient is None:
            print("Account does not exist.")
        elif amount > self.balance:
            print("Transfer amount exceeded.")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to Account {recipient.account_number}")

class Admin:
    users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        Admin.users.append(user)
        print(f"Account created successfully. Account Number: {user.account_number}")

    def delete_account(self, user):
        Admin.users.remove(user)
        print(f"Account {user.account_number} deleted successfully.")

    def see_all_accounts(self):
        print("All User Accounts:")
        for user in Admin.users:
            print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {user.email}")

    def check_total_balance(self):
        total_balance = sum(user.balance for user in Admin.users)
        print(f"Total Available Balance: ${total_balance}")

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.loan_taken for user in Admin.users)
        print(f"Total Loan Amount: ${total_loan_amount}")

    def toggle_loan_feature(self, status):
        User.loan_feature_enabled = status
        print(f"Loan Feature {'enabled' if status else 'disabled'}")



# Example Usage
admin = Admin()

# Create user accounts
admin.create_account("Saidul", "saidul@example.com", "Moheshkhali", "Savings")
admin.create_account("Shakil", "shakil@example.com", "Banderban", "Current")

# See all user accounts
admin.see_all_accounts()

# Access user account and perform transactions
user1 = Admin.users[0]
user2 = Admin.users[1]

user1.deposit(1000)
user1.transfer_amount(user2, 500)
user2.withdraw(200)
user1.check_balance()
user1.check_transaction_history()
user1.take_loan(10000)

# Admin functionalities
admin.check_total_balance()
admin.check_total_loan_amount()
admin.toggle_loan_feature(True)
admin.delete_account(user1)
admin.see_all_accounts()

# currerntUser = None
# while(True):
#     if currerntUser == None:
#         print("\n--> No user !")
#         print("Create an account")
#         name = input("Name:")
#         Email = input("Email:")
#         address = input("Address:")
#         a=input("Savings Account or current Account (Savings/current) :")
#         currerntUser = admin.create_account(name, Email, address, a)
    
#     else:

