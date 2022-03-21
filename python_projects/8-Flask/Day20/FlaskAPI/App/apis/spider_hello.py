import requests


def get_data():
    headers = {
        'User-Agent': "Liyingjun Browser"
    }

    response = requests.get('http://127.0.0.1:5000/goods/?g_name=110', headers=headers)
    print(response.json())


if __name__ == '__main__':
    get_data()
