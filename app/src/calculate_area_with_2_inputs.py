from app.src.base import Area


class CA2(Area):
    """Ideal class for calculate area of objects which can be calculated area
     using minimum of two inputs"""

    @staticmethod
    def triangle_area(a: float, b: float) -> float:
        """Calculate area of the triangle.
        a = height of the triangle
        b = width of the base
        """
        area = (1 / 2) * a * b
        return area

    @staticmethod
    def rectangle_area(a: float, b: float):
        """Calculate area of the rectangle
        a = height of the rectangle
        b = width of the rectangle
        """
        area = a * b
        return area
