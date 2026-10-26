import numpy as np

points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]

print(points)

print(f'row sum={np.sum(points, axis=1)}')
print(f'col sum={np.sum(points, axis=0)}')

col_sum = np.sum(points, axis=0)
print(f'type(el)={type(col_sum[0])}')

print(np.iinfo(np.int64))