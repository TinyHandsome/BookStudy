import requests


def get_data():
    res = requests.get('http://127.0.0.1:5000/getnews/')
    print(res.content.decode('utf-8'))


if __name__ == '__main__':
    get_data()
