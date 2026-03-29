def age_def(age):
    if age >= 18:
        return "Можно"
    else:
        return "-"
    
age = int(input("Введите возраст: "))
print(age_def(age))