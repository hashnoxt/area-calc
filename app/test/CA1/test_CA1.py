import unittest
from app.src.calculate_area_with_1_inputs import CA1

A: int = 4


class TestCA1(unittest.TestCase):

    def test_square_area(self):
        ca1 = CA1()
        assert ca1.square_area(a=A) == 16

    def test_circle_area(self):
        ca1 = CA1()
        assert ca1.circle_area(r=A) == 50.26548245743669
