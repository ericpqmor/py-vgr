# -*- coding: utf-8 -*-
import sys
import time
import pygame
import draw
import polygon
from point import Point
from util import *

BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
BLUE    = (  0,   0, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)

pygame.init()
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont(None, 55)
pygame.display.set_caption('Shape Draw Test')

# Filling the background color
screen.fill(WHITE)

# Reading entries from command line args
entries = sys.argv[1:]
shapes = []
print(entries)

# Getting data from entries
for entry in entries:
    entry_file = open(entry, 'r')
    if entry_file.mode == 'r':
        shape_data = entry_file.readlines()
        shape_color = shape_data.pop()
        point_list = []

        for shape_coord in shape_data:
            coord = [x.strip() for x in shape_coord.split(',')]
            px, py = int(coord[0]), int(coord[1])
            print('Point: ', px, py)
            new_point = Point(px, py)
            point_list.append(new_point.normalize(screen_width, screen_height))

        color_coord = [x.strip() for x in shape_color.split(',')]
        r,g,b = int(color_coord[0]), int(color_coord[1]), int(color_coord[2])
        color = (r,g,b)

        shapes.append(polygon.Polygon(point_list, color))


print(shapes)
# shapes.append(polygon.Triangle(Point(30,30), Point(60,60), Point(90,30), BLUE))
# shapes.append(polygon.Circle(50, Point(200, 200), GREEN))
# shapes.append(polygon.Polygon([Point(30,30), Point(60,60), Point(90,30), Point(60,300)], RED))

for x in range(screen_width):
    for y in range(screen_height):
        for shape in shapes:
            if shape.is_inside(Point(x,y)):
                draw.draw_pixel(screen, shape.color, x, y)

pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
