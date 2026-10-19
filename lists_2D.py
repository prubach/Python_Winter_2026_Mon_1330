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

# for r in points:
#     print(r)
#     for c in r:
#         print(c)


def sum_rows(my_list):
    row_sums = []
    row_number = 0
    for row in my_list:
        row_sum = 0
        for num in row:
            row_sum += num
        #print(f"Row sum: {row_sum} for row {row} which is row number {row_number}")
        row_sums.append(row_sum)
        row_number += 1
    return row_sums
# ...

print(sum_rows(points))

# def sum_cols(my_list):


# def sum_list(my_list):
