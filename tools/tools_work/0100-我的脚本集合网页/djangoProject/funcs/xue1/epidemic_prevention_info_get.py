import requests
import time
import sched
from dataclasses import dataclass


@dataclass
class EpidemicPrevention:
    authorization: str
    scheduler_gap: int = 600
    check_list = ['富力湾', '锦园', '辉盛岚海']

    def __post_init__(self):
        self.run_state = True
        self.current_str = ''
        self.update_authorization(self.authorization)

        self.url1 = 'http://lsqzdrqgkxt.ytlaishan.gov.cn:18081/key/area/personnel/re/xz/list?pageNum=1&pageSize=100&auditStatus=0'
        self.url2 = 'http://lsqzdrqgkxt.ytlaishan.gov.cn:18081/system/declare/list?pageNum=1&pageSize=100&declarationStatus=0'

    def update_authorization(self, author):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "Authorization": author,
        }

    def get_url_address(self, url) -> list:
        resp = requests.get(url, headers=self.headers)
        result = resp.json()
        addrs = [x.get('address') for x in result.get('rows')]
        return addrs

    @staticmethod
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

    def check_two_urls(self):
        addresses1 = self.get_url_address(self.url1)
        addresses2 = self.get_url_address(self.url2)
        len_addr1 = len(addresses1)
        len_addr2 = len(addresses2)
        sum_addr = len_addr1 + len_addr2

        c1 = self.check_fuliwan_in_list(addresses1, self.check_list)
        c2 = self.check_fuliwan_in_list(addresses2, self.check_list)
        c_sum = c1 + c2

        str_all = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        str_all = str_all + '    疑似白银河居委会未修正数量：' + str(c1) + '/' + str(len_addr1) + ' | ' + '疑似白银河居委会未审核数量：' + \
                  str(c2) + '/' + str(len_addr2) + ' | ' + '疑似总数量：' + str(c_sum) + '/' + str(sum_addr) + '\n'

        if c_sum <= 0:
            str_all = str_all + '    【周队不用担心，没有问题~】\n'
        else:
            str_all = str_all + '    【周队快处理啦~】\n'
        print(str_all)

        return str_all

    def start_scheduler(self):
        def perform(inc):
            if not self.run_state:
                return

            scheduler.enter(inc, 0, perform, (inc,))
            self.current_str = self.check_two_urls()

        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(0, 0, perform, (self.scheduler_gap,))
        scheduler.run()


if __name__ == '__main__':
    bear = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjQ1YjVlZDI2LTA2MTItNDdhYy04ODI1LTBiMDM2NmUzMWE2OSJ9.-nDsehdiMEQ9p_PF9giVxHsi9JHYGNHOWuYr3N7fQMJCPfEGvwg6E32rkJDzIQlQycJXvgArL9ExugHZhs_hyA"
    ep = EpidemicPrevention(bear)
    ep.start_scheduler()
