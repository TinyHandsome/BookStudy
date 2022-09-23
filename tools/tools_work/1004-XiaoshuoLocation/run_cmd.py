import os


def run_cmd(bat_file):
    # with open(bat_file, 'r', encoding='utf-8') as f:
    #     bat = f.read()
    os.system(bat_file)


if __name__ == '__main__':
    os.system('open_chrome.bat')
