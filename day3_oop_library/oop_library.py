# Day 3: OOP - Book and Library

class Book():
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"Title of the book is {self.title} written by {self.author} in {self.year}"

    def is_classic(self):
        return 2025 - self.year > 50

book_1 = Book("Last Samurai", "J.K. Kiplling", 1982)
book_2 = Book("8 Miles", "Eminem", 1990)
book_3 = Book("Queens Gambit", "S. King", 1992)

list_of_books = [book_1, book_2, book_3]
for book in list_of_books:
    print(book.description())
    print(f"{book.title} is classic: {book.is_classic()}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book_by_title(self, title):
        self.books = [b for b in self.books if b.title != title]

    def display_books(self):
        for book in self.books:
            print(book.description())

    def get_classic_books(self):
        return [book for book in self.books if book.is_classic()]

my_library = Library()
my_library.add_book(book_1)
my_library.add_book(book_2)
my_library.add_book(book_3)

print("
All Books:")
my_library.display_books()

print("
Removing '8 Miles'...")
my_library.remove_book_by_title("8 Miles")
my_library.display_books()

print("
Classic Books:")
for classic in my_library.get_classic_books():
    print(classic.description())
