class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_order(self):
        print(f"Клиент: {self.customer.name}")
        print("Товары: ")
        for item in self.items:
            print(item)

cust = Customer("Dima")
order = Order(cust)

order.add_item("Laptop")
order.add_item("Mouse")

order.show_order()
