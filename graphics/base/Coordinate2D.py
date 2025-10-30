from abc import ABC, abstractmethod

class Coordinate2D(ABC):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    @abstractmethod
    def __str__(self) -> str:
        pass
