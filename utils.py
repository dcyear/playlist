import requests
from requests.utils import cookiejar_from_dict
from requests.exceptions import ProxyError, Timeout, SSLError, ConnectionError

def str_cookie_to_dict(cookie: str):
    cookie_dict = {}
    pairs = cookie.split("; ")
    for pair in pairs:
        key_value = pair.split("=")
        if len(key_value) == 2:
            key, value = key_value
            cookie_dict[key.strip()] = value.strip()

    return cookiejar_from_dict(cookie_dict)

def request_with_retry(method, url, proxies=None, headers=None, data=None, cookies=None, params=None, retries=5):
    for i in range(retries):
        try:
            response = requests.request(method, url, proxies=proxies, headers=headers, data=data, params=params,
                                        timeout=30, cookies=cookies)
            return response
        except (ProxyError, Timeout, SSLError, ConnectionError) as e:
            # print(f"请求错误: {str(e)}, 重试: ({i + 1}/{retries})...")
            pass
    # print("请求已达最大重试次数 跳出")
    return None
