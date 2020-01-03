import requests
import re

'''
爬取ins博主图片初次失败作
'''
headers = {
    'origin' : 'https://www.instagram.com',
    'referer' : 'https://www.instagram.com/maousamaii/',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'x-csrftoken': 'E02eq9L12I104bzHwqqUVWJhmcjyZL0J',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0fVmB70v7trPZvL9AiGrNyLUmSoWbU0kkPBvsT61AEZNvs',
    'x-requested-with': 'XMLHttpRequest'
}
URL = 'https://www.instagram.com/maousamaii/'

proxy = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809'
}

def crawl():
    try:
        res = requests.get(URL,headers=headers,proxies=proxy)
        # print(res.text)
        pictures = re.findall(r'"src":"(.*?)",',res.text)
        print(type(pictures))
        print(len(pictures))
        for picture in pictures:
            #picture.replace('\u0026','&')#replace 不会改变原 string 的内容
            picture = picture.encode('utf-8').decode('unicode-escape')
            print(picture)#图片url   有60张图片 每五张内容是一样的
            # with open("C:/ins/{}.jpg".format(a), 'w')as f:
            #     f.write(picture)
    except Exception as e:
        raise e

if __name__ == '__main__':
    crawl()