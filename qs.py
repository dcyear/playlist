import utils
from utils import request_with_retry


# 汽水音乐后台 抖音音乐后台


# 获取所有歌曲
def getAllSong(cookie, offset=0):
    uri = f"https://music.douyin.com/console/api/v1/albums/list?limit=10&offset={offset}"
    headers = {
        "Referer": "https://music.douyin.com/label/songs",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
    }
    response = request_with_retry("GET", uri, headers=headers, cookies=utils.str_cookie_to_dict(cookie))
    if response is not None:
        response_json = response.json()
        return response_json


# 获取统计
# {'cvAll': 12782, 'cvOneDay': 8, 'cv7Days': 8, 'cvLiveAll': 11, 'cvLive7Days': 1, 'favoriteAll': 406, 'favoriteOneDay': 2, 'favorite7Days': 2, 'cvvvAll': 37264839, 'cvvvOneDay': 10841, 'cvvv7Days': 10841, 'cvvvStreamingAll': 31376, 'cvvvStreaming7Days': 527, 'fansOneDay': 0, 'fansAll': 39, 'claimSongCount': 0, 'releaseSongCount': 50, 'signSongCount': 50, 'baseResp': {'requestId': '202311281700584D8011134C4A3204734B', 'errorCode': 0}}
# favoriteAll 音乐收藏量
# cvvvAll 音乐播放量
# cvAll 音乐使用量

def getSongOverview(cookie):
    uri = "https://music.douyin.com/console/api/v1/index/overview"
    headers = {
        "Referer": "https://music.douyin.com/label/statistics?select=vv",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
    }
    response = request_with_retry("GET", uri, headers=headers, cookies=utils.str_cookie_to_dict(cookie))
    if response is not None:
        response_json = response.json()
        return response_json


# 获取收益
# {
#     "cumulativeIncome": "13233",
#     "withdrawableBalance": "13233",
#     "withdrawnAmount": "0",
#     "lastPeriodIncome": "610",
#     "lastPeriodTime": "1696089600",
#     "baseResp": {
#         "requestId": "202311281702520D01659AFDE0E80479F8",
#         "errorCode": 0
#     }
# }
# withdrawableBalance 可提现金额
# cumulativeIncome 累积营收
# lastPeriodIncome 上月收入
def getSettlement(cookie):
    uri = "https://music.douyin.com/console/api/v1/settlement/overview/v2"
    headers = {
        "Referer": "https://music.douyin.com/label/statistics?select=vv",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
    }
    response = request_with_retry("GET", uri, headers=headers, cookies=utils.str_cookie_to_dict(cookie))
    if response is not None:
        response_json = response.json()
        return response_json


# 获取播放量按时间范围内趋势数据
def getStatisticsSeries(cookie,startTime="1698570499625",endTime="1701076099625"):
    uri = "https://music.douyin.com/console/api/v1/statistics/totalTimeseries"
    query = {
        "startTime":startTime,
        "endTime":endTime
    }
    headers = {
        "Referer": "https://music.douyin.com/label/statistics",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"
    }

    response = request_with_retry("GET", uri, headers=headers,params=query, cookies=utils.str_cookie_to_dict(cookie))
    if response is not None:
        response_json = response.json()
        return response_json


if __name__ == "__main__":
    cookie = "sso_uid_tt=c836efeff589eebada2b3b7bce4cb03f; sso_uid_tt_ss=c836efeff589eebada2b3b7bce4cb03f; toutiao_sso_user=98d234099c439d2ca36b36f95eb64879; toutiao_sso_user_ss=98d234099c439d2ca36b36f95eb64879; LOGIN_STATUS=1; store-region=cn-cq; store-region-src=uid; my_rd=2; __live_version__=%221.1.1.3951%22; sid_ucp_sso_v1=1.0.0-KDQxNzYzN2ExNjhjMzY3MGIwNmVlODU0YzFjNDBjNGM3ZmExYzM1ZjkKHwj8r7HF2IzDBhDrzI2qBhjvMSAMMP6V4poGOAZA9AcaAmxxIiA5OGQyMzQwOTljNDM5ZDJjYTM2YjM2Zjk1ZWI2NDg3OQ; ssid_ucp_sso_v1=1.0.0-KDQxNzYzN2ExNjhjMzY3MGIwNmVlODU0YzFjNDBjNGM3ZmExYzM1ZjkKHwj8r7HF2IzDBhDrzI2qBhjvMSAMMP6V4poGOAZA9AcaAmxxIiA5OGQyMzQwOTljNDM5ZDJjYTM2YjM2Zjk1ZWI2NDg3OQ; x-jupiter-uuid=17011597355119520; gf_part_986745=62; csrf_token=lqZVcYKr-NUZ44uSupFqUy4ksQpaFfWtuAI8; csrf_session_id=1d822aed79a546f8d5d208e641cd0bc0; passport_csrf_token=bbb6469f9d5fc453a7c31e0cdc0aa549; passport_csrf_token_default=bbb6469f9d5fc453a7c31e0cdc0aa549; s_v_web_id=verify_lpi2wg1d_xtXFTyk4_eGMo_4sg1_97Y4_i1edtE0SYLu4; MONITOR_WEB_ID=631a70a3-50a9-4d12-9062-d7ce8bd550b9; d_ticket=f8579fff353d6ba6a5b847bf7c0548d31391f; odin_tt=0bf17407acb1307d97c4910b00a006a839e243381e75df23ff91723faa95adc459d5e90c94cb9a7a3eedd1ccd33b064fca61433a2a29047c7352e6e15083d5f4; passport_assist_user=CkFL_oCpoTsdXeRoEtRJYJZpC2NFROG77a7sBuCe98kkX4BiYdVNwPVtgGxbSApjhYgOtAzTwE2tWLsfkYaKSkCVcBpKCjz9E5vouV9l1puqN3bGxCOKtj0olBS7pV5l6mmLp7zG8BGC-XJmL2c4m0XFuwn6ShXuJ96YmN_J5aLxwAMQrL_CDRiJr9ZUIAEiAQPllm8M; n_mh=35z7A0UoORlfrCLnmn85q1356nGSpUle0R6Dp8dGzzI; passport_auth_status=4ed7de2cebbd3796f5cab53a81cd5fc3%2C; passport_auth_status_ss=4ed7de2cebbd3796f5cab53a81cd5fc3%2C; sid_guard=0f8019e61d59519f52cca2a34b13b094%7C1701161016%7C5184000%7CSat%2C+27-Jan-2024+08%3A43%3A36+GMT; uid_tt=04b8fea4e1d8fcd4877f659ffec0afa2; uid_tt_ss=04b8fea4e1d8fcd4877f659ffec0afa2; sid_tt=0f8019e61d59519f52cca2a34b13b094; sessionid=0f8019e61d59519f52cca2a34b13b094; sessionid_ss=0f8019e61d59519f52cca2a34b13b094; sid_ucp_v1=1.0.0-KDY0ZmJjNzQ0NjJkZjlhNWVkZWE2MWU3YWJlNTlhNTI0ODE0YTk3ZTEKHwjYz_DxmYz5BRC40JarBhjGDCAMMIjH55AGOAJA8QcaAmxxIiAwZjgwMTllNjFkNTk1MTlmNTJjY2EyYTM0YjEzYjA5NA; ssid_ucp_v1=1.0.0-KDY0ZmJjNzQ0NjJkZjlhNWVkZWE2MWU3YWJlNTlhNTI0ODE0YTk3ZTEKHwjYz_DxmYz5BRC40JarBhjGDCAMMIjH55AGOAJA8QcaAmxxIiAwZjgwMTllNjFkNTk1MTlmNTJjY2EyYTM0YjEzYjA5NA; ttwid=1%7Cl7Pm-kYp5IbjNgsO7Ootrrgkpv4m8m03tOIlJdetftg%7C1701161041%7Cd8a0b3163ea19e75127d7494af42b783fc1df36b97d871e0c63cdb66ba194a04"
    print(getStatisticsSeries(cookie))
