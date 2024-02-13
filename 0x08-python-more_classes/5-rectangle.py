#!/usr/bin/python3

"""
Class rectangele
"""


class Rectangle:
    """rectangle class"""

    def __init__(self, wdth=0, hght=0):
        """initializing class"""
        self.wdth = wdth
        self.hght = hght

    @property
    def wdth(self):
        """Get wdth"""
        return self.__wdth

    @wdth.setter
    def wdth(self, wdthValue):
        """Set wdth"""
        if type(wdthValue) != int:
            raise TypeError("wdth must be an integer")
        if wdthValue < 0:
            raise ValueError("wdth must be >= 0")
        self.__wdth = wdthValue

    @property
    def hght(self):
        """Get hght"""
        return self.__hght

    @hght.setter
    def hght(self, hghtValue):
        """Set hght"""
        if type(hghtValue) != int:
            raise TypeError("hght must be an integer")
        if hghtValue < 0:
            raise ValueError("hght must be >= 0")
        self.__hght = hghtValue

    def area(self):
        """Calculate area"""
        return self.__wdth * self.__hght

    def perimeter(self):
        """Calculate perimeter"""
        wdth = self.__wdth
        hght = self.__hght
        if wdth == 0 or hght == 0:
            return 0
        return (wdth + hght) * 2

    def __str__(self):
        """Get string representation"""
        wdth = self.__wdth
        hght = self.__hght
        string = ""
        if wdth == 0 or hght == 0:
            return string
        for r in range(hght):
            for c in range(wdth):
                string = string + '#'
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        """Get string."""
        wdth = self.__wdth
        hght = self.__hght
        string = "Rectangle(" + str(wdth) + \
            ", " + str(hght) + ")"
        return string

    def __del__(self):
        """deleted"""
        print("Bye rectangle...")
