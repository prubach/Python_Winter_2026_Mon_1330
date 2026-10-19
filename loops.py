for i in range(10):
    print(i)
print('-'*80)

for i in range(5, 11):
    print(i, end=' ')

print('\n' + '-'*80)

for i in reversed(range(20, 50, 3)):
    print(i, end=' ')

print('\n' + '-'*80)


for i in range(-50, -20, 3):
    print(i, end=' ')

print('\n' + '-'*80)


for i in range(50, 20, -2):
    if i == 24:
        break
    print(i, end=' ')

print('\n' + '-'*80)

print('While loop')


i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    if i == 8:
        break
    print(i, end=' ')

print('\n' + '-' * 80)