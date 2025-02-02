class Book:
    def __init__(self, title=None, author=None, isbn=None, price=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def display_info(self):
        print(f"title: {self.title}\nauthor: {self.author}\nisbn: {self.isbn}\nprice: {self.price}")
    def find_product(self):
        print(f"https://isbnsearch.org/isbn/{str(self.isbn)}")


bk = Book("harry potter", "J.K. Rowling", 9780545162074,250)
bk.find_product()
