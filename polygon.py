import math
from point import *
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

    def normalize_polygon(self, w, h, dx, dy):
        px = [p.x for p in self.points]
        py = [p.y for p in self.points]

        min_px, max_px, min_py, max_py = min(px), max(px), min(py), max(py)

        for p in self.points:
            p.x = w * (p.x - min_px)/(max_px - min_px) + dx
            p.y = h * (p.y - min_py)/(max_py - min_py) + dy

    def get_far_left_point(self):
        far_left_point = self.points[0]
        far_left_point_ind = 0

        for ind in range(len(self.points)):
            point = self.points[ind]
            if point.x < far_left_point.x or (point.x == far_left_point.x and point.y < far_left_point.y):
                far_left_point = point
                far_left_point_ind = ind

        return far_left_point, far_left_point_ind

    def is_ear(self, triangle):
        answer = True
        cut_point = Point(10**6, 10**6)
        cut_point_index = -1

        for ind in range(len(self.points)):
            point = self.points[ind]
            is_part = False
            
            for p in triangle.points:
                if p.x == point.x and p.y == point.y:
                    # The point belongs to the triangle test
                    is_part = True

            if triangle.is_inside(point) and not is_part:
                answer = False
                if point.x < cut_point.x or (point.x == cut_point.x and point.y < cut_point.y):
                    cut_point = point
                    cut_point_index = ind
        
        return answer, cut_point_index

    def divide_polygon_by_diagonal(self, diagonal):
        d0, d1 = diagonal[0], diagonal[1]

        point_list = []
        ind = d0
        while not ind == d1:
            point_list.append(self.points[ind])
            ind = (ind + 1) % self.get_size()
        point_list.append(self.points[d1])

        p1 = Polygon(point_list, self.color)
        point_list = []

        ind = d1
        while not ind == d0:
            point_list.append(self.points[ind])
            ind = (ind + 1) % self.get_size()
        point_list.append(self.points[d0])
        p2 = Polygon(point_list, self.color)

        return p1, p2


    def polygon_triangulation(self, triangle_array):
    
        # Stopping condition
        if self.get_size() == 3:
            triangle_array.append(Triangle(self.points[0], self.points[1], self.points[2], self.color))
            return

        far_left_point, far_left_point_ind = self.get_far_left_point()

        test_triangle = Triangle(far_left_point, 
                        self.points[(far_left_point_ind-1) % self.get_size()],
                        self.points[(far_left_point_ind+1) % self.get_size()], self.color)
        
        ans, cut_point_index = self.is_ear(test_triangle)
        if ans:
            diagonal = [ (far_left_point_ind-1) % self.get_size(), (far_left_point_ind+1) % self.get_size() ]
        else:
            diagonal = [ far_left_point_ind, cut_point_index ]

        p1, p2 = self.divide_polygon_by_diagonal(diagonal)
        p1.polygon_triangulation(triangle_array)
        p2.polygon_triangulation(triangle_array)


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

    def get_point_as_list(self, index):
        return [self.points[index].x, self.points[index].y]

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