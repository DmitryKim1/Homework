n = int(input("Сколько чисел: "))
s = 0

for i in range(n):
    x = int(input("Введите число: "))
    if x > 0:
        s += x

print("Сумма положительных чисел:", s)