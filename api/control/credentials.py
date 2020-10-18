import os
from flask import Blueprint, request
from api.ranker.scapertest import scraping
from api.ranker.scraper_dao import ScraperDAO

from api.service.service import astra_service


credentials = Blueprint('credentials', __name__)


@credentials.route('/api/boot', methods=['GET'])
def connect():
    print('Attempt logged')

    # Load sites for webscraping
    zip_path = os.path.abspath('secure-connect-astra-db-free.zip')
    astra_service.save_credentials(os.environ['ASTRA_USER'], os.environ['ASTRA_PASS'], 'AstraTest01', zip_path)
    dao = ScraperDAO(astra_service.get_session())
    final = scraping()
    dao.write(final)

    return {'connected': True}, 200