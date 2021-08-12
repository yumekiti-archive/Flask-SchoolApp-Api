# API(flask)
from flask import Flask, render_template, jsonify, request

# ファイル読み込み
import news

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def GetNews():

    return news.only(16282132111362768937)

@app.route('/api', methods=['POST'])
def post():
    result = {
        'data': request.json['text']
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)