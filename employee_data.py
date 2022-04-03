'''
Employee data storage app contains employee information about first name,
last name, year of birth, salary and email address from approved domain
'''

class Employee:
    '''employee data storage class'''
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, first_name, last_name, birth_year, salary, email):
        '''class initialization'''
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.salary = salary
        self.email = email
        #domain = email[email.index('@')+1 :]

    @property
    def email(self):
        '''contain an email address'''
        return self._email

    @email.setter
    def email(self, new_mail):
        '''check email domain and change email adress if approved'''
        domain = new_mail[new_mail.index('@')+1 :]
        if domain in Employee.allowed_domains:
            self._email = new_mail
        else:
            raise RuntimeError(f'Domain {domain} is not allowed')

    def show(self):
        '''show employee information'''
        print (f'''I am {self.first_name} {self.last_name}
born in {self.birth_year}
email: {self.email}
--------------------------''')

    def display(self):
        '''display employee first and second name'''
        print(self.first_name, self.email)


if __name__ == '__main__':
    e0 = Employee('Gregor', 'Nonnn', 1980, 25000, 'gregor@gmail.com')
    e1 = Employee('Janusz', 'Abacuk', 1999, 20000, 'janusz@yahoo.com')
    e2 = Employee('Piotr', 'Kowalski', 1990, 5000, 'piotr@outlook.com')
    e3 = Employee('Jill', 'Nowak', 1975, 3500, 'jill@outlook.com')
    e4 = Employee('Ted', 'Novinski', 1995, 10000, 'ted@yahoo.com')

    e0.show()
    e1.show()
    e1.show()
    e2.show()

    e3.email = 'jill@gmail.com'
    e3.display()

    print('-' * 30)
    e4.show()
    try:
        e4.email = 'ted@ymail.com'
        e4.display()
    except RuntimeError:
        print('The domain you want to change is not allowed')
