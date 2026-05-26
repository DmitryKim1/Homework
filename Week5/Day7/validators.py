from datetime import datetime

def validate_type(record_type):
    if record_type not in ["income", "expense"]:
        raise ValueError("type должен быть income или expense")
    
def validate_amount(amount):
    if amount <= 0:
        raise ValueError("amount должен быть больше 0")
    
def validate_date(date):
    try:
        datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        raise ValueError("date должен быть в формате YYYY-MM-DD")
    
    