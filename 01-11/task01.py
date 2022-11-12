"""File with figure classes."""
from math import pi


class Triangle:
    """The representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float):
        """Initialization method.

        Args:
            side1 (float): the first side of the triangle.
            side2 (float): the second side of the triangle.
            side3 (float): the third side of the triangle.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        x = self.side1 + self.side2 + self.side3
        return float('{:.2f}'.format(x))

    def area(self):
        s_per = self.perimeter() / 2
        x = (s_per * (s_per - self.side1) * (s_per - self.side2) * (s_per 
- self.side3)) ** 0.5
        return float('{:.2f}'.format(x))


class Circle:
    """The representation of circle."""

    def __init__(self, radius: float):
        """Initialization method.

        Args:
            radius (float): the radius of the circle.
        """
        self.radius = radius

    def length(self):
        x = self.radius * pi * 2
        return float('{:.2f}'.format(x))

    def area(self):
        x = (self.radius ** 2) * pi
        return float('{:.2f}'.format(x))

