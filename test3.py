import requests
from bs4 import BeautifulSoup

def getHTML(url):
    r = requests.get(url)
    return r.content

def parseHTML(html):
    soup = BeautifulSoup(html,'html.parser')

    body = soup.body
    eleBox = body.find_all('div',attrs={'class':'small_box'})

    for eleBoxItem in eleBox:
        a = eleBoxItem.find('p').find('a',attrs={'target':'_blank'})
        url = a['href']
        text = a.get_text()
        print '\n' + text
        print url

URL = 'http://digi.sina.com.cn/'
html = getHTML(URL)
parseHTML(html)