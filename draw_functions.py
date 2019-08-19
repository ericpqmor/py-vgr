import pygame
import polygon
from point import Point

def draw_pixel(surface, color, x, y):
    pygame.draw.line(surface, color, (x,y), (x,y))

def get_shape_from_entry(entry):

    entry_file = open(entry, 'r')
        
    shape_data = entry_file.readlines()
    shape_color = shape_data.pop()
    point_list = []

    for shape_coord in shape_data:
        coord = [x.strip() for x in shape_coord.split(',')]
        px, py = float(coord[0]), float(coord[1])
        point_list.append(Point(px,py))

    color_coord = [x.strip() for x in shape_color.split(',')]
    r,g,b = int(color_coord[0]), int(color_coord[1]), int(color_coord[2])
    color = (r,g,b)

    new_shape = polygon.Polygon(point_list, color)
    return new_shape

def draw_shape_on_screen(shape, screen):
    screen.fill((255,255,255))

    for x in range(screen.get_width()):
        for y in range(screen.get_height()):
            if shape.is_inside(Point(x,y)):
                draw_pixel(screen, shape.color, x, y)
    
    screen = pygame.transform.flip(screen, True, True)