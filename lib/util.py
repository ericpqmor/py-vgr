from math import sqrt

def sign(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

def distance(a,b):
    return sqrt((a.x - b.x)**2 + (a.y-b.y)**2)

def cross_product(p1, p2):
    return p1.x * p2.y - p2.x * p1.y