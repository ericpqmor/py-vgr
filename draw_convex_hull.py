# -*- coding: utf-8 -*-
import sys
import time
sys.path.insert(1, 'lib')
from draw_functions import *
from convex_hull import *
from polygon_generator import *
import pylab

pygame.init()
screen_width = 700
screen_height = 700
x_margin = 70
y_margin = 70

# Reading entries from command line args
# entries = sys.argv[1:]
shapes = []
convex_hulls = []
x_time = []
y_time = []
start_time = time.time()

# Getting data from entries
# for entry in entries:
for i in range(4,10):
    new_shape = generate_convex_polygon(i)
    # new_shape = get_shape_from_entry(entry)
    new_shape.normalize_polygon(screen_width - 2*x_margin, screen_height - 2*y_margin, x_margin, y_margin)
    start_time = time.time()
    convex_hulls.append(gift_wrapping_convex_hull(new_shape.points))
    elapsed_time = 1000 * (time.time() - start_time)
    x_time.append(i)
    y_time.append(elapsed_time)
    shapes.append(new_shape)

for i in range(len(shapes)):
    # Setting up screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255,255,255))

    for line in convex_hulls[i]:
        pygame.draw.line(screen, (0,0,0), line[0], line[1], 1)
    draw_points(shapes[i].points, screen, 'output/' + str(x_time[i]) + '_convex_hull.png')

# print "Here"

# expected_output = []
# for x in x_time:
#     expected_output.append(x * x * x / 3000)

# pylab.plot(x_time, y_time, 'r-', label='Brute Force')
# pylab.plot(x_time, expected_output, 'b-', label='Expected Time')
# pylab.xlabel('Polygon Size')
# pylab.ylabel('Elapsed Time (ms)')
# pylab.title
# pylab.show()

# elapsed_time = time.time() - start_time
# print("Elapsed time = " + str(elapsed_time))