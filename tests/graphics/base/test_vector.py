from unittest import TestCase

from graphics.base.Point import Point
from graphics.base.Vector import Vector


class TestVector(TestCase):

    def setUp(self):
        self.cut = Vector(2.0, 3.0)

    def test_str(self):
        # act
        result = self.cut.__str__() # str(self.cut)

        # assert
        self.assertEqual("Vector(2.0, 3.0)", result)

    def test_add(self):
        # arrange
        v = Vector(1.0, 2.0)

        # act
        result = self.cut + v

        # assert
        self.assertEqual(result, Vector(3.0, 5.0))

