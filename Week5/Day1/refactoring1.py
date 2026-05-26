def calculate_discount(price):
    if price > 1000:
        return price * 0.9
    return price

def main():
    price = int(input("Введите цену: "))
    result = calculate_discount(price)
    print(result)

main()
