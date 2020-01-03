from urllib import request,parse
from http.cookiejar import CookieJar


'''
#手写cookie访问个人网页
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Cookie': 'anonymid=k3ifhniraebw4a; depovince=GW; _r01_=1; JSESSIONID=abcwCudYfx1Yhh3TRbX6w; ick_login=8a8b52c1-3de5-4d85-a90b-5035887bed2b; t=b402c1b7baf8ecec76c094d52431fc9b5; societyguester=b402c1b7baf8ecec76c094d52431fc9b5; id=972970875; xnsid=4ef87479; ver=7.0; loginfrom=null; jebe_key=0f39238a-69e8-4b1f-a52a-df5944edd34a%7C861bef4875ac25595a626f42ed6e5165%7C1574928095397%7C1%7C1574928095471; jebe_key=0f39238a-69e8-4b1f-a52a-df5944edd34a%7C861bef4875ac25595a626f42ed6e5165%7C1574928095397%7C1%7C1574928095474; wp_fold=0; jebecookies=48ab04ed-4415-4754-b3f2-1686a33c5bce|||||'
}

url = 'http://www.renren.com/972970875/profile'


req = request.Request(url,headers=headers)
resp = request.urlopen(req)
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))
    
'''

#使用登录后将cookie存储到cookiejar
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    data = {"email": "970138074@qq.com", "password": "pythonspider"}
    data = parse.urlencode(data).encode('utf-8')
    login_url = "http://www.renren.com/PLogin.do"
    #post请求
    req = request.Request(login_url, headers=headers, data=data)
    opener.open(req)

def visit_profile(opener):
    url = 'http://www.renren.com/880151247/profile'
    req = request.Request(url,headers=headers)
    #获取个人主页页面时候 不要新建一个opener  之前那个opener已经包含登录所需的cookie信息
    resp = opener.open(req)
    with open('renren.html','w') as fp:
        fp.write(resp.read().decode("utf-8"))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)

