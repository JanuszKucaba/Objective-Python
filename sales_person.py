'''
Sales Person App
'''

class SalesPerson:
    '''sale person class'''
    total_revenue = 0
    names = []

    def __init__(self,name,age):
        '''class initialization'''
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self,money):
        '''sales person make a sale'''
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        '''show name, age and amount'''
        print(self.name, self.age, self.sales_amount)


if __name__ == '__main__':
    s1 = SalesPerson('Jim', 23)
    s2 = SalesPerson('Peter', 32)
    s3 = SalesPerson('Mark', 27)

    s1.make_sale(800)
    s1.make_sale(1200)
    s2.make_sale(4000)
    s3.make_sale(2000)
    s3.make_sale(5000)

    s1.show()
    s2.show()
    s3.show()

    print(SalesPerson.total_revenue)
    print(SalesPerson.names)
