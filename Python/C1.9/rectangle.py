import math

class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height


class Square:
    def __init__(self, width):
	    self.width = width

    def get_area_square(self):
        return self.width ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        return round(self.radius ** 2 * math.pi, 3)