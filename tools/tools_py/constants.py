"""
常用的常量
"""
import json



VSCODE_JSON_PATH = 'C:/Users/LITIAN/AppData/Roaming/Code/User/settings.json'


def get_vscode_json_dict():
    """
    获取vscode的配置json
    """

    with open(VSCODE_JSON_PATH, 'r', encoding='utf-8') as f:
        raw_json = f.readlines()

    raw_json = [i for i in raw_json if '//' not in i]
    str_json = "".join(raw_json)
    print(str_json)
    vscode_json_dict = json.loads(str_json)

    return vscode_json_dict


if __name__ == '__main__':
    get_vscode_json_dict()