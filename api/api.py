from flask import Flask
from api.ranker.scapertest import scraping
from api.control.news_sites_load import SiteLoader
from api.control.credentials import credentials
# from flask_cors import CORS <- Not necessary due to the proxy

# Initialize App
app = Flask(__name__)

app.register_blueprint(credentials)

# Load sites for webscraping
final = scraping()
SiteLoader.save_sites(final)

@app.route('/news', methods=['GET'])
def get_news():
    result = SiteLoader.get_sites()
    return result

if __name__ == '__main__':
    app.run()