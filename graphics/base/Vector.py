import math


class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Vector ({self._x}, {self._y})"

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


    def length(self):
        return math.sqrt(self.get_x()**2 + self.get_y()**2)

    def angle_rad(self):
        return math.atan2(self._y, self._x)

    def angle_deg(self):
        return math.degrees(math.atan2(self._y, self._x))

    def polar_form_as_string(self):
        return f"{self.__str__()}: len = {self.length()} | angle = {self.angle_deg()}° or {self.angle_rad()/math.pi}pi"