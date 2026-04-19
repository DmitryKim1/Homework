from services import LibraryService
from storage import load_books, save_books

def main():
    service = LibraryService()
    service.books = load_books("data/books.json")

    try:
        service.add_book("1984", "G", "planned")
        service.add_book("Dune", "Frank Herbert", "reading")
        service.mark_as_read(1)

        print("Список книг: ")
        for book in service.get_all_books():
            print(book)

        save_books("data/books.json", service.get_all_books())

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()