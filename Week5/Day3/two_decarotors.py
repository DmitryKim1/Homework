def log(func):
    def wrapper(*args, **kwargs):
        print("Вызов")
        return func(*args, **kwargs)
    return wrapper

def double(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@log
@double
def add(a, b):
     return a + b

print(add(2, 3))