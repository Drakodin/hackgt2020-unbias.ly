import os
from flask import Blueprint, request

from api.service.service import astra_service

credentials = Blueprint('credentials', __name__)

@credentials.route('/api/boot', methods=['GET'])
def connect():
    zip_path = os.path.abspath('secure-connect-astra-db-free.zip')
    astra_service.save_credentials(os.environ['ASTRA_USER'], os.environ['ASTRA_PASS'], 'AstraTest01', zip_path)
    astra_service.connect()
    return {'connected': True}, 200