import tweepy
import Authentication
import datetime

#認証
auth = Authentication.Auth()
#APIインスタンス生成
api = tweepy.API(auth, wait_on_rate_limit=True)

# トレンドを1位のものから取得
colum = ["日本", "札幌", "仙台", "東京", "京都", "大阪", "広島", "福岡", "沖縄"]

places ={
    "日本": 23424856,
    # "札幌": 1118108, 
    "仙台": 1118129,
    "東京": 1118370, 
    # "京都": 15015372, 
    # "大阪": 15015370,
    # "広島": 1117227, 
    # "福岡": 1117099, 
    # "沖縄": 2345896
}

for area, place in places.items():
    # リストになっているので取り出す
    tr_date = [] 
    treands = api.trends_place(place)[0]

    for i, content in enumerate(treands["trends"]):
        a = i + 1, content['name']
        tr_date.append(a)

    print("\n--{}--".format(area))
    for trends in tr_date:
        print('-----------------')
        print(trends)