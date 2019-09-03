import util
# ------------------------ GIFT WRAPPING IMPLEMENTATION -------------------------

'''
0 -> p, q and r collinear
1 -> clockwise
2 -> counterclockwise
'''
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def gift_wrapping_convex_hull(points):
    hull = []

    l = 0
    n = len(points)
    for i in range(n):
        if points[i].x < points[l].x:
            l = i

    p = l
    q = None

    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q
        if p == l:
            break
    
    return hull

# ------------------------ GRAHAM SCAN IMPLEMENTATION -------------------------

def graham_scan_convex_hull(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm.
    '''
    list_points = []
    for point in points:
        list_points.append(point.get_as_list())

    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    list_points = sorted(list_points)
    l = reduce(_keep_left, list_points, [])
    u = reduce(_keep_left, reversed(list_points), [])
    list_points = l.extend(u[i] for i in range(1, len(u) - 1)) or l
    
    lines = []
    for i in range(len(list_points)):
        lines.append([list_points[i % len(list_points)], list_points[(i+1) % len(list_points)]])

    return lines


# ------------------------ BRUTE FORCE IMPLEMENTATION -------------------------

def semi_plane_test(points, i, j, k):
    p1, p2, p = points[i], points[j], points[k]

    a, b, c = p2.y - p1.y, p1.x - p2.x, p1.x * (p2.y - p1.y) - p1.y * (p2.x - p1.x)
    val = a * p.x + b * p.y

    if val > c:
        return 1
    elif val == c:
        return 0
    elif val < c:
        return -1

def is_part_convex_hull(points, i, j):
    prev_side = 0
    ans = True

    for k in range(len(points)):
        if not (k == i or k == j):
            side = semi_plane_test(points, i, j, k)
            if prev_side == 0:
                # Initialization
                prev_side = side

            if prev_side != side:
                ans = False

    return ans

def brute_force_convex_hull(points):
    lines = []
    for i in range(len(points)):
        for j in range(i,len(points)):
            if not i == j:
                ans = is_part_convex_hull(points, i, j)
                if ans:
                    lines.append([points[i], points[j]])

    return lines

