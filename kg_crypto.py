import hashlib
from typing import Dict

import requests

# 酷狗算法

fetchHost = "http://52.81.212.203:3667"


def getSign(params: Dict, body: Dict | str):
    full = {
        "params": params,
        "body": body
    }
    resp = requests.post(fetchHost + "/kg_sign", json=full, timeout=10)

    return resp.text


def __sign__(s):
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf8'))
    res = hl.hexdigest()
    return str(res)
