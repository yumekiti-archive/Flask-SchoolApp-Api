# json
import json

# ログイン用
import login

# 環境変数
import os
from dotenv import load_dotenv

# スクレイピング
import requests, re
from bs4 import BeautifulSoup

def news():

    ids = []
    titles = []
    dates = []
    tags = []
    links = []

    params = []

    # セッション開始
    session = requests.session()

    # ログイン
    res = session.post(os.getenv('LOGIN_URL'), data=login.AppLogin(0,0))

    # get
    geturl = session.get(os.getenv('NEWS_URL'))

    # html解析
    soup = BeautifulSoup(geturl.content, 'html.parser')

    # データの取得
    for element in soup.find_all('a'):
        if 'news_view' in element.get('href'):
            ids.append(re.sub(r"\D", "", element.get('href')))
    for element in soup.find_all('dd'):
        titles.append(element.text)
    for element in soup.find_all('dt'):
        dates.append(element.text.split(None,1)[0].replace(" ", ""))
    for element in soup.find_all('dt'):
        tags.append(element.text.split(None,1)[1].replace(" ", ""))
    for element in soup.find_all('a'):
        if 'news_view' in element.get('href'):
            links.append('https://comp-app.ecc-sv.com/app/news' + element.get('href').strip('.'))

    # paramsにデータを入れる
    for i, id in enumerate(ids):
        params.append({
            'id': id,
            'title': titles[i],
            'date': dates[i],
            'tag': tags[i],
            'link': links[i],
        })

    # セッション終了
    session.close()

    # jsonにして返す
    return json.dumps(params)

def only(id):

    params = []

    # セッション開始
    session = requests.session()

    # ログイン
    res = session.post(os.getenv('LOGIN_URL'), data=login.AppLogin(0,0))

    # get
    geturl = session.get(os.getenv('NEWS_ONLY_FRONT') + str(id) + os.getenv('NEWS_ONLY_BACK'))

    # html解析
    soup = BeautifulSoup(geturl.content, 'html.parser')

    params.append({
        'title': soup.find(class_='title').text,
        'data': soup.find_all('div')[10].text,
    })

    # セッション終了
    session.close()

    # jsonにして返す
    return json.dumps(params)