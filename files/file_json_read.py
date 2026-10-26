import os
import json
my_json_file = os.path.join('..', 'data', 'rates.json')

with open(my_json_file) as f:
    data = json.load(f)
    rates_dict = data[0]
    weekdays_dict = data[1]
    print(rates_dict)
    print(rates_dict['USD'])
    print(type(rates_dict['USD']))
    print(weekdays_dict)