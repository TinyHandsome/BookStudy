"""
常用的常量
"""
import json


VSCODE_JSON_PATH = 'C:/Users/LITIAN/AppData/Roaming/Code/User/settings.json'


class VSCODE:
    def __init__(self) -> None:
        with open(VSCODE_JSON_PATH, 'r', encoding='utf-8') as f:
            self.raw_json = f.readlines()

    def get_vscode_json_dict(self):
        """
        获取vscode的配置json
        """

        json_remove_xiegang = [i for i in self.raw_json if '//' not in i]
        str_json = "".join(json_remove_xiegang)
        # print('\n'.join(str_json.split('\n')[130:150]))
        vscode_json_dict = json.loads(str_json)
        return vscode_json_dict

    def write_file(self, new_str):
        """将文件中的内容替换为"""
        with open(VSCODE_JSON_PATH, 'w', encoding='utf-8') as f:
            f.write(new_str)

    def update_param(self, key, new_value):
        """修改vscode中的值，并保存文件，其中key没有引号"""
        new_str = ''
        for row in self.raw_json:
            # 不能是注释的的行
            new_row = None
            if '//' not in row:
                if key in row:
                    new_row = ' ' * 4 + '"' + key + '": ' + str(new_value) + ',\n'

            if new_row is not None:
                new_str += new_row
            else:
                new_str += row
        
        self.write_file(new_str)





if __name__ == '__main__':
    vv = VSCODE()
    vv.update_param('thiefBook.currPageNumber', 12341234)