# json
import json

# ログイン用
import login

# 環境変数
import os
from dotenv import load_dotenv

# スクレイピング
import requests
from bs4 import BeautifulSoup

def news():

    news = []

    # セッション開始
    session = requests.session()

    # ログイン
    res = session.post(os.getenv('LOGIN_URL'), data=login.AppLogin(0,0))

    # get
    geturl = session.get(os.getenv('NEWS_URL'))

    # html解析
    soup = BeautifulSoup(geturl.content, 'html.parser')

    for element in soup.find_all('li'):
        news.append({'title': element.text})

    # セッション終了
    session.close()

    return json.dumps(news)