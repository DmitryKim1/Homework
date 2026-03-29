def range_def(number):
    if 5 <= number <= 10:
        return "В диапозоне"
    else:
        return "Не в диапозоне"
    
n = int(input("Введите число: "))
print(range_def(n))