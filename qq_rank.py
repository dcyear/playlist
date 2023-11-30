import requests


def getAllRank():
    uri = "https://lite.y.qq.com/cgi-bin/musicu.fcg"
    body = {
        "comm": {
            "ct": 11,
            "cv": "1003006",
            "v": "1003006",
            "tmeAppID": "qqmusiclight",
        },
        "request": {
            "module": "music.qqmusiclite.MtMusicChartsSvr",
            "method": "GetAllCharts",
            "param": {},
        }
    }
    headers = {
        "User-Agent": "okhttp/3.14.9"
    }
    r = requests.post(uri, json=body, headers=headers,timeout=10)
    return r.json()


# topId 4是流行指数榜 62是飙升榜
# period 2023_22 可不传默认最新
def getRankDetail(topId ,period=""):
    uri = "https://lite.y.qq.com/cgi-bin/musicu.fcg"

    param = {
                "topId": topId,
                "orderlist": 1,
                "offset": 0,
                "num": 300,
            }
    if len(period) >=1 :
        param["period"] = period

    body = {
        "comm": {
            "ct": 11,
            "cv": "1003006",
            "v": "1003006",
            "tmeAppID": "qqmusiclight",
        },
        "request": {
            "module": "musicToplist.ToplistInfoServer",
            "method": "GetDetail",
            "param": param,
        }
    }
    headers = {
        "User-Agent": "okhttp/3.14.9"
    }
    r = requests.post(uri, json=body, headers=headers,timeout=10)
    return r.json()

if __name__ == "__main__":
    print(getRankDetail(62))
