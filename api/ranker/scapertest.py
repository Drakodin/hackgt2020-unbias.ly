import requests
from bs4 import BeautifulSoup
from newspaper import Article

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }



#NDTV
# --------------------------------------------------------------------------------------------
url = "https://www.ndtv.com/topic/politics"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())
#print(soup.find_all("a"))
articles = soup.find_all("a")
#articles = articles[10:50]
#print(articles)
artlinks = []

for a in articles:
    artlinks+=[a.get('href')]

#print(artlinks)
#print(artlinks.index("https://www.ndtv.com/india-news/congress-had-stepmotherly-attitude-towards-ladakh-for-70-years-g-kishan-reddy-2311747"))

NDTVLinks = artlinks[50:75]
#print(links)
# -------------------------------------------------------------------------------------------



# INDIAN EXPRESS
# --------------------------------------------------------------------------------------------
url = "https://indianexpress.com/section/india/politics/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.find_all("a"))

articles = soup.find_all("a")
# print(articles)
artlinks = []

for a in articles:
    artlinks+=[a.get('href')]

# print(artlinks)
# print(artlinks.index("https://indianexpress.com/article/india/politics/maharashtra-agriculture-water-supply-sharad-pawar-baramati-indapur-5766457/"))

IndianExpressLinks = artlinks[37:62]
#print(links)
# --------------------------------------------------------------------------------------------


LINKS = IndianExpressLinks+NDTVLinks

ARTICLES = []

for l in LINKS:
    url = l
    art = Article(url)
    art.download()
    ARTICLES +=[art.text]
