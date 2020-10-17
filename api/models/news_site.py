import json

class NewsSite(object):
    def __init__(self, data):
        self.provider = data.get('provider')
        self.title = data.get('title')
        self.rank = data.get('rank')
    
    def to_JSON(self):
        return json.dumps(self)