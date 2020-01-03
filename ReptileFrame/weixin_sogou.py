#!/usr/bin/env python3
# coding:utf-8
# Author: veelion

import urllib.parse as urlparse
import re
import time
import random
import requests
import lxml.html



class WeixinSogou:
    def __init__(self):
        self.uigs_para = {
            'uigs_productid': "vs_web",
            'terminal': "web",
            'vstype': "weixin",
            'pagetype': "index",
            'channel': "index_pc",
            'type': "weixin_search_pc",
            'wuid': '',
            'snuid': '',
            'uigs_uuid': str(int(1000 * time.time())) + str(random.randint(100, 1000)),
            'uigs_refer': 'HTTP/1.1',
        }
        self.select_time = {
            '0': 'select_time_all',
            '1': 'select_time_day',
            '2': 'select_time_week',
            '3': 'select_time_month',
            '4': 'select_time_year',
            '5': 'select_time_zdy', # custome time scope
        }
        self.has_init = False
        # self.init_session()

    def init_session(self,):
        if self.has_init:
            return
        self.has_init = True
        print('init session...')
        self.session = requests.Session()
        # self.session.proxies = {
        #     'http': 'http://127.0.0.1:8888',
        # }
        ua = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        }
        self.session.headers.update(ua)

        url = 'https://weixin.sogou.com/'
        r = self.session.get(url)

        pv_url = self.gen_pv_url()

        r = self.session.get(pv_url)
        print('pv_url got cookies:', r.cookies)
        print('init session...done!')

    def gen_pv_url(self,):
        url_pre = "http://pb.sogou.com/pv.gif?uigs_t={}".format(int(time.time()*1000))
        param = ['{}={}'.format(k, v) for k, v in self.uigs_para.items()]
        url = url_pre + '&' + '&'.join(param)
        return url

    def gen_cl_url(self, select_type, referrer):
        a = ["http://pb.sogou.com/cl.gif?uigs_cl=", select_type, "%26uigs_refer=", urlparse.quote(referrer, safe='')]
        for k, v in self.uigs_para.items():
            if isinstance(v, str):
                v = urlparse.quote(v, safe='')
            p = '&{}={}'.format(k, v)
            a.append(p)
        return ''.join(a)

    def update_uigs_para(self, html):
        m = re.search(r'var uigs_para = ({.*?})', html, re.DOTALL)
        if not m:
            print('update_uigs_para got nothing')
            return
        para = m.groups()[0]
        para = re.sub(r'login.*?,', 'login":"0",', para)
        print(para)
        self.uigs_para = eval(para)

    def gen_url(self, word, tsn='', ft='', et=''):
        '''
        word: keyword to search,
        tsn: time scope name:
            0: all,
            1: day,
            2: week,
            3: month,
            4: year,
            5: zdy,
        ft: from time,
        et: end time,
        '''
        pre = 'https://weixin.sogou.com/weixin?type=2&query={}'
        url = pre.format(word)
        if tsn in self.select_time and tsn != 5:
            url += '&tsn=' + tsn
        if tsn==5 and ft and et:
            url += '&tsn=5&ft={}&et={}'.format(ft, et)
        return url

    def fetch(self, url):
        print('crawling...', url)
        if 'tsn' in url:
            referrer = 'https://weixin.sogou.com/weixin?type=2&query=python'
            tsn = re.findall(r'tsn=(\d)', url)[0]
            select_time = self.select_time.get(tsn, '')
            cl_url = self.gen_cl_url(select_time, referrer)
            self.session.get(cl_url)
            self.session.headers.update({'referer': referrer})
        r = self.session.get(url)
        if r.url == 'https://weixin.sogou.com/':
            raise Exception('error: redirect to home')
        r.encoding = 'utf8'
        return r.text

    def extract_search_link(self, html):
        hrefs = re.findall(r'<h3>.*?<a .*?href="(/link?.*?)"', html, re.DOTALL)
        hrefs = set(hrefs)
        pre = 'https://weixin.sogou.com'
        hrefs = [pre+urlparse.unquote(h) for h in hrefs]
        good = []
        for href in hrefs:
            b = random.randint(1,100)
            a = href.find('url=')
            a = href[a+4 + 21 + b]
            new = href + '&k={}&h={}'.format(b, a)
            good.append(new)
        # get next pages
        nexts = re.findall(r'<a id="sogou_page.*?href="(.*?)"', html)
        pre = 'https://weixin.sogou.com/weixin'
        nexts = [pre+n for n in nexts]
        return good, nexts

    def extract_weixin_data(self, url, html):
        with open('z-weixin-post.html', 'w') as f:
                f.write(html)
        try:
            doc = lxml.html.fromstring(html)
        except:
            return None
        item = {}
        item['p_url'] = url
        title = doc.xpath('//h2[@id="activity-name"]/text()')
        if not title:
            print('\tno title of:', url)
            return None
        item['p_title'] = title[0].strip()
        item['gzh_name'] = doc.xpath('//a[@id="js_name"]/text()')[0].strip()
        item['gzh_id'] = doc.xpath('//span[@class="profile_meta_value"]/text()')[0]
        item['p_data'] = doc.xpath('//div[@id="js_content"]')[0].text_content().strip()
        ct = re.search(r'var ct = "(.*?)"', html)
        ct = ct.groups()[0]
        tu = time.localtime(int(ct))
        item['p_date'] = time.strftime('%Y-%m-%d %H:%M:%S', tu)
        del doc
        return item

    def process_weixin(self, sogou_link, i):
        '''call this to download weixin post'''
        cl_url = self.gen_cl_url('article_title_%s'%i, sogou_link)
        print('cl_url:', cl_url)
        self.session.get(cl_url)
        print('crawl:', sogou_link)
        r = self.session.get(sogou_link)
        print(r.content.decode('utf8'))
        ss = re.findall(r"url \+= '(.*?)'", r.content.decode('utf8'))
        if not ss:
            print('wrong page')
            return None
        weixin_url = ''.join(ss).replace("@", '')
        if 'http://mp.weixin.qq.com/profile' in weixin_url:
            print('weixin user url:', weixin_url)
            return None

        r = self.session.get(weixin_url)
        r.encoding = 'utf8'
        item = self.extract_weixin_data(weixin_url, r.text)
        return item

    def process(self, url):
        '''call this to download sogou search'''
        html = self.fetch(url)
        with open('zz.html', 'w') as f:
                f.write(html)
        links, nexts = self.extract_search_link(html)
        self.update_uigs_para(html)
        return links, nexts


if __name__ == '__main__':
    import sys
    from pprint import pprint
    opt = sys.argv[1]
    cc = WeixinSogou()
    if opt == 'extract':
        html = open('./z-wx-post.html').read()
        item = cc.extract_weixin_data('', html)
        print(item)
    elif opt == 'search':
        cc.init_session()
        url = cc.gen_url('猿人学', tsn='1')
        links, nexts = cc.process(url)
        print(links)
        print(nexts)
        item = cc.process_weixin(links[0], 0)
        pprint(item)
    elif opt == 'update':
        html = open('zz.html').read()
        cc.update_uigs_para(html)
        print(cc.uigs_para)
    else:
        pass

