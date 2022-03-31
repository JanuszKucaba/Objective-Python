'''
Bank account class
'''

class BankAccount:
    '''Takes name balance and bank name
    could retur info about account, witdrwa and deposit'''
    bank_name = 'Commercial Bank, Palace Street, Rzeszow'

    def __init__(self, name, balance=0, bank=bank_name):
        '''initialization class'''
        self.name = name
        self.balance = balance
        self.bank = bank

    def display(self):
        '''display account info: name, balance and bank name'''
        print(self.name, self.balance, self.bank)

    def withdraw(self, amount):
        '''choosing money'''
        self.balance -= amount

    def deposit(self, amount):
        '''adding money'''
        self.balance += amount

if __name__ == '__main__':
    a1 = BankAccount('John', 500, 'Central Bank')
    a2 = BankAccount('Tom', 100)
    a3 = BankAccount('George')

    a1.display()
    a2.display()
    a2.withdraw(50)
    a2.display()
    a3.display()
    a3.deposit(500)
    a3.display()
