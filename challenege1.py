class Account:
    def __init__(self, owner, balance=0): self.owner, self.balance = owner, balance
    def deposit(self, amt): self.balance += amt; print(f"{self.owner} +${amt}, balance: ${self.balance}")
    def withdraw(self, amt):
        if amt <= self.balance: self.balance -= amt; print(f"{self.owner} -${amt}, balance: ${self.balance}")
        else: print("Insufficient funds.")

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, rate=0.02): super().__init__(owner, balance); self.rate = rate
    def add_interest(self): self.balance += self.balance * self.rate; print(f"{self.owner} interest added, balance: ${self.balance:.2f}")

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, limit=100): super().__init__(owner, balance); self.limit = limit
    def withdraw(self, amt):
        if amt <= self.balance + self.limit: self.balance -= amt; print(f"{self.owner} -${amt}, balance: ${self.balance}")
        else: print("Overdraft limit reached!")

accounts = [SavingsAccount("Alice", 1000), CheckingAccount("Bob", 200)]
for a in accounts: a.deposit(100); a.withdraw(50)
accounts[0].add_interest()
accounts[1].withdraw(400)
