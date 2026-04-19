# Book Tracker CLI

Консольная программа для работы со списком книг.

## Возможности

* добавить книгу
* показать все книги
* найти книгу по названию или автору
* фильтр по статусу (planned, read, dropped)
* изменить статус книги
* удалить книгу
* посмотреть статистику
* сохранить данные в JSON

## Структура проекта

* `main.py` — меню и работа с пользователем
* `models.py` — модель книги (Book)
* `services.py` — логика работы с книгами
* `storage.py` — загрузка и сохранение JSON
* `tests/` — тесты

## Запуск

Перейти в папку проекта:

```bash
python3 main.py
```

## Тесты

```bash
python3 -m unittest tests/test_services.py
```

## Хранение данных

Данные сохраняются в файл `books.json`.

Пример:

```json
[
  {
    "id": 1,
    "title": "1984",
    "author": "Orwell",
    "genre": "Dystopia",
    "status": "read"
  }
]
```
![Screnshot](screenshots/image.png)