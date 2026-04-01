def create_list():
    while True:
        n = int(input("Введите количество элементов в массиве: "))
        if n > 0:
            break
    massive = []

    for i in range(n):
        znachenie = int(input("Введите значение элемента: "))
        massive.append(znachenie)

    return massive

def sum_znach(massive):
    if len(massive) > 0:
        return sum(massive)
    else:
        return "У массива нет суммы"

def min_znach(massive):
    if len(massive) > 0:
        return min(massive)
    else:
        return "У массива нет наименьшего значения"

def max_index(massive):
    return massive.index(max(massive))

def num_pos_integer(massive):
    count = 0
    for i in massive:
        if i > 0:
            count +=1
    return count

def every_second_element(massive):
    return massive[0::2]

def main():
    massive = create_list()

    print("Массив", massive)
    print("Сумма значений в массиве", sum_znach(massive))
    print("Минимальное значение в массиве", min_znach(massive))
    print("Индекс максимального значения в массиве", max_index(massive))
    print("Число положительныех значений в массиве", num_pos_integer(massive))
    print("Выводит каждый 2 элемент в массиве", every_second_element(massive))

main()
