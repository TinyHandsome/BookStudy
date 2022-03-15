import json
import base64


def base64_encode_str(s):
    """用base64加密数据"""
    s_bt = s.encode()
    s_b64 = base64.b64encode(s_bt)
    s_b64_str = s_b64.decode()
    return s_b64_str


def base64_decode_str(s):
    """用base64解密数据"""
    untie_s = base64.b64decode(s)
    return untie_s.decode()


def base64_encode_dict2json(s: dict, file_name=None):
    """加密的是dict数据，变成json后加密"""
    s_json = json.dumps(s)
    s_base64 = base64_encode_str(s_json)

    if file_name is not None:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(s_base64)

    return s_base64


def base64_decode_json2dict(s: str):
    """加密的是json数据，解码并返回dict"""
    s_json = base64_decode_str(s)
    return json.loads(s_json)


if __name__ == '__main__':
    with open('myemail', 'r', encoding='utf-8') as f:
        email = f.read()
    password = base64_decode_json2dict(email)
    print(password)
