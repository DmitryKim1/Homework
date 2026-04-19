from services import LibraryService
from storage import JsonStorage


VALID_STATUSES = ["planned", "read", "dropped"]


def print_books(books):
    if not books:
        print("Список пуст")
        return

    for book in books:
        print(f"{book.id}. {book.title} - {book.author} | {book.genre} | {book.status}")


def show_menu():
    print()
    print("1. Показать книги")
    print("2. Закрыть")
    print("3. Добавить книгу")
    print("4. Найти книгу")
    print("5. Найти книги по статусу")
    print("6. Изменить статус книги по id")
    print("7. Удалить книгу")
    print("8. Показать статистику")


def input_book_id():
    try:
        return int(input("Введите id: ").strip())
    except ValueError:
        print("Нечисловой id")
        return None


def handle_show_books(service):
    print_books(service.get_all_books())


def handle_add_book(service):
    title = input("Введите название: ").strip()
    author = input("Введите автора: ").strip()
    genre = input("Введите жанр: ").strip()

    if not title or not author or not genre:
        print("Поля не должны быть пустыми")
        return

    book = service.add_book(title, author, genre)
    print(f"Книга добавлена: {book.title}")


def handle_search_books(service):
    query = input("Введите название книги или автора: ").strip()

    if not query:
        print("Запрос не должен быть пустым")
        return

    found_books = service.search_books(query)
    print_books(found_books)


def handle_filter_by_status(service):
    status = input("Введите статус: ").strip().lower()

    if status not in VALID_STATUSES:
        print("Неверный статус")
        return

    result = service.filter_by_status(status)
    print_books(result)


def handle_change_status(service):
    book_id = input_book_id()

    if book_id is None:
        return

    new_status = input("Введите новый статус: ").strip().lower()

    if new_status not in VALID_STATUSES:
        print("Неверный статус")
        return

    flag = service.change_status(book_id, new_status)

    if flag:
        print("Статус изменен")
    else:
        print("Книга с таким id не найдена")


def handle_delete_book(service):
    book_id = input_book_id()

    if book_id is None:
        return

    flag = service.delete_book(book_id)

    if flag:
        print("Книга удалена")
    else:
        print("Книга не найдена")


def handle_show_stats(service):
    print("Статистика по статусам:")
    status_stats = service.status_stats()
    for status, count in status_stats.items():
        print(f"{status}: {count}")

    print("Статистика по жанрам:")
    genre_stats = service.genre_stats()
    for genre, count in genre_stats.items():
        print(f"{genre}: {count}")


def main():
    storage = JsonStorage("books.json")
    service = LibraryService()
    service.books = storage.load_books()

    print("Книги загружены")

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            handle_show_books(service)
        elif choice == "2":
            storage.save_books(service.books)
            print("Данные сохранены. Выход.")
            break
        elif choice == "3":
            handle_add_book(service)
        elif choice == "4":
            handle_search_books(service)
        elif choice == "5":
            handle_filter_by_status(service)
        elif choice == "6":
            handle_change_status(service)
        elif choice == "7":
            handle_delete_book(service)
        elif choice == "8":
            handle_show_stats(service)
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()