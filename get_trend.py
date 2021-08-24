import tweepy
import Authentication

#認証
auth = Authentication.Auth()
#APIインスタンス生成
api = tweepy.API(auth)

# キーワードからツイートを取得
tweets = api.search(q=['from:C_herec'], count=10)

for tweet in tweets:
    print('-----------------')
    print(tweet.text)