import requests
from bs4 import BeautifulSoup
from ReptileFrame.ezpymysql import Connection

db = Connection(
    'localhost',
    'news',
    'root',
    '123456'
)

def parse_page(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'referer' : 'https://www.sina.com.cn/'
    }
    response = requests.get(url,headers)
    text = response.content.decode('utf-8')
    #print(response.content.decode('utf-8'))
    soup = BeautifulSoup(text,'html.parser')
    divs = [".part_01.clearfix",".part_02 pt_8.clearfix",".part_03.clearfix",".part_02.clearfix",".blk_09",".part_05.clearfix",".newpart",".part_04.clearfix"]
    for div in divs:
        search(soup,div)

def search(soup,div):
    divs = soup.select(div)
    for div in divs:
        for a in div.find_all('a'):
            if (len(a.text) > 2) and (a['href'].startswith("http")):
                title = a.text.replace('\r','').replace('\n','')
                href = a['href'].replace('\r','').replace('\n','')
                #href = re.findall('http.*',old_href)
                sql = 'insert into detail_news(title, href) values(%s, %s)'
                db.execute(sql,title, href)
                # print({"title": title, "href": href})

def main():
    url = 'https://news.sina.com.cn/'
    parse_page(url)
if __name__ == '__main__':
    main()
