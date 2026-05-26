def log_args(func):
    def wrapper(*args, **kwargs):
        print("args: ", args)
        print("kwargs: ", kwargs)
        return func(*args, **kwargs)
    return wrapper


@log_args
def add(a, b):
    return a + b

print(add(2, 3))