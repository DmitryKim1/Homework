def sozdat_stroku():
    while True:
        stroka = input("Введите строку: ")
        if len(stroka) > 0:
            break
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

def srednya_dlina_slova(massive):
    summa = 0
    for i in massive:
        summa += len(i)

    average = summa/len(massive)
    return average

def main():
    stroka = sozdat_stroku()
    stroka1 = normalizaciya(stroka)
    massive = razbienie(stroka1)
    
    print("Строка ", stroka)
    print("Строка нормализованная ", stroka1)
    print("Массив строк", massive)
    print("Длина строки ", dlina_spiska(massive))
    print("Максимальная длина строки", max_dlina_stroki(massive))
    print("Сколько раз слово встречается в массиве ", number_word(massive))
    print("Слов длиннее порога", slov_dlinnee_poroga(massive))
    print("Средняя длина слова", srednya_dlina_slova(massive))

main()