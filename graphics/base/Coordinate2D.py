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

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
