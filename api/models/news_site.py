import json

class NewsSite(object):
    def __init__(self, data):
        self.link = data.get('provider')
        self.title = data.get('title')
        self.score = data.get('score')
        self.summary = data.get('summary')
    
    def to_JSON(self):
        return json.dumps(self)