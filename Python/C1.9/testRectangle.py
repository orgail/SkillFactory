from rectangle import Rectangle, Square, Circle

# r1 = Rectangle(10, 5)
#
# print("r1.width =", r1.width)
# print("r1.height =", r1.height)
# print("r1.get_width =", r1.get_width())
# print("r1.get_height =", r1.get_height())
# print("r1.get_area =", r1.get_area())
# print('-----')
# r2 = Rectangle(6, 8)
#
# print("r2.width =", r2.width)
# print("r2.height =", r2.height)
# print("r2.get_width =", r2.get_width())
# print("r2.get_height =", r2.get_height())
# print("r2.get_area =", r2.get_area())
# print('-----')

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
#вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), ',',
      square_2.get_area_square())


figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circle_1 = Circle(4)
circle_2 = Circle(8)

print('circle_1 = ', circle_1.get_area_circle())
print('circle_2 = ', circle_2.get_area_circle())
