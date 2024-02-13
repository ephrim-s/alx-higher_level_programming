#!/usr/bin/python3

"""
class Rectangle
"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """Set width"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, heightValue):
        """Set height"""
        if type(heightValue) != int:
            raise TypeError("height must be an integer")
        if heightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = heightValue
