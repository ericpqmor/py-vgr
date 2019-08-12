from math import sqrt

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def ray_intersects_segment(self, p1, p2):
        if p1.y <= p2.y:
            a,b = p1,p2
        else:
            a,b = p2,p1

        px,py = self.x, self.y

        EPS, INF = 0.005, 10**6

        # Gambiarra 
        if py == a.y or py == b.y:
            py += EPS
        if px == a.x or px == b.x:
            px += EPS

        if (py > b.y or py < a.y) or (px > max(a.x, b.x)):
            return False

        if px  < min(a.x, b.x):
            return True
        else:
            if abs(a.x - b.x) > EPS:
                m1 = (b.y - a.y) / (b.x - a.x)
            else:
                m1 = INF

            if abs(a.x - px) > EPS:
                m2 = (py - a.y) / (px - a.x)
            else:
                m2 = INF

        return m2 >= m1

            