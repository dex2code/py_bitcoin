points = [
    (192, 105),
    (17, 56),
    (200, 119),
    (1, 193),
    (42, 99)
    ]

prime = 223


for point in points:

    point_x = point[0]
    point_y = point[1]

    left = pow(point_y, 2) % prime
    right = (pow(point_x, 3) + 7) % prime

    if left == right:
        print(f"Point ({point_x}, {point_y}) is on curve Y**2 = X**3 + 7")
    else:
        print(f"Point ({point_x}, {point_y}) is NOT on curve Y**2 = X**3 + 7")