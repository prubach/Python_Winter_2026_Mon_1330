# points = [[1, 2],
#           [4, 5],
#           [7, 8]]

points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]

print(points)
el_5 = points[1][1]
print(el_5)
print(type(points))
print(type(points[2]))

for r in points:
    print(r)
    for c in r:
        print(c)