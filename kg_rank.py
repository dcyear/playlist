import json
import time

import requests

from kg_crypto import getSign


# 获取排行榜期数
def appRankVol(rankId: str, rankCid: str):
    uri = "https://gateway.kugou.com/ocean/v6/rank/vol"
    params = {
        "rankid": rankId,
        "appid": "1005",
        "mid": "297580060635075034974339956030890869789",
        "clientver": "11689",
        "clienttime": str(int(time.time())),
        "token": "",
        "dfid": "",
        "ranktype": "2",
        "plat": "0",
        "rank_cid": rankCid,
        "zone": "tx6_gz_kmr",
    }
    body = {}
    headers = {
        "User-Agent": "Android9-AndroidPhone-11689-201-0-RankingStaging-wifi"
    }
    sign = getSign(params, body)
    params["signature"] = sign
    resp = requests.get(uri, params=params, headers=headers)
    if resp.status_code == 200:
        return resp.json()


# 获取排行榜歌曲
def appRankSongList(rankId: str, page: int):
    uri = "https://gateway.kugou.com/openapi/kmr/v2/rank/audio"
    params = {
        "dfid": "",
        "appid": "1005",
        "mid": "297580060635075034974339956030890869788",
        "clientver": "11689",
        "clienttime": round(time.time()),
    }
    body = {
        "area_code": "1",
        "rank_id": rankId,
        "rank_cid": int(rankId),
        "zone": "tx6_gz_kmr",
        "type": 1,
        "show_type_total": 1,
        "page": page,
        "pagesize": 100,
        "show_portrait_mv": 1,
        "filter_original_remarks": 1,
    }
    headers = {
        "User-Agent": "Android9-AndroidPhone-11689-201-0-NewRankSongListProtocol-wifi",
        "kg-tid": "369",
    }
    _body = json.dumps(body, separators=(',', ':'))
    sign = getSign(params, body)
    params["signature"] = sign
    resp = requests.post(uri, params=params, headers=headers, data=_body)
    if resp.status_code == 200:
        return resp.json()


if __name__ == "__main__":
    # print(appRankVol("8888", "74931"))
    print(appRankSongList("74930", 1))
