class Polygon:
    def __init__(self, sides):
        self.n = sides
        self.sides = list()

    def input_sides(self):
        while True:
            self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]
            if max(self.sides) < sum(self.sides) / 2:
                break
            print("It's impossible to create a polygon, try again")
    def disp_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %s' % area)


class Right_Tr(Triangle):
    def __init__(self):
        Triangle.__init__(self)

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n - 1)]
        self.sides.append((self.sides[0] ** 2 + self.sides[1] ** 2) ** 0.5)


rat = Right_Tr()
rat.input_sides()
rat.disp_sides()
rat.area()