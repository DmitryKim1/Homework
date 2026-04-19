class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

book1 = Book("1984", "Orwell")
book2 = Book("Dune", "Herbert")

lib = Library()
lib.add_book(book1)
lib.add_book(book2)

lib.show_books()