import os
import json

rates_dict = {'USD': 3.8, 'PLN': 1, 'EUR': 4.3}

my_json_file = os.path.join('..', 'data', 'rates.json')

with open(my_json_file, 'w') as f:
    json.dump(rates_dict, f)