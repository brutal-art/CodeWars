def is_collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])

def max_encount_points(points):
    n = len(points)
    if n < 2:
        return (n, 1 if n == 1 else 0)
    max_count = 0
    beams = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = points[i], points[j]
            collinear = [a, b]
            for k in range(n):
                if k != i and k != j and is_collinear(a, b, points[k]):
                    collinear.append(points[k])
            if len(collinear) > max_count:
                max_count = len(collinear)
                beams = [collinear]
            elif len(collinear) == max_count:
                beams.append(collinear)

    unique_beams = {frozenset(beam) for beam in beams}
    return max_count, len(unique_beams)


if __name__ == '__main__':

    a = [(3, 7), (6, 4), (11, 7), (9, 4), (3, 10), (7, 6), (7, 1), (13, 1), (16, -1), (14, -1), (11, 2)]
    a2 = [(-1, 0), (1, 0), (0, 0)]
    a3 = [(2, 3), (6, -6), (4, 3), (2, -2), (8, 4), (11, -3),(11, 1)]

    print(max_encount_points(a2))