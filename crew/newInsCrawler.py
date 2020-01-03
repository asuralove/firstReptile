import re
import time
import requests
from ReptileFrame.ezpymysql import Connection

'''
爬取ins博主图片
'''
db = Connection(
    'localhost',
    'news',
    'root',
    '123456'
)
name = input("输入你想访问的博主:")
print(type(name))

class Spider(object):
    def __init__(self):
        self.HTTP_PROXY = {
            "http": "127.0.0.1:10809",
            "https": "127.0.0.1:10809",
        }
        self.home_url = 'https://www.instagram.com/'+name+'/'
        self.base_url = "https://www.instagram.com/graphql/query/?query_hash=2c5d4d8b70cad329c4a6ebe3abb6eedd&variables=%7B\"id\"%3A\"{id}\"%2C\"first\"%3A12%2C\"after\"%3A\"{end_cursor}\"%7D"
        self.data_list = []
        self.headers = {
            'origin': 'https://www.instagram.com',
            'referer' : 'https://www.instagram.com/'+name+'/',
            'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'x-csrftoken': 'E02eq9L12I104bzHwqqUVWJhmcjyZL0J',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0fVmB70v7trPZvL9AiGrNyLUmSoWbU0kkPBvsT61AEZNvs',
            'x-requested-with': 'XMLHttpRequest',
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "accept-encoding": "gzip,deflate,br",
            "accept-language": "zh-CN,zh;q=0.9",
        }

    def run(self):
        html = requests.get(url=self.home_url, headers=self.headers, proxies=self.HTTP_PROXY).text
        # print(html)
        pictures = re.findall(r'"display_url":"(.*?)",',html)
        id = re.findall(r'"owner":{"id":"(.*?)",',html)[0]
        end_cursor = re.findall(r'"end_cursor":"(.*?)"}',html)[0] #初始游标
        print(end_cursor)
        print(type(id))
        print(id)
        print(type(pictures))
        print(len(pictures))
        count = 0
        count += len(pictures)
        for picture in pictures:
            picture = picture.encode('utf-8').decode('unicode-escape')
            print(picture)#源代码中有12份
            sql = 'insert into setu(name, url) values(%s, %s)'
            db.execute(sql, name, picture)
        time.sleep(2)
        url = self.base_url.format(id=id, end_cursor=end_cursor)
        # dict = {'id':id,'end_cursor':end_cursor}
        # return url
        #循环抓取xhr页面数据
        while (1):
            id = id
            print('id:'+id)
            response = requests.get(url=url, headers=self.headers, proxies=self.HTTP_PROXY)
            json = response.text
            print(response.text)
            pictures = re.findall(r'"display_url":"(.*?)",', json)
            print(len(pictures))
            count += len(pictures)
            for picture in pictures:
                sql = 'insert into setu(name, url) values(%s, %s)'
                db.execute(sql, name, picture)
                print(picture)
            end_cursors = re.findall(r'"end_cursor":"(.*?)"}', json)
            if end_cursors == []:
                print('count=',count)
                print('overr')
                break
            end_cursor = end_cursors[0]
            print(end_cursor)
            url = self.base_url.format(id=id, end_cursor=end_cursor)#重写url
            has_next_page = re.findall(r'"has_next_page":(.*?),', json)[0]
            print(type(has_next_page))
            print(has_next_page)
            if (has_next_page == 'false'):
                print('count=', count)
                print('over')
                break
            time.sleep(2)



if __name__ == '__main__':
    spider = Spider()
    spider.run()




