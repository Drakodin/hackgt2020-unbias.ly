# Based on DataStax=Example for Python with Astra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
from cassandra import Unauthorized, Unavailable, AuthenticationFailed, OperationTimedOut, ReadTimeout

class Manager(object):
    __instance = None
    username = None
    password = None
    keyspace = None
    secure_connect_bundle_path = None
    initialized = False
    _session = None

    @staticmethod
    def get_instance():
        if Manager.__instance is None:
            Manager()
        return Manager.__instance
    
    def __init__(self):
        Manager.__instance = self
    
    def save_credentials(self, username, password, keyspace, secure_connect_bundle_path):
        self.username = username
        self.password = password
        self.keyspace = keyspace
        self.secure_connect_bundle_path = secure_connect_bundle_path
        self.initialized = True
    
    def connect(self):
        if self.initialized is False:
            raise Exception('Initialization required for Manager.save_credentials')

        if self._session is None:
            astra_config = {
                'secure_connect_bundle': self.secure_connect_bundle_path
            }

            cluster = Cluster(cloud=astra_config, auth_provider=PlainTextAuthProvider(self.username, self.password))
            self._session = cluster.connect(keyspace=self.keyspace)
            self._session.row_factory = dict_factory
        
        return self._session
    
    def close(self):
        if self.initialized and self._session is not None:
            self._session.shutdown()