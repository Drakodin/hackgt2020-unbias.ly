from cassandra.query import BoundStatement, BatchStatement, BatchType
from api.models.news_site import NewsSite

class ScraperDAO(object):
    table_name = 'news_site'
    insert = 'INSERT INTO {table_name} (link, title, score, summary) ' \
             'VALUES (:link, :title, :score, :summary);' \
             ''.format(table_name=table_name)
    select = 'SELECT * FROM {table_name}'.format(table_name=table_name)
    
    def __init__(self, _session):
        self._session = _session
        self.insert = _session.prepare(self.insert)
        self.select = _session.prepare(self.select)

    def write(self, data):
        batch = BatchStatement()
        batch.batch_type = BatchType.UNLOGGED

        for site in data:
            curr_site = NewsSite(site)
            batch.add(self.insert.bind({
                'link': curr_site.link,
                'title': curr_site.title,
                'score': curr_site.score,
                'summary': curr_site.summary
            }))
        
        self._session.execute(batch)
    
    def get_sites(self):
        stmt = BoundStatement(self.select).bind({})
        result = self._session.execute(stmt)
        return result