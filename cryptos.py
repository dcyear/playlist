import re
from typing import Dict
import requests

import utils

fetchHost = "http://52.81.212.203:3667"

neteaseHost = "https://music.163.com"


def eapi(uri: str, item: Dict):
    if not uri.startswith("/"):
        uri = "/" + uri
    out = requests.post(fetchHost + "/eapi" + uri, json=item, timeout=10)
    return out.json()


def eapi_decrypt(raw_body):
    out = requests.post(fetchHost+"/eapi_decrypt", data=raw_body, timeout=10)
    return out.json()


def weapi(jsonBody: Dict):
    out = requests.post(fetchHost + "/weapi", json=jsonBody, timeout=10)
    return out.json()


def cookie_get_csrf(cookie: str):
    return re.search(r'__csrf=([^;]+)', cookie).group(1)


def weapiFetch(fullUrl, cookie, body, proxy=""):
    csrf_value = cookie_get_csrf(cookie)

    body_json = body
    body_enc = weapi(body_json)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36 Edg/117.0.1024.60"
    }
    params = {
        "csrf_token": csrf_value
    }

    proxies = {
        "http": proxy,
        "https": proxy
    }
    if not proxies:
        proxies = None

    resp = utils.request_with_retry("POST",fullUrl,
                                    data=body_enc,
                                    params=params,
                                    headers=headers,
                                    cookies=utils.str_cookie_to_dict(cookie),
                                    proxies=proxies)
    if resp:
        return resp
    return "获取失败"
