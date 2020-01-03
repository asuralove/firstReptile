import requests
from bs4 import BeautifulSoup


ALL_DATA = []
'''
爬取中国天气网练习bs4
'''
def parse_page(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    response = requests.get(url,headers)
    text = response.content.decode('utf-8')
    #lxml库不会补缺标签  html5lib容错性好
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    #print(conMidtab)
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            # for td in tds:
            #     print(td)
            #注意逻辑顺序
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            # print(city)
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            print({"city":city,"min_temp":min_temp})
        # break

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml#',
        'http://www.weather.com.cn/textFC/db.shtml#',
        'http://www.weather.com.cn/textFC/hd.shtml#',
        'http://www.weather.com.cn/textFC/hz.shtml#',
        'http://www.weather.com.cn/textFC/hn.shtml#',
        'http://www.weather.com.cn/textFC/xb.shtml#',
        'http://www.weather.com.cn/textFC/xn.shtml#',
        'http://www.weather.com.cn/textFC/gat.shtml#'
    ]
    # url = 'http://www.weather.com.cn/textFC/db.shtml#'
    # parse_page(url)
    for url in urls:
        parse_page(url)



if __name__ == '__main__':
    main()
