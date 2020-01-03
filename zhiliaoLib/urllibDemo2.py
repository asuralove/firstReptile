from urllib import parse
from urllib import request

url = 'http://www.baidu.com/s?wd=python&username=abd#1'
#urlparse和urlsplit对这个url中的各个组成部分进行分割
res1 = parse.urlparse(url)
print(res1)
# res2 = parse.urlunsplit(url)
# print(res2)

#使用代理
handler = request.ProxyHandler({"http":"127.0.0.1:10809"})
opener = request.build_opener(handler)
req = request.Request("http://httpbin.org/ip")
resp = opener.open(req)
print(resp.read())