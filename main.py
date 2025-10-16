from graphics.base.Point import Point, Vector

class Main:
    def run(self):
        print("Hello World")

        p1 = Point(1, 2)
        print(p1)

        v = Vector(1, 1)
        print(v)
        print(v.polar_form_as_string())

        p1.move_by_vector(v)
        print(p1)

        p2 = Point(5, 6)
        print(p2)

if __name__ == "__main__":
    main = Main()
    main.run()