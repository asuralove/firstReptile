from urllib import request
from urllib import parse
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': 'https://www.baidu.com/',
    }
#urlopen请求网页  Request增加请求头
# res = request.urlopen('http://www.baidu.com')
res =request.urlopen(request.Request('http://www.baidu.com',headers=headers))
print(type(res))
print(res.read())
print(res.getcode())

#将网页上的文件保存到本地
request.urlretrieve('http://www.baidu.com','baidu.html')

#urlencode进行编码  parse_qs进行解码
params = {'name':'张三','age':20,}
result = parse.urlencode(params)
print(result)
qs = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=hello+world&age=100"
print(parse.parse_qs(qs))
print('*'*30)
time.sleep(3)
url = 'http://www.baidu.com/s'

param = {'wd':'刘德华'}
qs = parse.urlencode(param)
url = url + '?' + qs
# print(request.urlopen(url).read())
print(request.urlopen(request.Request(url,headers=headers)).read())
