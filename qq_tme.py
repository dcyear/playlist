import random
import time

import requests


def get_trace_id():
    e = hex(int(time.time() * 1000))[2:]
    for _ in range(3):
        e += hex(int(random.random() * 1e16))[2:]
    return e[1:33]

# 获取趋势
def getTrend(token,startDay,endDay):
    uri = "https://y.tencentmusic.com/cd-gateway/musician/user/play/trend"
    query = {
        "startDay":startDay,
        "endDay":endDay
    }
    headers = {
        "Referer":"https://y.tencentmusic.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
        "Tme-Header-Feferer":"/",
        "Tme-Header-Herf":"https://y.tencentmusic.com/#/user/data/works",
        "Tme-Header-Token":token,
        "Tme-Source-Platform":"0",
        "Tme-Header-Trace":get_trace_id(),
        "Content-Type":"application/json;charset=utf-8"
    }
    r = requests.get(uri,params=query,headers=headers,timeout=10)
    if r.status_code == 200:
        return r.json()
    return r.text

# 获取作品数据
def getWorkData(token,startDay,endDay):
    uri = "https://y.tencentmusic.com/openapi/musician/data/song"
    query = {
        "platform":"all",
        "day":0,
        "pageNo":1,
        "pageSize":20,
        "beginDate": startDay,
        "endDate": endDay
    }
    headers = {
        "Referer": "https://y.tencentmusic.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
        "Tme-Header-Feferer": "/",
        "Tme-Header-Herf": "https://y.tencentmusic.com/#/user/data/works",
        "Tme-Header-Token": token,
        "Tme-Source-Platform": "0",
        "Tme-Header-Trace": get_trace_id(),
        "Content-Type": "application/json;charset=utf-8"
    }
    r = requests.get(uri, params=query, headers=headers, timeout=10)
    if r.status_code == 200:
        return r.json()
    return r.text


if __name__ == "__main__":
    # print(get_trace_id())
    token = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJ0bWUiLCJpYXQiOjE2OTgxMTUxMzgsInN1YiI6InBhc3NwcG9ydCIsImxvZ2luVHlwZSI6NywicXFVbmlvbklkIjoiQjBDMzI5ODIzMDE3QkVDQzRGNjI2QzQ0ODdFMDRFNzEiLCJtaWQiOjU2NDMzOSwidGVuYW50IjoibXVzaWNpYW4iLCJleHAiOjE3MDA3MDcxMzh9.mJ3u2uBuxtsie3AWZbIvkCbAQxtvaPkKqOZ5T-pklLQ"
    # print(getTrend(token,"2023-09-24","2023-10-23"))
    print(getWorkData(token,"20230922","20231022"))