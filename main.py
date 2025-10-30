from __future__ import annotations

from graphics.base.Coordinate2D import Coordinate2D
from graphics.base.Point import Point
from graphics.base.Vector import Vector

class Main:

    def run(self):
        print("Hello World")

        p1 = Point(1, 2)

        v1 = Vector(10, 20)
        print(v1)

        p_new = p1 + v1
        print(p_new)

if __name__ == "__main__":
    main = Main()
    main.run()
