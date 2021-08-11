# 本番環境ではenvを消す
import os
from dotenv import load_dotenv

def AppLogin(id, pw):

    login_info = {
        'c': 'login_2',
        'flg_auto': '1',
        'token_a': '',
        'id': os.getenv('TEST_ID'), # 本番環境ではenvを消す
        'pw' : os.getenv('TEST_PW'),# 本番環境ではenvを消す
    }

    return login_info