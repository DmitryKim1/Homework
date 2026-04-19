import json
from dataclasses import asdict
from models import Book

class JsonStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_books(self, books):
        data = [asdict(book) for book in books]

        with open(self.filename, "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_books(self):

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

        except FileNotFoundError:
            return []
        
        except json.JSONDecodeError:
            return []
        
        books = []
        for item in data:

            books.append(Book(**item))

        return books