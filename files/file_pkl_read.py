import os
import pickle
my_pkl_file = os.path.join('..', 'data', 'rates.pkl')

with open(my_pkl_file, mode='rb') as f:
    data = pickle.load(f)
    rates_dict = data[0]
    weekdays_dict = data[1]
    print(rates_dict)
    print(rates_dict['USD'])
    print(type(rates_dict['USD']))
    print(weekdays_dict)