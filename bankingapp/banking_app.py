"""
Banking System using OOP:
+ Parent Class: User
+ Holds details about an user
+ Has a function to show user details
+ Child Class: Bank
+ Stores details about the account balance
+ Stores details about the amount
+ Allows for deposits, withdraw, view_balance
"""

# Parent Class
class User():
    """_summary_
    User class contains info about user: name, age and gender
    contains show_user_details function
    """
    def __init__(self, name, age, gender):
        """_summary_

        Args:
            name (string): _description_
            age (int): _description_
            gender (string): _description_
        """
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        """_summary_

        Args:
            name (string): _description_
            age (int): _description_
            gender (string): _description_
        """
        print('Personal details')
        print()
        print('Name ', self.name)
        print('Age ', self.age)
        print('Gender ', self.gender)


# Child Class
class Bank(User):
    '''The class bank inferiting from the user class'''
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        """_summary_

        Args:
            name (string): _description_
            age (int): _description_
            gender (string): _description_
        """
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Account balance has been updated: {self.balance} PLN')

    def withdraw(self, amount):
        """_summary_

        Args:
            name (string): _description_
            age (int): _description_
            gender (string): _description_
        """
        self.amount = amount
        if self.amount > self.balance:
            print(f'Insufficient Funds | Balance available: {self.balance} PLN')
        else:
            self.balance -= self.amount
            print(f'Account balance has been updated: {self.balance} PLN')

    def view_balance(self):
        """_summary_
        Show account balance
        """
        self.show_user_details()
        print(f'Account balance: {self.balance} PLN')


if __name__ == '__main__':
    client1 = Bank('Grzegorz Nowak', 29, 'mężczyzna')
    client1.deposit(1000)
    client1.withdraw(300)
    print('-' * 30)
    client1.view_balance()
    print('-' * 30)
    client1.show_user_details()
