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
print('Columns:')

def sum_cols(points):
    rows = len(points)
    cols = len(points[0])
    sum_cols = [0] * cols
    for c in range(cols):
        for r in range(rows):
            sum_cols[c] += points[r][c]
    return sum_cols
    print(sum_cols)

def sum_columns(grid):
    column_sums = []
    for col in range(len(grid[0])):
        column_sum = 0

        for row in range(len(grid)):
            column_sum += grid[row][col]

        column_sums.append(column_sum)
    return column_sums

def sum_cols_youssef(my_list):
    cols = []
    for i in my_list:
        for j in range(len(i)):
            if my_list.index(i) == 0:
                cols.append(0)
            cols[j] = cols[j] + i[j]

    return cols


print(sum_cols(points))
print(sum_columns(points))
print(sum_cols_youssef(points))

print(sum(sum_rows(points)))
print(sum(sum_cols(points)))

#print(sum_cols_youssef(sum_cols(points)))

# def sum_list(my_list):

print('-' * 60)

cur = ['USD', 'USD', 'PLN']
rates = [3.8, 4.3, 1.0]

rates_list = list(zip(cur, rates))
print(rates_list)

for currency, rate in zip(cur, rates):
    print(f'{currency} -> {rate}')

currencies_rates = list(zip(*rates_list))  # - unzip into a list
print(currencies_rates)
#currencies, rates = zip(*rates_list)
#print(currencies)
#print(rates)

l_a = [1, 2, 3]
#l_b = [3*x for x in l_a]
l_b = [3*x for x in l_a if x > 1]
print(l_b)

print('-' * 60)

def sum_rows_single_line(my_list):
    return [sum(row) for row in my_list]

def sum_cols_zip(my_list):
    unzip_cols = list(zip(*my_list))
    print(unzip_cols)
    return sum_rows_single_line(zip(*my_list))

print(f'sum_rows_single_line({sum_rows_single_line(points)}')
print(f'sum_cols_zip({sum_cols_zip(points)}')


