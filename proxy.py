import random
import threading
from typing import List

import requests


class ProxyIP:
    def __init__(self, ip):
        self.host = ip.strip()
        self.use_count = 0

    @property
    def ip(self):
        if self.host.startswith("http"):
            return self.host
        return "http://" + self.host


# 品易代理
# flow 是流量包模式 否则是余额模式
class PyProxy:
    def __init__(self, neek, flow=True, bulk_size=300, life=5):
        self.url = f'http://zltiqu.pyhttp.taolop.com/getip?count={bulk_size}&neek={neek}&type=1&yys=0&port=2&sb=&mr=1&sep=1'
        if not flow:
            self.url += "&time=2"
        self.ip_pool: List[ProxyIP] = []
        self.ip_life = life
        self.lock = threading.Lock()

    def get_ip(self):
        with self.lock:
            if len(self.ip_pool) == 0:
                self._get_new_ips()
            target = random.choice(self.ip_pool)
            target.use_count += 1
            if target.use_count >= self.ip_life:
                self.ip_pool = [x for x in self.ip_pool if x.ip != target.ip]
            return target.ip

    def _get_new_ips(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            if "code" in response.text:
                raise Exception("获取ip代理失败",response.text)
            ip_list = response.text.strip().split('\n')
            self.ip_pool = [ProxyIP(ip) for ip in ip_list]
        else:
            raise Exception("Failed to get new IPs")
