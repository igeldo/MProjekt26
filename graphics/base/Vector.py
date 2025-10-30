from __future__ import annotations

from graphics.base.Coordinate2D import Coordinate2D


class Vector(Coordinate2D):

    def __init__(self, x, y):
        super().__init__(x, y)

    def __add__(self, v: Vector) -> Vector:
        return Vector(self._x + v.get_x(), self._y + v.get_y())

    def __mul__(self, s: float) -> Vector:
        return Vector(self._x * s, self._y * s)

    def __str__(self) -> str:
        return "Vector({}, {})".format(self._x, self._y)