import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print("Время:", end - start)
        return result

    return wrapper


@timer
def slow():
    total = 0

    for i in range(100000):
        total += i

    return total


print(slow())