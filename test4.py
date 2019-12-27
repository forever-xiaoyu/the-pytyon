#coding=utf-8
import requests
from bs4 import BeautifulSoup
import codecs
import csv

def getHTML(url):
    r = requests.get(url)
    return r.content

def parseHTML(html):
	soup = BeautifulSoup(html,'html.parser')

	body = soup.body
	eleBox = body.find_all('div',attrs={'class':'small_box'})

	listTemp = []

	for eleBoxItem in eleBox:
		a = eleBoxItem.find('p').find('a',attrs={'target':'_blank'})
		url = a['href']
		text = a.get_text()
		listTemp.append([url.encode('utf-8'), text.encode('GBK')])

	return listTemp

def writeCSV(file_name,data_list):
    with codecs.open(file_name,'wb') as f:
        writer = csv.writer(f)
        for data in data_list:
            writer.writerow(data)

URL = 'http://digi.sina.com.cn/'
html = getHTML(URL)
data_list = parseHTML(html)
writeCSV('test.csv',data_list)
print data_list