def no_negative(func):
    def wrapper(*args, **kwargs):
        for x in args:
            if isinstance(x, (int, float)) and x < 0:
                raise ValueError("Отрицательное число")
            
        return func(*args, **kwargs)
    
    return wrapper

@no_negative
def multiply(a, b):
    return a * b

print(multiply(2, 3))