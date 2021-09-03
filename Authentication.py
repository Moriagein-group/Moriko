#認証部分をやります
import tweepy

import os
from os.path import join, dirname
from dotenv import load_dotenv

def Auth():

    # .envファイルに書いた内容を環境変数にセットするよ
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(verbose=True, dotenv_path=dotenv_path)

    # 環境変数に設定したトークンたちを読み込むよ
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth