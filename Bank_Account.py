class BankAccount:


    all_accounts = []


    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount

        return self

    def withdraw(self, amount):
        self.balance -= amount

        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

        return self

    def yield_interest(self):
        self.balance += self.int_rate

        return self



    @classmethod
    def print_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()



# end class

guido = BankAccount(0.02, 443)
monty = BankAccount(0.5, 4)

guido.deposit(300).deposit(200).deposit(100).withdraw(42).yield_interest()
monty.deposit(1230).deposit(333).withdraw(36).withdraw(23).withdraw(50).withdraw(75).yield_interest()


BankAccount.print_info()
