def obchaya_stoimost(price, kolvo):
    return price*kolvo

price = float(input("Введите цену: "))
kolvo = int(input("Введите количество: "))

print("Общая цена: ", obchaya_stoimost(price, kolvo))