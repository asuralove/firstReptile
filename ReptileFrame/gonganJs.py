import requests
import execjs
import re
import time

def parse_url(url,session,cookie_str):

    headers = {
        'Referer': 'http://www.mps.gov.cn/n2253534/n2253535/index.html',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'DNT': '1',
        'Host': 'www.mps.gov.cn',
        'Upgrade-Insecure-Requests': '1',
     }
    session.headers.update(headers)
    print('session.headers:', session.headers)
    time.sleep(1.4)
    newcookie = {'__jsl_clearance': cookie_str}
    print('newcookie:', newcookie)
    r = session.get(url,cookies=newcookie)
    print(len(r.content))
    print(r.content)
    print('session.cookies:', session.cookies)
    titles = re.findall(r'<dd style.*?<a.*?>(.*?)</a>', r.content.decode('utf8'))
    print('titles:' + '\n'.join(titles))

def parse_js(text):
    js = re.findall(r'<script>(.*?)</script>',text)[0]
    js = js.replace('eval(','var zzz = (')
    print('js:'+ js)
    ct = execjs.compile(js)
    zzz = ct.eval('zzz') #获取js运行返回值
    print('zzz:' + zzz)
    cookie = re.findall(r'cookie=(.*?)Path=',zzz)[0]
    print('cookie:'+ cookie)
    js2 = 'var window={};var cookie =' +cookie + "'"
    print('js2:' +js2)
    ct2 = execjs.compile(js2)
    cookie1 = ct2.eval('cookie')
    print('cookie1:'+cookie1)
    __jsl_clearance = re.findall(r'__jsl_clearance=(.*?);Expires',cookie1)[0]
    print('__jsl_clearance:'+__jsl_clearance)
    return __jsl_clearance



def main():
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
    url = 'http://www.mps.gov.cn/n2253534/n2253535/index.html'
    session.headers.update(headers)
    r = session.get(url)
    print('r.text:' + r.text)
    cookie_str = parse_js(r.text)
    print('cookie_str:'+ cookie_str)
    parse_url(url,session,cookie_str)


if __name__ == '__main__':
    main()