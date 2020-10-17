from flask import Flask
from api.ranker.scapertest import scraping
# from flask_cors import CORS <- Not necessary due to the proxy

# Initialize App
app = Flask(__name__)

@app.route('/news', methods=['GET'])
def get_news():
    final = scraping()
    return {'data': final}

if __name__ == '__main__':
    app.run()