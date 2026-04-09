def validate_title(title):
    if not title.strip():
        raise ValueError("Название не может быть пустым")
    
def validate_priority(priority):
    allowed = {"low", "medium", "high"}
    if priority not in allowed:
        raise ValueError("Недопустимый приоритет")