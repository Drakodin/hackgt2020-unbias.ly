from api.service.service import astra_service
from api.ranker.scraper_dao import ScraperDAO

class SiteLoader(object):
    dao = ScraperDAO(astra_service.get_session())

    @staticmethod
    def save_sites(self, sites):
        self.dao.write(sites)
    
    @staticmethod
    def get_sites(self):
        sites = self.dao.get_sites()
        return sites