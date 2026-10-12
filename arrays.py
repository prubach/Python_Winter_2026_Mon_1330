arr_a = [3, 5, 7, 9]
print(f'arr_a={arr_a}')
print(f'3rd elem: {arr_a[2]}')

arr_b = [3, '5', 7.0, 9]
print(f'arr_b={arr_b}')

for e in arr_b:
    print(f'e={e} type={type(e)}')