def max_length(limit):
    def decorator(func):
        def wrapper(text):
            if len(text) > limit:
                raise ValueError("Слишком длинная строка")
            return func(text)
        return wrapper
    return decorator

@max_length(5)
def process(text):
    return text.upper()

print(process("hello"))

