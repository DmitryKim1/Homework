from storage import load_tasks, save_tasks
from services import (
    add_task, get_all_tasks,
    get_undone_tasks,
    search_tasks,
    mark_task_done,
    delete_task,
    get_statistics
)
from validators import validate_title, validate_priority

def print_tasks(tasks):
    if not tasks:
        print("Список задач пуст")
        return
    
    for task in tasks:
        status = "done" if task["done"] else "not done"
        print(f'ID: {task["id"]} | {task["title"]} | {status} | {task["priority"]}')

def main():
    tasks = load_tasks()

    while True:
        print("\n     Менеджер задач     ")
        print("1.  Показать все задачи")
        print("2. Показать незавершенные")
        print("3. Добавить задачу")
        print("4. Поиск по слову")
        print("5. Отметить как done")
        print("6. Удалить задачу")
        print("7. Показать статистику")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print_tasks(get_all_tasks(tasks))

        elif choice == "2":
            print_tasks(get_undone_tasks(tasks))

        elif choice == "3":
            title = input("Введите название задачи: ")
            priority = input("Введите приоритет (low/medium/high): ")

            try:
                validate_title(title)
                validate_priority(priority)
                add_task(tasks, title, priority)
                save_tasks(tasks)
                print("Задача добавлена")
            except ValueError as e:
                print("Ошибка:", e)

        elif choice == "4":
            keyword = input("Введите слово для поиска: ")
            found = search_tasks(tasks, keyword)
            print_tasks(found)

        elif choice == "5":
            try:
                task_id = int(input("Введите ID задачи: "))
                result = mark_task_done(tasks, task_id)

                if result is True:
                    save_tasks(tasks)
                    print("Задача отмечена как done")
                elif result == "already done":
                    print("Задача уже была выполнена")
                else:
                    print("Задача не найдена")
            except ValueError:
                print("Введите корректный ID")

        elif choice == "6":
            try:
                task_id = int(input("Введите ID задачи: "))
                result = delete_task(tasks, task_id) 

                if result:
                    save_tasks(tasks)               
                    print("Задача удалена")
                else:
                    print("Задача не найдена")
            except ValueError:
                print("Введите корректный ID")

        elif choice == "7":
            stats = get_statistics(tasks)
            print("Всего задач: ", stats["total"])
            print("Выполнено", stats["done"])
            print("Не выполнено", stats["undone"])
            print("По приоритетам: ", stats["by_priority"])

        elif choice == "0":
            print("Выход из программы")
            break

        else:
            print("Неверный пункт меню")

if __name__ == "__main__":
    main()