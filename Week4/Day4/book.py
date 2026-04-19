from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: str

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Dune", "Frank Herbert", 1965)

print(book1)
print(book2)