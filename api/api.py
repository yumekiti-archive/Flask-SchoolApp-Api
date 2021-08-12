# API(flask)
from flask import Flask, render_template, jsonify, request

# ファイル読み込み
import news

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news', methods=['GET'])
def News():
    return news.news()

@app.route('/news', methods=['POST'])
def OnlyNews():
    return news.only(request.json['id'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)