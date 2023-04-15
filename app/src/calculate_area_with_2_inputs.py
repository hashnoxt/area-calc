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
