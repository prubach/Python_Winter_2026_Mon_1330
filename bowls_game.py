'''
 * * * * *
  * * * *
   * * *
    * *
     *

n = 5 - number of rows

compute how many bowls we need given n
for n=5, result=15
'''

#def count_bowls(n):
#    #...
#    return


def count_pins(rows):
    pins = 0
    for r in range(rows):
        pins += r + 1
    return pins

def count_bowls(n):
    i = 1
    bowls = 0
    while i <= n:
        bowls += i
        i += 1
    return bowls


def count_bowls_recurse(n):
    if n == 1:
        return 1
    else:
        return n + count_bowls_recurse(n - 1)

def count_bowls_sequence(n):
    return round((n * (n + 1))/2)
#result = count_bowls_recurse(5)
#print(result)


n = 999
print(f'count_bowls({n})={count_bowls(n)}')
print(f'count_pins({n})={count_pins(n)}')
print(f'count_bowls_recurse({n})={count_bowls_recurse(n)}')
print(f'count_bowls_sequence({n})={count_bowls_sequence(n)}')
