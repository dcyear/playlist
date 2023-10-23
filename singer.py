import cryptos


# 获取歌手的歌曲列表
def get_song_list(cookie: str):
    uri = "/weapi/nmusician/workbench/upgrade/production/song/publish/list"
    csrf_value = cryptos.cookie_get_csrf(cookie)
    body_json = {
        "limit": 10,
        "offset": 0,
        "publishStatus": 200,
        "operations": "[\"MANAGE_SONG\",\"EDIT_SONG\",\"OFFLINE_SONG\",\"SET_SCHEDULE_TIME\"]",
        "onlyBeat": False,
        "csrf_token": csrf_value
    }
    return cryptos.weapiFetch(cryptos.neteaseHost + uri, cookie, body_json)


# 获取歌曲的图表数据
def get_song_graph(cookie: str, song_id: str):
    uri = "/weapi/nmusician/statistics/songs/song/get"
    csrf_value = cryptos.cookie_get_csrf(cookie)

    body_json = {
        "songid": song_id,
        "count": 7,  # 周期
        "csrf_token": csrf_value
    }
    return cryptos.weapiFetch(cryptos.neteaseHost + uri, cookie, body_json)


if __name__ == "__main__":
    cookie = "NMTID=00OHQqaYEpPvh5m00milJFANOyr1cwAAAGKjXToLw; JSESSIONID-WYYY=bEHUaOXpo3l2hXpp5ZwzsjnEzyWYg9pft%2FDfAcXY%2FwT43k3ETi7b2UubTx3AwwXhP7bcB83noQYndoAeQ%2FzHtYv96uI%2FqiqGixBgSnfa3TSBEebNArFWYnSSM2vpVDdBEpUKhBAn3c8qbJREHry1GRAWjBt3D12NWCDqo8SXOPqhGcHF%3A1694592163817; _iuqxldmzr_=32; _ntes_nnid=24c8273a00ddaabe80990aaac135a570,1694590363839; _ntes_nuid=24c8273a00ddaabe80990aaac135a570; WEVNSM=1.0.0; WNMCID=inrjtu.1694590366262.01.0; WM_TID=WzHPLtAuy3dFEEBUAQPB2U1WcnTxs8fo; __snaker__id=J2d9hdd34vGeCmhj; ntes_utid=tid._.9uwtbp7p7%252BNFVkQQBBOFmB1TdiCvI41K._.0; sDeviceId=YD-d3HJ1xmCJwpEVlBFQAKAaTOAmroxpzYG; gdxidpyhxdE=NW2ZPYj8ZlvQp3gMvtowO7lAtpBNhCo%5C98oGZasSPDif%2FE03wzs%2BNi2QTjU28dV%5CfRwbmbLTgDsiXU97aUQ1u88OvPgyAYAl%5CjGOUUA6tybtqEqfdBA3vOb6CLHpGGGXUKmhUGiCvHYQaYouX6T6Sns%2Bi%2BPJsVuOId45ExciOUugApJY%3A1694591268935; YD00000558929251%3AWM_TID=j3lm%2F0vQt2BFRABEFQLEmEvMG59Sp121; __csrf=26f727e4c330cd2c90b9b872a5e289a0; __remember_me=true; MUSIC_U=003741CC564BAF62DEFB59B5007FF75B015AEF96B4E59B2186800E6B8FE18763997395D02FC35FFF59B372ECFCEE40EE9459BE308A09978EE6F93B45A952620DD3CBCD12800878BD2CCA8D5D835CA32CC72642FE056311A21D4D1AC3B06A5CCBD65408D301568596C7AFC7D213F5646E69163AFF0D6E335059B9530A6AA4E3EB22DE227BF5C86934923215E36D2A5D9D7AA2D36FAE8A5412591C3E0F4D557763E73A5AC4915ED391A29DE03E58F19F721F7FD75DD707134B41B6D2D701700ECA0818FAA8D7EA810188F3727DBBA9E3A25D70EF9563A425C650E53C5E86F42CE943623225AB166059258C38BE2E127ACF0FFA19DDE3825ED279D4EB66141DF96C95F233EF42315678E0EAE85D333100AE6BA0C0A4A02EF285B755AE53FC91E658F02A7FAB459DF673157CF3C15939D0320228419F263EA9EAB367F8E4959DCC239A7E5F737B5B20310B0A00F4F3C2A0A8364BF1D358CB176CA932AA74F372021428A0B5BBCBCCAF983F560382A718628A29; ntes_kaola_ad=1"
    # get_song_list(cookie)
    # print(get_song_graph(cookie, "2040894553"))
