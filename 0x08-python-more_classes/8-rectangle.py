#!/usr/bin/python3
""" This program defines a class Rectangle """


class Rectangle:
    """ Define all instances for class Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @classmethod
    def change_symbol(cls, value):
        cls.print_symbol = value
        return cls, Rectangle.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        type(self).number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if not self.__height or not self.__width:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        rectangle = ''
        if not self.__height or not self.__width:
            return rectangle
        for row in range(self.__height):
            for column in range(self.__width):
                rectangle += str(self.print_symbol)
            if row < self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        return '{self.__class__.__name__}({self.width}, \
{self.height})'.format(self=self)

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = Rectangle.area(rect_1)
        area2 = Rectangle.area(rect_2)
        if area1 > area2:
            return rect_1
        elif area1 == area2:
            return rect_1
        else:
            return rect_2
