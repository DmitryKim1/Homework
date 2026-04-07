def chastota():
    text = input("Введите строку")
    freq = {}
    
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 0
        
    return freq

def uniq():
    text = input("Введите строку")
    words = text.lower().split()
    return set(words)

def create_phone_book(n):
    phone_book = {}
    for _ in range(n):
        name = input("Введите имя: ")
        number = input("Введите телефон")
        phone_book[name] = number
    
    return phone_book

def find_name(phone_book, name):
    return phone_book.get(name,"Не найдено")

def obschie_slova(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    return set1&set2

def duplicates_freq_def(numbers):
    freq = {}
    for i in numbers:
        freq[i] = freq.get(i, 0) + 1
    
    dubplicates =  {}
    for key,value in freq.items():
        if value > 1:
             dubplicates[key] = value
    
    return dubplicates