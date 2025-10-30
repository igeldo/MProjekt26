from __future__ import annotations

from graphics.base import Vector
from graphics.base.Coordinate2D import Coordinate2D

class Point(Coordinate2D):

    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def __add__(self, v: Vector) -> Point:
        return Point(self._x + v.get_x(), self._y + v.get_y())

    def __sub__(self, v: Vector) -> Point:
        x = self._x - v.get_x()
        y = self._y - v.get_y()
        return Point(x, y)

    def __str__(self) -> str:
        return "Point({}, {})".format(self._x, self._y)