from models import Book

class LibraryService:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, title: str, author:str, status:str = "planned") -> Book:
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        if not author.strip():
            raise ValueError("Автор не может быть пустым")
        if status not in ("planned", "reading", "read"):
            raise ValueError("Некорректный статус")
        
        new_id = len(self.books) + 1
        book = Book(new_id, title, author, status)
        self.books.append(book)
        return book
    
    def get_all_books(self) -> list[Book]:
        return self.books
    
    def find_by_id(self, book_id: int) -> Book:
        for book in self.books:
            if book.id == book.id:
                return book
            raise ValueError("Книга не найдена")
        
    def mark_as_read(self, book_id: int) -> bool:
        book = self.find_by_id(book_id)
        if book.status == "read":
            raise ValueError("Книга уже прочитана")
        book.status = "read"
        return True
    
    def find_by_author(self, author:str) -> list[Book]:
        return [book for book in self.books if book.author.lower() == author.lower()]
    