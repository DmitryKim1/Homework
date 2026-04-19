class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner} {self.balance}")

    
acc1 = BankAccount("D" , 100)
acc2 = BankAccount("A", 200)

acc1.deposit(50)
acc2.withdraw(100)

acc1.show_balance()
acc2.show_balance()