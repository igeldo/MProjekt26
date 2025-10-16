class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, deltaX, deltaY):
        self._x += deltaX
        self._y += deltaY

    def __str__(self):
        return "Point({}, {})".format(self._x, self._y)