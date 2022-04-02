import json


def load_data():
    with open('./data/cities.json', 'r') as f:
        return json.load(f)


def insert_cities(cities_dict):
    for k, v in cities_dict.items():
        for city in v:
            print(city)


if __name__ == '__main__':
    j = load_data()
    insert_cities(j)
