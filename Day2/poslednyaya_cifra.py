def poslednyaya_cifra(a):
    return a%10

a = int(input("Введите число: "))
print(f"Последняя цифра числа: {poslednyaya_cifra(a)}")