'''
Circle App
'''
from math import pi

class Circle:
    '''circle class'''
    def __init__(self, radius):
        '''class initialization'''
        self.radius = radius                        # promień

    @property
    def radius(self):
        '''radius of the circle'''
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        '''changes the radius of the circle'''
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError('Radius should be positive')

    @property
    def area(self):                                 # powierzchnia
        '''calculates the area of the circle'''
        return pi * self._radius * self._radius

    @property
    def diameter(self):                             # średnica
        '''calculates the diameter of the circle'''
        return self._radius * 2

    @property
    def circumference(self):                        # obwód
        '''calctulates the circumference of the circle'''
        return 2 * pi * self._radius


if __name__ == '__main__':
    c1 = Circle(10)

    print(c1.radius)
    print(c1.area)
    print(c1.diameter)
    print(c1.circumference)

    c2 = Circle(7)
    print(c2.radius, c2.diameter, c2.circumference, c2.area )
