n = int(input("Введите n: "))
count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        count += 1

print("Количество четных:", count)