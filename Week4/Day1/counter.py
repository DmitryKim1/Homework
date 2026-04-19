class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def show(self):
        print(f"Value {self.value}")

counter1 = Counter(5)
counter2= Counter(25)

counter1.increment()
counter1.show()
counter2.decrement()
counter2.show()