import unittest
from app.src.calculate_area_with_2_inputs import CA2

A: int = 2
B: int = 4


class TestCA2(unittest.TestCase):

    def test_triangle_area(self):
        ca2 = CA2()
        assert ca2.triangle_area(a=A, b=B) == 4
