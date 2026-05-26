def parse_numbers(text):
    return [int(x) for x in text.split()]

def find_max(numbers):
    return max(numbers)

def main():
    text = input("Введите числа через пробел: ")
    numbers = parse_numbers(text)
    result = find_max(numbers)
    print(result)

main()
