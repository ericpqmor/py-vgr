import math
import random
import polygon
import point

def generate_convex_polygon(n):
    r = 100 # Radius

    color_array = [('255','0','0'),('0','255','0'),('0','0','255'),('255','0','0'),('255','255','0'),('255','0','255'),('0','255','255'),('0','0','0')]

    point_list = []

    for i in range(n):
        point_list.append(point.Point(r * math.cos(2 * math.pi * i/n), r * math.sin (2 * math.pi * i/n)))

    color = random.choice(color_array)
    return polygon.Polygon(point_list, color)

def generate_non_convex_polygon(n):
    color_array = [('255','0','0'),('0','255','0'),('0','0','255'),('255','0','0'),('255','255','0'),('255','0','255'),('0','255','255'),('0','0','0')]

    point_list = []

    for i in range(n):
        r = random.uniform(0,100) + 10
        point_list.append(point.Point(r * math.cos(2 * math.pi * i/n), r * math.sin (2 * math.pi * i/n)))

    color = random.choice(color_array)
    return polygon.Polygon(point_list, color)