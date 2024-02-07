#!/usr/bin/python3
"""magic class"""
import math


class MagicClass:
    """bytecode magic class maker"""

    def __init__(self, radius=0):
        """starts class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """calculate area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """cal culate other nums"""
        return (2 * math.pi) * self.__radius
