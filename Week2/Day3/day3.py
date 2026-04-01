def stroka_def():
    while True:
        stroka = input("Введите строку: ")
        if len(stroka) > 0:
            break
    return stroka

def dlina_stroki(stroka):
    dlina = len(stroka)
    return dlina

def first_and_last_symbol(stroka):
    first = stroka[0]
    last = stroka[-1]
    return f"{first}, {last}"

def kolvo_probelov_glasnih(stroka):
    count = 0
    glasnie_i_probel = ["a","e","y","u","i","o"," "]
    for i in stroka:
        if i in glasnie_i_probel:
            count += 1
    
    return count

def iniciali_def(stroka):
    massive_strok = stroka.split()
    iniciali = ""

    for i in massive_strok:
        iniciali += i[0]
        iniciali += " "

    iniciali = iniciali.rstrip()

    return iniciali

def palindrom_def(stroka):
    final = stroka.lower().replace(" ", "")
    
    if final == final[::-1]:
        return True
    
    return False
    
def max_dlina_stroki(stroka):
    sam_dlin_slovo = {}
    massive_strok = stroka.split()
    samoe_dlinnaya_dlina_stroki = 0
    for i in massive_strok:
        tekuschaya_dlina_stroki = len(i)
        if tekuschaya_dlina_stroki > samoe_dlinnaya_dlina_stroki:
            samoe_dlinnaya_dlina_stroki = tekuschaya_dlina_stroki
            sam_dlin_slovo[0] = i
    return sam_dlin_slovo[0]

def main():

    stroka = stroka_def()

    print("Строка: ", stroka)
    print("Длина строки", dlina_stroki(stroka))
    print("Первый и последний символ строки", first_and_last_symbol(stroka))
    print("Количество пробелов и гласных в строке: ", kolvo_probelov_glasnih(stroka))
    print("Инициалы: ", iniciali_def(stroka))
    print("Палиндром ли?", palindrom_def(stroka))
    print("Максмимальная длина слова в строке: ", max_dlina_stroki(stroka))

main()
