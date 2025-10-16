from graphics.base.Vector import Vector

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, deltaX, deltaY):
        self._x += deltaX
        self._y += deltaY

    def move_by_vector(self, v:Vector):
        self._x += v.get_x()
        self._y += v.get_y()

    def __str__(self):
        return "Point({}, {})".format(self._x, self._y)