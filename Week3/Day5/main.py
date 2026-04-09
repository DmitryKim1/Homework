from day5_storage import load_tasks, save_tasks
from day5_services import add_task
from day5_validators import validate_title, validate_priority

def main():
    tasks = load_tasks()

    title = input("Введите название задачи: ")
    priority = input("Введите приоритет (low/medium/high): ")

    try:
        validate_title(title)
        validate_priority(priority)
        add_task(tasks, title, priority)
        save_tasks(tasks)
        print("Задача добавлена")
    except ValueError as e:
        print("Ошибка: ", e)

if __name__ == "__main__":
    main()