def sum_it(a: int, b: int) -> int:
    return a + b

print(sum_it(1.67, 32.53))

def sum_it_params(a=5, b=10):
    s_i = 35252
    summ = a +b
    # return summ, - adding a comma turns the output into a tuple with an empty second element
    return summ

print(sum_it_params(1.67))
print(sum_it_params())
print(sum_it_params(b=15))

print('-'*60)

b = 4
d = 0
if b > 5:
    d = 10
else:
    d = 5

print(f'd={d}')

for i in range(10):
    bi = i * 10

print(f'bi={bi}')
res = sum_it_params(5, 10)
print(f'res={res}')
#print(f's_i={s_i}') - not available outside of the function


def sum_and_multiply(a, b):
    summ = a + b

    #def multiply(c, d):
    #    print(a, b, c, d)
    #    return c * d
    def multiply():
        return a * b
    multi = multiply()
    #multi = multiply(a, b)
    return summ, multi

result = sum_and_multiply(5, 10)
print(f'result={result}')
print(f'type(result)={type(result)}')

sum_ab, multi_ab = sum_and_multiply(5, 10)
print(f'sum_ab={sum_ab}, multi_ab={multi_ab}')

#print(sum_and_multiply.multiply(1, 3))