from models import Book

class LibraryService:
    def __init__(self):
        self.books = []

    def next_id(self):
        if not self.books:
            return 1
        
        return max(book.id for book in self.books) + 1
    
    def add_book(self, title, author, genre):
        book = Book(
            id=self.next_id(),
            title=title,
            author=author,
            genre=genre
        )

        self.books.append(book)
        return book
    
    def get_all_books(self):
        return self.books
    
    def find_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        
        return None
    
    def search_books(self, query):
        result = []
        query = query.lower()

        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                result.append(book)
            
        return result
    
    def filter_by_status(self, status):
        return [book for book in self.books if book.status == status]
    
    def change_status(self, book_id, new_status):
        book = self.find_by_id(book_id)
        if book is None:
            return False
        
        if new_status not in ['planned', 'read', 'dropped']:
            return False
        
        book.status = new_status
        return True
    
    def delete_book(self, book_id):
        book = self.find_by_id(book_id)

        if book is None:
            return False
        
        self.books.remove(book)

        return True
    
    def status_stats(self):
        stats = {
            "planned" : 0,
            "read" : 0,
            "dropped" : 0
        }

        for book in self.books:
            stats[book.status] += 1

        return stats
    
    def genre_stats(self):
        stats = {}

        for book in self.books:
            stats[book.genre] = stats.get(book.genre, 0) + 1

        return stats