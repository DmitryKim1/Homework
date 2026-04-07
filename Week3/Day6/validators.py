def validate_title(title):
    if not title.strip():
        raise ValueError("Название задачи не может быть пустым")
    
def validate_priority(priority):
    allowed = {"low", "medium", "high"}
    if priority not in allowed:
        raise ValueError("Приоритет должен быть low, medium или high")
    
def validate_task_id(task_id):
    if task_id <= 0:
        raise ValueError("Id должен быть положительным числом")
    