class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            print("Температура не может быть ниже -273")
            return
        self._celsius = value

    def __str__(self):
        return f"Температура: {self._celsius}C"
    
t = Temperature(20)
print(t)

t.celsius = 30
print(30)

t.celsius = -300
print(t)