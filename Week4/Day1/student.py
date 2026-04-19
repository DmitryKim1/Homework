class Student:
    def __init__(self, name, grade):
        self.name= name
        self.grade = grade

    def upgrade(self):
        self.grade += 1

    def downgrade(self):
        self.grade -= 1

    def show_info(self):
        print(f"{self.name} {self.grade}")

alex = Student("Alex", 3)
sam = Student("Sam", 4)

alex.downgrade()

alex.show_info()
sam.show_info()