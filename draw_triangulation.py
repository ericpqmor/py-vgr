# -*- coding: utf-8 -*-
import sys
import time
from draw_functions import *

pygame.init()
screen_width = 7000
screen_height = 7000
x_margin = 10
y_margin = 10
sys.setrecursionlimit(15000)

# Reading entries from command line args
entries = sys.argv[1:]
# triangles = [polygon.Triangle(Point(0,0), Point(50,50), Point(100,0), (0,0,0))]
triangles = []

start_time = time.time()

# Getting data from entries
for entry in entries:
    triangles_entry = []

    new_shape = get_shape_from_entry(entry)
    new_shape.normalize_polygon(screen_width - 2*x_margin, screen_height - 2*y_margin, x_margin, y_margin)
    new_shape.polygon_triangulation(triangles_entry)
    triangles.append(triangles_entry)

for i in range(len(triangles)):
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255,255,255))
    triangle_entry = triangles[i]

    for triangle in triangle_entry:
        pygame.draw.line(screen, (0,0,0), triangle.get_point_as_list(0), triangle.get_point_as_list(1), 1)
        pygame.draw.line(screen, (0,0,0), triangle.get_point_as_list(1), triangle.get_point_as_list(2), 1)
        pygame.draw.line(screen, (0,0,0), triangle.get_point_as_list(2), triangle.get_point_as_list(0), 1)

    text = 'output/' + entries[i][5:-4] + '_triangulation.png'
    screen = pygame.transform.flip(screen, True, True)
    pygame.image.save(screen, text)

elapsed_time = time.time() - start_time
print("Elapsed time = " + str(elapsed_time))