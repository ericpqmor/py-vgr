# -*- coding: utf-8 -*-
import sys
import time
from draw_functions import *

pygame.init()
screen_width = 1000
screen_height = 1000
x_margin = 50
y_margin = 50

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
    screen = pygame.display.set_mode((screen_width, screen_height))
    draw_shape_on_screen(shapes[i], screen)

    text = 'output/' + entries[i][5:-4] + '.png'
    pygame.image.save(screen, text)

elapsed_time = time.time() - start_time
print("Elapsed time = " + str(elapsed_time))