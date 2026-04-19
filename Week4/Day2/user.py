class User:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        parts = data.split(",")
        name = parts[0]
        age = int(parts[1])
        return cls(name,age)

    def __str__(self):
        return f"User: {self.name}, {self.age}"
    
u = User.from_string("Dima, 20")
print(u)