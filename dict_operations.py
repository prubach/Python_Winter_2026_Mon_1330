rates_dict = {'USD': 3.8, 'PLN': 1, 'EUR': 4.3}
#rates_list = [('USD', 3.8), ('PLN', 1), ('EUR', 4.3)]

#rates_dict = dict(rates_list)
print(rates_dict)

for key, value in rates_dict.items():
    print(key, value)

print('\n' + '-'*80)

for key in rates_dict.keys():
    print(key, rates_dict[key])

print(type(rates_dict.keys()))
print(set(rates_dict.keys()))
print(rates_dict.values())
print(type(rates_dict.values()))
print(list(rates_dict.values()))

my_exch_rate = rates_dict['USD']
# my_exch_rate = rates_dict['GBP'] - KeyError
my_exch_rate = rates_dict.get('GBP')
my_exch_rate = rates_dict.get('GBP', 2.5)
print(my_exch_rate)