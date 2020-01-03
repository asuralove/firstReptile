import requests
from lxml import etree

'''
爬取电影天堂网练习xpath
'''
headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    'Host':'www.ygdy8.net',
    'Cookie':'XLA_CI=30abf7dba86395ecbf2019e79b2b52d1; cscpvrich5041_fidx=1'
}
#注意https
url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
BASE_DOMAIN = 'http://www.ygdy8.net'
try:
    response = requests.get(url,headers=headers,verify=False)
    text = response.content.decode('gb18030','ignore')
    #text = response.text
    print(text)
    print('888'*30)
    html = etree.HTML(text)
    print(html)
    print('888' * 30)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    for detail_url in detail_urls:
        print(BASE_DOMAIN + detail_url)
except Exception as e:
    print('遇到问题')
    print(type(e))
    print(e)
