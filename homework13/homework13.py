class Figure:
    def __get_square(self):
        pass

    def __get_perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, first_side, second_side):
        self.__first_side = first_side
        self.__second_side = second_side

    def get_square(self):
        result = self.__first_side * self.__second_side
        return result

    def get_perimeter(self):
        result = 2 * (self.__first_side + self.__second_side)
        return result


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_square(self):
        result = 3.14 * self.__radius * self.__radius
        return result

    def get_perimeter(self):
        result = 2 * 3.14 * self.__radius
        return result


class RightTriangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        self.__first_side = first_side
        self.__second_side = second_side
        self.__third_side = third_side

    def get_square(self):
        result = 0.5 * self.__first_side * self.__second_side
        return result

    def get_perimeter(self):
        result = self.__first_side + self.__second_side + self.__third_side
        return result


figure = [Rectangle(23, 123), Rectangle(32, 45), Rectangle(56, 34), Circle(89), Circle(12), Circle(53),
          RightTriangle(3, 4, 5), RightTriangle(5, 12, 13)]

for f in figure:
    print(f'{type(f).__name__} has square = {f.get_square()} and perimeter {f.get_perimeter()}')

