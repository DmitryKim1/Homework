class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
    def show_info(self):
        print(f"Ширина {self.width} Высота {self.height} ")

rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(11, 12)

rectangle1.show_info()
rectangle2.show_info()

print(rectangle1.area())
print(rectangle2.area())

print(rectangle1.perimeter())
print(rectangle2.perimeter())

rectangle2.height = 25
print(rectangle2.height)
