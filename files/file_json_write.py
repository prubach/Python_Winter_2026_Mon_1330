import os
import json

weekdays_dict = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday'}
rates_dict = {'USD': 3.8, 'PLN': 1, 'EUR': 4.3}

my_list = [rates_dict, weekdays_dict]

my_json_file = os.path.join('..', 'data', 'rates.json')

with open(my_json_file, 'w') as f:
    json.dump(my_list, f)