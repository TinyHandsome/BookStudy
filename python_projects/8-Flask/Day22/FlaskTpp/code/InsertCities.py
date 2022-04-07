import json

import pymysql
import os


def load_data():
    with open('./data/cities.json', 'r') as f:
        return json.load(f)


def insert_cities(cities_dict):
    db = pymysql.Connect(host='localhost', port=3307, user='root', password=os.environ.get('MYPASSWORD'),
                         database='GP1FlaskTpp', charset='utf8')
    cursor = db.cursor()

    for k, v in cities_dict.items():
        cursor.execute("insert into letter(letter) values ('%s');" % k)
        db.commit()

        cursor.execute("select letter.id from letter where letter='%s'" % k)
        letter_id = cursor.fetchone()[0]

        for city in v:
            print(city)
            c_id = city.get('id')
            c_parent_id = city.get('parentId')
            c_region_name = city.get('regionName')
            c_city_code = city.get('cityCode')
            c_pinyin = city.get('pinYin')

            cursor.execute(
                "insert into city(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin) values (%d, %d, %d, '%s', %d, '%s');"
                % (letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin))

            db.commit()


if __name__ == '__main__':
    j = load_data()
    insert_cities(j)
