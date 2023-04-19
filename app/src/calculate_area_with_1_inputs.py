from app.src.base import Area
from math import pi


class CA1(Area):
    """Ideal class for calculate area of objects which
    need only input"""

    @staticmethod
    def square_area(a: float):
        """Calculate area of the square"""
        area: float = a * a
        return area

    @staticmethod
    def circle_area(r: float):
        """Calculate area of a circle"""
        area: str = '{0:.2f}'.format(pi * r ** 2)
        return float(area)
