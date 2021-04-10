class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = str(x)
        self.y = str(y)
        self.width = str(width)
        self.height = str(heigth)

    def get_rectangle(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'

figure = Rectangle(5, 10, 50, 100)

print(figure.get_rectangle())
