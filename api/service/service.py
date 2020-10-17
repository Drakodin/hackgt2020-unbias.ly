from api.queries.manager import Manager

class AstraService(object):
    _session_manager = Manager()
    _session = None

    def get_session(self):
        if self._session is None:
            self._session = self._session_manager.get_instance().connect()
        
        return self._session
    
    def save_credentials(self, username, password, keyspace, secure_connect_bundle_path):
        self._session_manager.save_credentials(username, password, keyspace, secure_connect_bundle_path)
    
    def connect(self):
        return self._session.connect()