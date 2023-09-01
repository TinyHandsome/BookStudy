import base64
import hashlib
import time

import requests


def make_data_secret(source):
    encode_content = base64.standard_b64encode(source.encode("utf-8")).decode("utf-8")
    add_content_encode_content = "CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk" + encode_content + "qOq3kRIxs26rmRtsUTJvBn9Z"
    encode_content_twice = base64.standard_b64encode(add_content_encode_content.encode("utf-8")).decode("utf-8")

    return encode_content_twice


def send_verify_code(phone):
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
        'mobile': phone,
    }
    response = requests.post(url, data=post_data, headers=headers)

    return response
