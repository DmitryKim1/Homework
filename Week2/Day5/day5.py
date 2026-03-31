def sozdat_stroku():
    stroka = input("Введите строку: ")
    return stroka

def normalizaciya(stroka):
    stroka = stroka.lower()
    return stroka

def razbienie(stroka):
    massive = stroka.split()
    return massive

def dlina_spiska(massive):
    return len(massive)

def max_dlina_stroki(massive):
    samoe_dlinnaya_dlina_stroki = 0
    dictionary = {}
    for i in massive:
        tekuschaya_dlina_stroki = len(i)
        if tekuschaya_dlina_stroki > samoe_dlinnaya_dlina_stroki:
            samoe_dlinnaya_dlina_stroki = tekuschaya_dlina_stroki
            dictionary[0] = i
    return dictionary[0]

def number_word(massive):
    count = 0
    slovo = input("Введите слово")
    slovo = slovo.lower().strip()
    for i in massive:
        if i == slovo:
            count += 1

    return count

def slov_dlinnee_poroga(massive):
    count = 0
    porog = int(input("Введите порог "))
    for i in massive:
        if len(i) > porog:
            count += 1
    return count

def main():
    stroka = sozdat_stroku()
    stroka1 = normalizaciya(stroka)
    massive = razbienie(stroka)
    
    print("Строка ", stroka)
    print("Строка нормализованная ", stroka1)
    print("Массив строк", massive)
    print("Длина строки ", dlina_spiska(massive))
    print("Максимальная длина строки", max_dlina_stroki(massive))
    print("Сколько раз слово встречается в массиве ", number_word(massive))
    print("Слов длиннее порога", slov_dlinnee_poroga(massive))

main()