'''
Book App
'''

class Book:
    '''book class'''
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        '''class initialization'''
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self._price = price
        self.copies = copies

    def display(self):
        '''display info about book'''
        print(f'ISBN: {self.isbn}')
        print(f'Price: {self.price}')
        print(f'Number of copies: {self.copies}')
        print('.' * 50)

    def in_stock(self):
        ''''check the availability of the book'''
        return True if self.copies > 0 else False

    def sell(self):
        '''reduce the number of books after sale'''
        if self.in_stock():
            self.copies -= 1
        else:
            print('The book is out of stock')

    @property
    def price(self):
        '''give the price price of the book'''
        return self._price

    @price.setter
    def price(self, new_price):
        '''change price of the book'''
        if not 50 <= new_price <= 1000:
            raise ValueError ('Price must be between 50 and 1000')
        return self._price


if __name__ == '__main__':
    book1 = Book('546-6-38-567512-1', 'Learn Psychology','Stephen', 'CBC', 350, 200,10)
    book2 = Book('652-6-86-748413-3', 'Learn Physics','Jack', 'CBC', 400, 220,20)
    book3 = Book('957-7-39-347216-2', 'Learn Math','John', 'XYZ', 500, 300,5)
    book4 = Book('957-7-39-347216-2', 'Learn Chemistry','Jack', 'XYZ', 400, 200,6)

    books = [book1, book2, book3, book4]

    for book in books:
        book.display()

    jack_books = [book.title for book in books if book.author == 'Jack']
    print(jack_books)
