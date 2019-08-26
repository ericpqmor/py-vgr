# -*- coding: utf-8 -*-
import sys
import time
sys.path.insert(1, 'lib')
from draw_functions import *

pygame.init()
screen_width = 700
screen_height = 700
x_margin = 70
y_margin = 70

# Reading entries from command line args
entries = sys.argv[1:]
shapes = []
start_time = time.time()

# Getting data from entries
for entry in entries:
    new_shape = get_shape_from_entry(entry)
    new_shape.normalize_polygon(screen_width - 2*x_margin, screen_height - 2*y_margin, x_margin, y_margin)
    shapes.append(new_shape)

for i in range(len(shapes)):
    # Setting up screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255,255,255))

    draw_points(shapes[i].points, screen, 'output/' + entries[i][5:-4] + '_convex_hull.png')
    
elapsed_time = time.time() - start_time
print("Elapsed time = " + str(elapsed_time))