numbers = [10, 20, 30]

it = iter(numbers)

while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break

