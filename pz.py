from concurrent.futures import ThreadPoolExecutor

import requests
import pandas as pd

from proxy import PyProxy
from tqdm import tqdm

from utils import request_with_retry

p = PyProxy("66291", bulk_size=500, life=3)

uri = "https://zfcxjw.cq.gov.cn/gzf/pczwff/site/cqgzf/queryresultpublic/getSqshjgAction"




def fetch_page(page_number, tableName, uri, headers, pbar, all_data):
    pbar.set_description(f'采集第{page_number}页')
    ip = p.get_ip()
    body = {
        "isInit": False,
        "pageNumber": page_number,
        "prefix": "",
        "xm": "",
        "cnumber": "",
        "sqpq": "",
        "hx": "",
        "sqhx": "",
        "code": "",
        "tableName": tableName
    }
    proxies = {
        "http": ip,
        "https": ip
    }
    proxies = None
    response = request_with_retry("POST", uri, headers=headers, data=body, proxies=proxies)
    if response is not None:
        response_json = response.json()
        if 'dataList' in response_json:
            all_data.extend(response_json['dataList'])
        else:
            pbar.set_description(response_json.get("message"))
    pbar.update(1)  # Increment the progress


def fetch_all_data(tableName):
    all_data = []
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://zfcxjw.cq.gov.cn",
        "Referer": "https://zfcxjw.cq.gov.cn/gzf/pczwff/site/cqgzf/queryresultpublic/applicationresultdetail/46",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/117.0.0.0"
    }
    # 先获取总页数
    first_page_body = {
        "isInit": True,
        "pageNumber": 1,
        "prefix": "",
        "xm": "",
        "cnumber": "",
        "sqpq": "",
        "hx": "",
        "sqhx": "",
        "code": "",
        "tableName": tableName
    }  # 基本与之前相同，但pageNumber为1
    first_page_response = request_with_retry("POST", uri, headers=headers, data=first_page_body,proxies=None)
    total_page = first_page_response.json().get('totalPage', 1)

    with tqdm(total=total_page,desc="采集进度") as pbar:
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(fetch_page, page_number, tableName, uri, headers, pbar, all_data) for page_number
                       in range(1, total_page + 1)]

            for future in futures:
                future.result()

    return all_data


if __name__ == "__main__":
    tableName = "querynow44"
    all_data = fetch_all_data(tableName)

    df = pd.DataFrame(all_data)
    df.to_csv(tableName + '.csv', index=False)
