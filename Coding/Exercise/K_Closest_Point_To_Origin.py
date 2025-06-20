def k_closest(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

print(k_closest([[1,3],[-2,2]], 1))