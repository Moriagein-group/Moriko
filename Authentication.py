#認証部分をやります
import tweepy

def Auth():
    #認証キーとトークン(/消してください)
    API_KEY = 'zFMOi/4rwU0Bq54tv8/WFArYdDm' #your API KEY
    API_SECRET = 'QBDdzVldnx/MiBe7qQ5Ybp2/R8Uf3CJEOJBP/nKLrMiN2rNZONiUT' #your API SECRET KEY
    ACCESS_TOKEN = '3279591482-oFOs6Uw/gWqyXQdTcfG9Mmf2E/GS36FLMNksyMNpS' #your ACCESS TOKEN
    ACCESS_TOKEN_SECRET = 'ISOKW8ov/UcwLapW6lX3lG/vQSOKvmGlYl4L8/eGGnysi3qh' #your SECRET ACCESS TOKEN

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth