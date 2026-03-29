def triangle(a,b,c):
    if a + b >c and a+ c > b and b+c > a:
        return "Существует"
    else:
        return "Не существует"
    
a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))

print(triangle(a,b,c))