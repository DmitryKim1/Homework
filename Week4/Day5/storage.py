import json
from models import Book

def save_books(filename:str, books: list[Book]) -> None:
    data = []
    for book in books:
        data.append(
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "status": book.status,
            }
        )

    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)

def load_books(filename: str) -> list[Book]:
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    
    books = []
    for item in data:
        books.append(
            Book(
                id = item["id"],
                title = item["title"],
                author = item["author"],
                status = item["status"],
            )
        )

    return books