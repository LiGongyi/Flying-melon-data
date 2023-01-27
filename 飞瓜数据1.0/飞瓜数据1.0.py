import requests
import time

user_cookie = input('请输入自己飞瓜数据的cookie:')
user_header = ('姓名', '抖音ID', '认证标识', '飞瓜指数', '总粉丝量', '30天粉丝增量', '总作品数', '30天作品数', '总点赞量', '30天点赞增量', '人均客单价', '人均UV值')
user = input('请需要搜索的内容:')
for page in range(1, 11):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
        'Referer': 'https://dy.feigua.cn/Member',
        'Cookie': f'{user_cookie}'
    }
    body = {'pageSize': '10', 'sort': '0', 'showmodel': '0', 'keyword': f'{user}', 'liveOrAwamePromotionTitle': '', 'page': f'{page}'}

    # 时间戳
    t = time.time()
    t = int(round(t*1000))

    url = f'https://dy.feigua.cn/api/v1/bloggersearch/list?_={t}'
    response = requests.post(url=url, headers=headers, json=body)
    response_json = response.json()
    resps = response_json['Data']['BloggerDatas']

    for resp in resps:
        # 数据分析
        name = resp['NickName']  # 姓名
        UniqueId = resp['UniqueId']  # 抖音ID
        CustomVerify = resp['CustomVerify']  # 认证标识
        Score = resp['Score']  # 飞瓜指数
        Platform_Fans = resp['Platform_Fans']  # 总粉丝量
        FansInc_30day = resp['FansInc_30day']  # 30天粉丝增量
        Awemes = resp['Awemes']  # 总作品数
        AwemeCount30Day = resp['AwemeCount30Day']  # 30天作品数
        LikeCount = resp['LikeCount']  # 总点赞量
        LikesInc_30day = resp['LikesInc_30day']  # 30天点赞增量
        AvgGuestPrice = resp['AvgGuestPrice']  # 人均客单价
        AvgUserSale = resp['AvgUserSale']  # 人均UV值

        with open(f'飞瓜数据({user}).csv', mode='a+', encoding='utf-8_sig')as f:

            f.write('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(name, UniqueId, CustomVerify, Score,
                                                                      Platform_Fans,FansInc_30day, Awemes, AwemeCount30Day,
                                                                      LikeCount, LikesInc_30day, AvgGuestPrice, AvgUserSale))





