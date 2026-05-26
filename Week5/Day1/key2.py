products = [
    {"name":"Phone", "price": 500},
    {"name":"Laptop", "price": 1200},
    {"name":"Mouse", "price": 50},
]

most_expensive = max(products, key = lambda product: product["price"])
print(most_expensive)

