'''
Product Store App
'''

class Product():
    '''product store class'''
    def __init__(self, product_id, marked_price, discount):
        '''class initialization'''
        self.product_id = product_id
        self.marked_price = marked_price
        self._discount = discount

    def display(self):
        '''display product product_id, price and discount'''
        print(self.product_id,  self.marked_price,  self.discount)

    @property
    def selling_price(self):
        '''selling price after discount'''
        return  self.marked_price - self.marked_price * self.discount/100

    @property
    def discount(self):
        '''extra 2% product discoun if price is more than 500'''
        return  self._discount + 2 if self.marked_price > 500 else self._discount

    @discount.setter
    def discount(self, new_discount):
        '''product discount'''
        self._discount = new_discount

if __name__ == '__main__':

    p1 = Product('X879', 400, 6)
    p2 = Product('A234', 100, 5)
    p3 = Product('B987', 990, 4)
    p4 = Product('H456', 800, 6)

    products = [p1, p2, p3, p4]

    for product in products:
        product.display()

    print('-' * 30)

    print(p1.product_id, p1.selling_price)
    print(p2.product_id, p2.selling_price)
    print(p3.product_id, p3.selling_price)
    print(p4.product_id, p4.selling_price)

    p4.discount = 10

    print(p4.product_id, p4.selling_price)
