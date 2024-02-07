class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if self.balance - money >= 0: self.balance -= money
        else: print(f'does not enough, you have only - {self.balance}tg')
    
    def __str__(self):
        return f'name: {self.owner} \nbalance: {self.balance}'

me = Account('Aiym', 8888)
print(me)

me.deposit(10000)
print(me)

me.withdraw(2500)
print(me)

me.withdraw(6000)
print(me)