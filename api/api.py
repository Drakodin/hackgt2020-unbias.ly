import os
from flask import Flask
from api.service.service import astra_service
from api.control.credentials import credentials
from cassandra.query import dict_factory
# from flask_cors import CORS <- Not necessary due to the proxy

# Initialize App
app = Flask(__name__)

app.register_blueprint(credentials)

@app.route('/news', methods=['GET'])
def get_news():
    zip_path = os.path.abspath('secure-connect-astra-db-free.zip')
    astra_service.save_credentials(os.environ['ASTRA_USER'], os.environ['ASTRA_PASS'], 'AstraTest01', zip_path)
    session = astra_service.get_session()
    session.row_factory = dict_factory
    result = session.execute('SELECT * FROM news_site')
    
    return {'data': result[0:]}

if __name__ == '__main__':
    app.run()