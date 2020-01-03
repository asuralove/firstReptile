import requests

kw = {'wd':'中国'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
proxy = {
    'http': '171.14.209.180:27829'
}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s", params = kw, headers = headers)
#使用代理
#response = requests.get("http://www.baidu.com/s", params = kw, headers = headers,proxies=proxy)
# 查看响应内容，response.text 返回的是Unicode格式的数据 经过requests解码过得
print(response.text.encode('utf-8'))
print('*'*30)
# 查看响应内容，response.content返回的字节流数据
print(response.content.decode('utf-8'))

# 查看完整url地址
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)
#获取cookie
print(response.cookies)
print(response.cookies.get_dict())


#post请求 直接传入一个字典
url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
resp = requests.post(url, headers=headers, data=data)
# 如果是json数据，直接可以调用json方法
print(resp.json())