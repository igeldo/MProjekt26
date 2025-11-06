from unittest import TestCase

from graphics.base.Point import Point
from graphics.base.Vector import Vector


class TestPoint(TestCase):

    def setUp(self):
        self.cut = Point(2.0, 3.0)

    def test_str(self):
        # act
        result = self.cut.__str__() # str(self.cut)

        # assert
        self.assertEqual("Point(2.0, 3.0)", result)

    def test_add(self):
        # arrange
        v = Vector(1.0, 2.0)
        v2 = Vector(3.0, 4.0)

        # act
        result = self.cut + v

        # assert
        self.assertTrue(isinstance(result, Point))
        self.assertEqual(result.get_x(), 3.0)
        self.assertEqual(result.get_y(), 5.0)

    def test_add_2(self):
        # arrange
        p = Point(5.0, 6.0)
        v = Vector(1.0, 2.0)

        # act
        result = p + v

        # assert
        self.assertTrue(isinstance(result, Point))
        self.assertEqual(result.get_x(), 6.0)
        self.assertEqual(result.get_y(), 8.0)

    def test_add_3(self):
        # arrange
        v = Vector(1.0, 2.0)

        # act
        result = self.cut + v

        # assert
        self.assertEqual(result, Point(3.0, 5.0))

