import requests
from bs4 import BeautifulSoup
from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def scraping():
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

    NDTVLinks = artlinks[50:77]
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



    # DECCAN CHRONICLES
    # --------------------------------------------------------------------------------------------
    url = "https://www.deccanchronicle.com/nation/politics"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    # print(soup.find_all("a"))

    articles = soup.find_all("a")
    # print(articles)
    artlinks = []

    for a in articles:
        artlinks+=["https://www.deccanchronicle.com" + a.get('href')]

    # print(artlinks)
    DeccanLinks = artlinks[123: 163]


    # --------------------------------------------------------------------------------------------






    LINKS = IndianExpressLinks+NDTVLinks+DeccanLinks

    ARTICLES = []
    TITLES = []
    SUMMARY = []
    for l in LINKS:
        url = l
        art = Article(url)
        art.download()
        art.parse()
        art.nlp()
        ARTICLES +=[art.text]
        TITLES += [art.title]
        SUMMARY += [art.summary]
    # VADER Scores, specifically compound
    SCORES = []
    analyzer = SentimentIntensityAnalyzer()
    for A in ARTICLES:
        vs = analyzer.polarity_scores(A)
        SCORES += [abs(vs['compound'])]

    LINKS_FINAL = []
    for i in range(len(LINKS)):
        if SCORES[i] != 0:
            value = {'link': LINKS[i], 'score': SCORES[i], 'title': TITLES[i], 'summary': SUMMARY[i]}
            if value in LINKS_FINAL:
                continue
            else:
                LINKS_FINAL += [value]

    return LINKS_FINAL
