def minutesdef(seconds):
    minutes = seconds//60
    remainingseconds = seconds%60
    return minutes, remainingseconds

seconds = int(input("Введите секунды"))
m,s  = minutesdef(seconds)

print(f"Минуты = {m}, Секунды = {s}")