from hw2 import Book

if __name__ == "__main__":
    books = []

    def create_data(n):
        for i in range(n):
            x = input("INPUT title, author, isbn, price of your book (in that order only): ")
            y = x.split(',')
            bk = Book(y[0],y[1],y[2],y[3])
            books.append(bk)
        for i in books:
            i.display_info()
            if i != books[-1]:
                print("\n")

    create_data(2)


