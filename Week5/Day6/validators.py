from datetime import datetime

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Сумма должна быть не больше 0")
    return True

def validate_type(record_type):
    if record_type not in ["income", "expense"]:
        raise ValueError("Тип должен быть income или expense")
    return True

def parse_date(date_string):
    try:
        return datetime.strptime(date_string,"%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Дата должна быть в формате YYYY-MM-DD")