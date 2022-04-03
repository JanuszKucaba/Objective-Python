'''
Academic student app can show information about student and increase and decrease the semester
'''

from math import ceil


class InvalidSemester(Exception):
    '''create own exception'''
    pass


class Student:
    '''class Student'''

    def __init__(self, first_name, last_name):
        '''class initialization'''
        self.first_name = first_name
        self.last_name = last_name
        self.semester = 1

    def hello(self):
        '''print first and last name'''
        return f'{self.first_name} {self.last_name}'

    def go_higher(self):
        '''increace semester'''
        self.semester += 1

    def go_down(self):
        '''decrease semester'''
        if self.semester <=1:
            raise InvalidSemester("You can't do it")
        else:
            self.semester -= 1

    @property
    def year(self):
        '''calculates the year of study'''
        return ceil(self.semester/2)


if __name__ == '__main__':
    janek = Student(first_name='Janko', last_name='Muzykant')
    print('Object:', janek)
    print('First name:', janek.first_name)
    print('Last name:', janek.last_name)
    print('Semester:', janek.semester)
    janek.go_higher()
    janek.go_higher()
    print('Semester:', janek.semester)
    print('Rok:', janek.year)

    try:
        piotr = Student('Piotr', 'Muzykant')
        print(piotr.hello())
        piotr.go_down()
    # except Exception as message:
    except InvalidSemester as message:
        print(message)
