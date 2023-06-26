from datetime import datetime
import json


def create_txt(city_name, numbers, error):
    current_date = str(datetime.now())[0:10]
    with open(f'./phone_numbers/{city_name}_{current_date}.txt', 'w') as f:
        f.write(json.dumps(numbers))
        if (error):
            print(error)
        else:
            print('done')
