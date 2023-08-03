#!/usr/bin/python3

""""
    This class represent a Square with a given size.
    Attribute:
       _size(int): The size of the square(private attribute).
    """


class Square:
    """"
    This class represent a Square with a given size.
    Attribute:
       _size(int): The size of the square(private attribute).
    """

    def __init__(self, size=0):
        """
        Initialize a Square object with a given size

        Args:
            size(int): The size of the Square
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.
        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.__size

    def get_size(self):
        """
        Gets the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, new_size):
        """
        Sets the size of the square to a new value.
        Args:
            new_size (int): The new size to set.
        Raises:
            ValueError: If the new size is negative.
        """
        if not new_size(int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size
