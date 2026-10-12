p = False
q = True
print(type(p))

if p:
    print('p is True')
else:
    print('p is False')

print('--------------')

if p and q:
    print('p and q is True')
else:
    print('p or q is False')

print('--------------')

if p or q:
    print('p or q is True')
else:
    print('p and q is False')

print('--------------')

if p ^ q:
    print('p xor q is True')
else:
    print('not xor p and q')


a = 10

if a < 12:
    print('a < 12')
    print('2nd line')
print('after the block')

def sumit(a, b):
    # comment
    return a + b

print(sumit(3, 8))
print(sumit(3, 4))