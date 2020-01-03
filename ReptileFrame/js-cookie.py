#!/usr/bin/env python3
# coding:utf-8
# Author: veelion


import time
import urllib.parse as urlparse
import execjs
import re
import requests


print(execjs.get().name)

def go(url, session, cookie_dict):
    print('cookie_dict:'+'\n', cookie_dict)
    key = '__jsl_clearance'
    value = cookie_dict.pop(key)
    # session.cookies.set(key, value, **cookie_dict)
    # print(session.cookies)
    new = {
        'Referer': 'http://www.mps.gov.cn/n2253534/n2253535/index.html',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'DNT': '1',
        'Host': 'www.mps.gov.cn',
        'Upgrade-Insecure-Requests': '1',
    }
    session.headers.update(new)
    print('session.headers:', session.headers)
    time.sleep(1.4)
    newcookie = {key: value}
    print('newcookie:',newcookie)
    r = session.get(url, cookies=newcookie)
    # r = session.get(url)
    print('len(r.text):')
    print( len(r.text))
    print(r.content)
    print('session.cookies:',session.cookies)
    with open('z.html', 'wb') as f:
        f.write(r.content)
    print('len(r.content):')
    print( len(r.content))

    titles = re.findall(r'<dd style.*?<a.*?>(.*?)</a>', r.content.decode('utf8'))
    print('titles:'+ '\n'.join(titles))

    # if r.text.startswith('<script>'):
    #     return go(url, session, key, value, cookie_dict)



def parse_js(text):
    js = re.findall(r'<script>(.*?)</script>', text)
    js = js[0]
    with open('z-js.js', 'w') as f:
        f.write(js)
    js = js.replace('eval(', 'var zzz = (')
    print('js:'+ js)

    ctx = execjs.compile(js)
    zzz = ctx.eval('zzz')
    print('zzz:'+ zzz)

    p_begin = zzz.find('cookie')
    if p_begin < 0:
        return None
    p_end = zzz.find("Path=/;'") + len("Path=/;'")

    new_js = 'var window={}; var ' + zzz[p_begin:p_end]
    print('new_js:'+ new_js)

    ctx = execjs.compile(new_js)
    cookie_str = ctx.eval('cookie')
    print('cookie_str:'+ cookie_str)
    # __jsl_clearance=1562638360.469|0|BwZgllDMTblN%2FL8bc%2FGWscSP8w8%3D;Expires=Tue, 09-Jul-19 03:12:40 GMT;Path=/;
    #strip 去除头尾指定字符
    zz = cookie_str.strip(';').split(';')
    print(type(zz))
    print(zz)
    cookie_dict = {}
    for z in zz:
        k, v = z.split('=')
        cookie_dict[k] = v
    # cookie_dict['expires'] = time.mktime(time.strptime(cookie_dict['expires'], time_format)) + 25200
    cookie_dict['Domain'] = 'www.mps.gov.cn'
    return cookie_dict


def crawl():
    session = requests.Session()
    ## 设置cookies 代理，查看发送的cookies有无问题
    # session.proxies = {
    #     'http': 'http://127.0.0.1:8888',
    # }
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
    url = 'http://www.mps.gov.cn/n2253534/n2253535/index.html'
    #不同的请求方式 把请求头刷新进去
    session.headers.update(ua)
    r = session.get(url)
    print('r.text:'+ r.text)

    cookie_dict = parse_js(r.text)
    if cookie_dict:
        go(url, session, cookie_dict)
    else:
        print('failed to get cookie')



if __name__ == '__main__':
    crawl()
