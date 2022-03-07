import requests
import time
import sched

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImZiZTMzNDlmLTY4ZmUtNDY4OC04MDE0LTFlNWYyMzEyNTI0YyJ9.e-Z1uVDB2l9HeUs1X9SXwWGpYVgbI3Kkb3siO9vt4PjK_ilr-LlKI9Z6MCkqXjZe_NrEri1hmwVmljyAd_-6wQ",
}
url1 = 'http://lsqzdrqgkxt.ytlaishan.gov.cn:18081/key/area/personnel/re/xz/list?pageNum=1&pageSize=100&auditStatus=0'
url2 = 'http://lsqzdrqgkxt.ytlaishan.gov.cn:18081/system/declare/list?pageNum=1&pageSize=100&declarationStatus=0'


def get_url_address(url) -> list:
    resp = requests.get(url, headers=headers)
    result = resp.json()
    addrs = [x.get('address') for x in result.get('rows')]
    return addrs


def check_fuliwan_in_list(ll: list, check_list):
    """检查富力湾是否在list中"""
    def check_fuliwan_in_str(ss: str):
        for cl in check_list:
            if cl in ss:
                return True
        return False

    count = 0
    for l in ll:
        if check_fuliwan_in_str(l):
            count += 1

    return count


def check_two_urls():
    check_list = ['富力湾', '锦园']

    addresses1 = get_url_address(url1)
    addresses2 = get_url_address(url2)

    c1 = check_fuliwan_in_list(addresses1, check_list)
    c2 = check_fuliwan_in_list(addresses2, check_list)
    c_sum = c1 + c2
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('    疑似白银河居委会未修正数量：', str(c1) + '/' + str(len(addresses1)), '|', '疑似白银河居委会未审核数量：', str(c2) + '/' + str(len(addresses2)), '|', '疑似总数量：', c_sum)
    if c_sum <= 0:
        print('    【周队不用担心，没有问题~】')
    else:
        print('    【周队快处理啦~】')
    print()


def main():
    def perform(inc):
        scheduler.enter(inc, 0, perform, (inc,))
        check_two_urls()

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 0, perform, (600,))
    scheduler.run()


if __name__ == '__main__':
    main()
