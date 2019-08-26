def cmp_function(a,b):
    return (a > b) - (a < b)

def turn(p, q, r):
    return cmp_function((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
        hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)

    return hull

def convex_hull_graham(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    print l.extend(u[i] for i in range(1, len(u) - 1) or 1)