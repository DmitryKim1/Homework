from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

class LibraryService:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_all_books(self) -> list[Book]:
        return self.books
    
library = LibraryService()

book1 = Book("1", "a", 1991)
book2 = Book("2", "b", 2005)

library.add_book(book1)
library.add_book(book2)

all_books = library.get_all_books()

for book in all_books:
    print(book)