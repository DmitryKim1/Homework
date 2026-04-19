class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        if amount >self._balance:
            print("Недостаточно денег")
            return 
        self._balance -= amount

    def __str__(self):
        return f"Владелец: {self.owner}, баланс: {self._balance}"
    
acc = BankAccount("N", 100)
print(acc)

acc.deposit(50)
print(acc)

acc.withdraw(30)
print(acc)

print(acc.balance)