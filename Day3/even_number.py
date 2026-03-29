def even(number):
    if number % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"
    
n = int(input("Введите число: "))
print(even(n))


