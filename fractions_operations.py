'''
Application for actions with fractions:
- showing fraction
- adding
- multiplying
- highest common factor
'''

class Fraction:
    '''class for actions with fractions'''
    def __init__(self, frac_nr, frac_dr=1):
        '''class initialization'''
        self.frac_nr = frac_nr    # numerator
        self.frac_dr = frac_dr    # denominator
        if self.frac_dr < 0:
            self.frac_nr *= -1
            self.frac_dr *= -1
        self._reduce()

    def show(self):
        '''display fraction'''
        print (f'{self.frac_nr}/{self.frac_dr}')

    def multiply(self, other):
        '''multiply two fractions'''
        if isinstance(other, int):
            other = Fraction(other)
        multi_frac = Fraction(self.frac_nr * other.frac_nr, self.frac_dr * other.frac_dr)
        multi_frac._reduce()
        return multi_frac

    def add(self, other):
        '''add two fractions'''
        if isinstance(other, int):
            other = Fraction(other)
        add_frac = Fraction(
            self.frac_nr * other.frac_dr + other.frac_nr * self.frac_dr,
            self.frac_dr * other.frac_dr
            )
        add_frac._reduce()
        return add_frac

    def _reduce(self):
        '''reduce fraction for hcf'''
        red_frac = Fraction.hcf(self.frac_nr, self.frac_dr)
        if red_frac == 0:
            return

        self.frac_nr //= red_frac
        self.frac_dr //= red_frac


    @staticmethod
    def hcf(x_frac, y_frac):        # highest common factor - najwyższy wspólny dzielnik
        '''compute highest common factor'''
        x_frac = abs(x_frac)
        y_frac = abs(y_frac)
        smaller = y_frac if x_frac > y_frac else x_frac
        s_frac = smaller
        while s_frac > 0:
            if x_frac % s_frac == 0 and y_frac % s_frac == 0:
                break
            s_frac -= 1
        return s_frac


if __name__ == '__main__':
    f1 = Fraction(2,3)
    f1.show()
    f2 = Fraction(3,4)
    f2.show()
    f3 = f1.multiply(f2)
    f3.show()
    f3 = f1.add(f2)
    f3.show()
    f3 = f1.add(5)
    f3.show()
    f3 = f1.multiply(5)
    f3.show()

    print(f1.hcf(1, 2))
