#抓取豆瓣电影练习xpath

import requests
from lxml import etree
# 1.将目标网页上的页面抓取下来
headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",

    'Referer ': "https://movie.douban.com/cinema/nowplaying/beijing/"
}
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
response = requests.get(url,headers=headers)
text = response.text
# print(response.text)

#response.text 返回的是一个经过解码后的字符串，是str（unicode）类型
#response.content 返回的是一个原生的字符串，就是从网页上抓取下来的，没有
#经过处理的字符串，是byte类型

# 2.将抓取下来的数据根据一定的规则进行抓取
#xpath返回的是一个列表
html = etree.HTML(text)
print(html)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))
lis = ul.xpath("./li")

liiii = lis[0]
titles = liiii.xpath("@data-title")
print(titles)
print(titles[0])
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]

    movie = {
        'title':title,
        'score': score,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail,
    }
    movies.append(movie)

print(movies)

