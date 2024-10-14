import hashlib
import time

import requests


def send_code():
    url = 'https://api.netease.im/sms/sendcode.action'
    nonce = hashlib.new("sha512", str(time.time()).encode('utf-8')).hexdigest()
    curtime = str(int(time.time()))
    sha1 = hashlib.sha1()
    secret = '待填写'
    sha1.update((secret + nonce + curtime).encode('utf-8'))
    check_sum = sha1.hexdigest()

    headers = {
        "AppKey": "待填写",
        "Nonce": nonce,
        "CurTime": curtime,
        "CheckSum": check_sum
    }
    post_data = {
        'mobile': '12344446666',
    }
    response = requests.post(url, data=post_data, headers=headers)

    print(response.content)


if __name__ == '__main__':
    send_code()
