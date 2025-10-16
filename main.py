from graphics.base.Point import Point

class Main:
    def run(self):
        print("Hello World")

        p1 = Point(1, 2)
        print(p1)

        v = Vector(10, 20)
        p1.move(v)
        print(p1)

        p2 = Point(5, 6)
        print(p2)

if __name__ == "__main__":
    main = Main()
    main.run()