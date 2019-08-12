import pygame

def draw_pixel(surface, color, x, y):
    pygame.draw.line(surface, color, (x,y), (x,y))