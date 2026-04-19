class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        if percent < 0 or percent >100:
            print("Скидка должна быть от 0 до 100")
            return
        self.price = self.price * (1- percent/100)

    def __str__(self):
        return f"{self.title} - {self.price}$"
    
p = Product("Phone", 500)
print(p)
