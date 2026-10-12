import sys

a = 153.36361
b = 546
c = a + b
print(c)
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
type_c = type(c)
print(f'type_c: {type(c)} c={c}')

d = 436276135862159267856215628356965145239457509572759245702509285930927921791877809170943794783694736
e = 543765975437029376937692473698473069724396724390673497693769473792875927593636363426269736092769777

f = d + e
print(f'f={f}')
print(f'type_f={type(f)}')
print('f={}'.format(f))
s_d = str(d)
num_digits_d = len(s_d)
print(f'num_digits_d={num_digits_d}')

f_d = 436276135862159267856215628356965145239457509572759245702509285930927921791877809170943794783694736.0
f_e = 543765975437029376937692473698473069724396724390673497693769473792875927593636363426269736092769777.0
print(f'type f_d={type(f_d)}')
print(f'f_d={f_d}')
print(f'f_e={f_e}')
f_f = f_d + f_e
print(f'f_f={f_f}')

g = 1.52e-2
print(f'g={g}')

max_f = 1.79444e308
print(f'max_f={max_f}')

print(sys.float_info)
b_b = 0b1011
print(f'b_b={b_b}')

h_c = 0x1f
print(f'h_c={h_c}')

a = 1.9835
b = round(a, 2)
print(f'a={a}')
print(f'b={b}')

f = 10
g = 4
r = f % g
print(f'r={r}')

h = 9
i = int('987686876868')
j = h + i

print(f'j={j}')
