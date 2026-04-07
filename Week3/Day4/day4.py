def safe_input_number():
    try:
        number = int(input("Введите число: "))
        return number
    except ValueError:
        print("Ошибка: нужно ввести целое число")
        return None
    
def read_file(filename):
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return ""
    
def get_value(data, key):
    try:
        return data[key]
    except KeyError:
        print("Ошибка: такого ключа нет")
        return None
    
def parse_numbers(lines):
    numbers = []

    for line in lines:
        try:
            numbers.append(int(line))
        except ValueError:
            print(f"Пропуская битую строку: {line}")

    return numbers