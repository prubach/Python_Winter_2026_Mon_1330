s_1 = 'abcdefg'
s_2 = 'hijkl'

print(f's_1[2]={s_1[2]}')
print(f's_1[2-4]={s_1[2:4]}')
print(f's_1[:4]={s_1[:4]}')
print(f's_1[4:]={s_1[4:]}')
print(f's_1[-3:]={s_1[-3:]}')


print(r'\n\n\nabgg\tgrhreh')
print('\n\n\nabgg\tgrhreh')
s_3 = s_1 + s_2
print(f's_3={s_3}')

c_a = ord('a')
print(f'c_a={c_a}')

c_b = chr(98)
print(f'c_b={c_b}')


s_5 = 'abcdefgabcdefg'
i_abc = s_5.find('bce')
print(f'i_abc={i_abc}')
i_abc = s_5.rfind('bc')
print(f'i_abc={i_abc}')

'''
Multline comment

'''
# Comment
#i_abc = s_5.index('bce')
print(f'i_abc={i_abc}')
i_abc = s_5.rindex('bc')
print(f'i_abc={i_abc}')

s_6 = '1445;2553;3647'
arr_s6 = s_6.split(';')
print(f'arr_s6={arr_s6}')

s_7 = '    sgsbg  '
s_8 = s_7.strip()
print(f's_8={s_8}')

