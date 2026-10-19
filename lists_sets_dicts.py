arr_a = [3, 5, 7, 9, 5, 9]
for i in arr_a:
    print(i, end=' ')
print(arr_a[2])

#arr_a.remove(7)
#print(arr_a)

print('\n' + '-'*80)
print('sets')
set_a = set(arr_a)

# print(set_a[2]) - can't be done

for i in set_a:
    print(i, end=' ')

print('\n' + '-'*80)

set_b = set_a.copy()
set_b.remove(9)

print(set_b)

print('\n' + '-'*80)

list_a = list(set_a)
print(list_a)
print(list_a[2])

list_a.append(8)
print(list_a)

list_a.insert(2, 100)
print(list_a)

list_a.remove(8)
print(list_a)

# Remove 2nd element
list_a.pop(1)
print(list_a)


print('\n' + '-'*80)
t_1 = (2, 56, 86)
print(t_1)
print(type(t_1))
print(t_1[2])

#t_1.append(100)

