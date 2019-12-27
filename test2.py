import requests

def getHTML(url):
	r = requests.get(url)
	return r.content

url = 'https://www.yc609.cn'
html = getHTML(url)
print(html)