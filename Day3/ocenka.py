def ocenka(skolko):
    if skolko >= 80:
        return "pyat"
    if skolko >= 65:
        return "chetire"
    if skolko >= 50:
        return "tri"
    else:
        return " "

balli = int(input("Введите баллы"))
print("Оценка: ", ocenka(balli))