class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, {self.name}")

    def show_info(self):
        print(f"Name: {self.name}, age: {self.age}")


user1 = User("Dima", 28)
user2 = User("Sasha", 30)

user1.say_hello()
user1.show_info()
user2.show_info()

user1.age = 25

print("После изменения")
user1.show_info()
user2.show_info()