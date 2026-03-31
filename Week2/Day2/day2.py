def create_list():
    n = int(input("Введите количество значений в массиве: "))
    massive = []

    for i in range(n):
        znachenie = int(input("Введите значение "))
        massive.append(znachenie)

    return massive

def kolvo_pos_neg_zeros(massive):
    pos = 0
    neg = 0
    zeros = 0
    for i in massive:
        if i > 0:
            pos += 1
        elif i< 0:
            neg += 1
        else:
            zeros += 1
    return pos, neg, zeros

def poisk_x(massive):
    x = int(input("Введите число которое хотите найти: "))
    if x in massive:
        return "Число найдено"
    else:
        return "Такого числа нет в массиве"

def kolvo_vhojdenii(massive):
    count = 0
    number = int(input("Введите число, чтобы узнать сколько раз оно встречается в массиве: "))

    for i in massive:
        if i == number:
            count += 1

    if count > 0:
        return f"Встречается {count}"
    else:
        return "Такого числа нет в массиве"

def index_max(massive):
    return massive.index(max(massive))

def sum_even_not_even_numbers(massive):
    sum_even = sum(massive[0::2])
    sum_not_even = sum(massive[1::2])
    return sum_even, sum_not_even

def sortirovka(massive):
    for i in range(len(massive)-1):
        if massive[i] > massive[i+1]:
            return False
    return True
    
def main():
    massive = create_list()

    print("Массив", massive)
    print("Количество положительных отрицательных нулей", kolvo_pos_neg_zeros(massive))
    print("Поиск числа", poisk_x(massive))
    print("Количество вхождений числа в массив", kolvo_vhojdenii(massive))
    print("Индекс максимального числа в массиве", index_max(massive))
    print("Четные нечетные суммы", sum_even_not_even_numbers(massive))
    print("Отсортирован ли массив в порядке возрастания", sortirovka(massive))

main()
