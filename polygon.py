import math
import point
from util import sign, distance

class Polygon:
    def __init__(self,p_arr,color):
        self.points = p_arr
        self.color = color
 
    def get_size(self):
        return len(self.points)

    def is_inside(self, point):
        count = 0

        for vertex in range(self.get_size()):
            if point.ray_intersects_segment(self.points[vertex], self.points[(vertex + 1) % self.get_size()]):
                count += 1

        return count % 2 == 1


class Triangle(Polygon):
    def __init__(self, p1, p2, p3, color):
        self.points = [p1, p2, p3]
        self.color = color

    def get_area(self):
        a = distance(p1,p2)
        b = distance(p1,p3)
        c = distance(p2,p3)

        s = (a + b + c) / 2.0
        return math.sqrt(s * (s-a) * (s-b) * (s-c))

    def is_inside(self, point):
        d1 = sign(point, self.points[0], self.points[1])
        d2 = sign(point, self.points[1], self.points[2])
        d3 = sign(point, self.points[2], self.points[0])

        has_neg = d1<0 or d2<0 or d3<0
        has_pos = d1>0 or d2>0 or d3>0

        return not (has_neg and has_pos)

class Circle:
    def __init__(self, radius, center, color):
        self.center = center
        self.radius = radius
        self.color = color

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def is_inside(self, point):
        return distance(point, self.center) < self.radius