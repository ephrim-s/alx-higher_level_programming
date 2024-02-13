#!/usr/bin/python3
# 4-rectangle.py
# Asmamaw Yismaw
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, wdth=0, hght=0):
        """Initialize a new Rectangle.
        Args:
            wdth (int): The wdth of the new rectangle.
            hght (int): The hght of the new rectangle.
        """
        self.wdth = wdth
        self.hght = hght

    @property
    def wdth(self):
        """Get/set the wdth of the Rectangle."""
        return self.__wdth

    @wdth.setter
    def wdth(self, value):
        if not isinstance(value, int):
            raise TypeError("wdth must be an integer")
        if value < 0:
            raise ValueError("wdth must be >= 0")
        self.__wdth = value

    @property
    def hght(self):
        """Get/set the hght of the Rectangle."""
        return self.__hght

    @hght.setter
    def hght(self, value):
        if not isinstance(value, int):
            raise TypeError("hght must be an integer")
        if value < 0:
            raise ValueError("hght must be >= 0")
        self.__hght = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__wdth * self.__hght)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__wdth == 0 or self.__hght == 0:
            return (0)
        return ((self.__wdth * 2) + (self.__hght * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__wdth == 0 or self.__hght == 0:
            return ("")

        rect = []
        for i in range(self.__hght):
            [rect.append('#') for j in range(self.__wdth)]
            if i != self.__hght - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__wdth)
        rect += ", " + str(self.__hght) + ")"
        return (rect)
