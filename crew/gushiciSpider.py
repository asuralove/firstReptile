import requests
import re
'''
爬取古诗词网练习正则
'''
def parse_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    response = requests.get(url,headers)
    text = response.text
    #re,S = re.DOTALL
    titles = re.findall(r'<div\sclass="cont".*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source".*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source".*?<a.*?>.*?</a>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_des = re.findall(r'<div\sclass="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    poems = []
    for content_de in content_des:
        x = re.sub(r'<.*?>',"",content_de).strip()
        contents.append(x)

    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content,
        }
        poems.append(poem)
    print(poems)

def main():
    url = 'https://www.gushiwen.org/default_5.aspx'
    for x in range(1,11):
        url = 'https://www.gushiwen.org/default_%s.aspx' %x
        parse_page(url)


if __name__ == '__main__':
    main()
