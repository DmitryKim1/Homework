def user_name():
    return input("Введите имя пользователя: ")

def pokupki_def():
    n = int(input("Введите количество покупок: "))
    pokupki = []

    for i in range (n):
        cena = float(input(f"Введите стоимость покупки {i + 1}: "))
        pokupki.append(cena)

    return pokupki

def total_def(pokupki):
    return sum(pokupki)

def average_def(pokupki):
    return sum(pokupki)/ len(pokupki)

def find_max_pokupka(pokupki):
    return max(pokupki)

def kolvo_vishe_granici(pokupki, porog):
    count = 0
    for price in pokupki:
        if price > porog:
            count += 1
    return count

def discount_def(total):
    n = input("Введите да, если нужно применить скидку: ")
    discount = 0.1
    if n == "да":
        final_total = total * (1 - discount)
    else:
        discount = 0
        final_total = total
    return final_total, discount

def main():
    name = user_name()
    pokupki = pokupki_def()

    total = total_def(pokupki)
    average = average_def(pokupki)
    max_pokupka = find_max_pokupka(pokupki)

    porog = float(input("Введите порог: "))
    count = kolvo_vishe_granici(pokupki, porog)

    final_total, discount = discount_def(total)

    print("Имя: ", name)
    print("Общая сумма", total)
    print("Средний чек: ", average)
    print("Самая дорогая покупка:", max_pokupka)
    print("Покупка выше порога:", count)
    print("Скидка:", int(discount*100), "%")
    print("Итог к оплате:", final_total) 

if __name__ == "__main__":
    main()