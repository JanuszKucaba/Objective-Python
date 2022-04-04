'''
Simple class with first and last name
'''

class Student:
    def __init__(self, first_name, last_name):
        '''class initialization'''
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        '''return first and last name'''
        return f'{self.first_name} {self.last_name}'


if __name__ == '__main__':
    piter = Student(first_name='Piotr', last_name='Muzykant')
    print('Obiekt', piter)
    print('First name', piter.first_name)
    print('Last name', piter.last_name)

    kasia = Student('Karzyna', 'Kowalska')
    print(kasia.first_name, kasia.last_name)
    print(kasia.hello())
