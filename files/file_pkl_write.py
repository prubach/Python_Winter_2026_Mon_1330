import os
import pickle

weekdays_dict = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday'}
rates_dict = {'USD': 3.8, 'PLN': 1, 'EUR': 4.3}

my_list = [rates_dict, weekdays_dict]

my_json_file = os.path.join('..', 'data', 'rates.pkl')

with open(my_json_file, 'wb') as f:
    pickle.dump(my_list, f)