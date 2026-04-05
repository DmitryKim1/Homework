def statistika_ocenok(massive):
    count_5= 0

    for i in massive:
        if i == 5:
            count_5 += 1

    srednee = sum(massive)/len(massive)

    return f"Количество пятерок {count_5}, среднее {srednee}"

def cifr_bukv(stroka):
    count_cifr = 0
    count_bukv = 0

    for i in stroka:
        if i.isdigit():
            count_cifr += 1
        if i.isalpha():
            count_bukv += 1

    return f"Цифр {count_cifr}, Букв {count_bukv}"

def odinnakovaya_stroka(stroka):
    stroka1 = input("Введите строку: ")
    if stroka.lower() == stroka1.lower():
        return True
    return False

def massive_bez_povtorov(massive):
    new_list = []
    for i in massive:
        if i not in new_list:
            new_list.append(i)
    return new_list

def ostanovka_na_oshibke(stroka):
    for i in stroka:
        if i.isdigit():
            return False
    
    return True


def main():
    massive = [1, 2, 3 ,4, 5]
    stroka = "abc123"

    print("Статистика оценок:", statistika_ocenok(massive))
    print(cifr_bukv(stroka))
    print("Одиннаковая ли строка: ", odinnakovaya_stroka(stroka))
    print("Массив без повторов ", massive_bez_povtorov(massive))
    print("Строка без цифр", ostanovka_na_oshibke(stroka))

main()

