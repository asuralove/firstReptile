from lxml import etree
text = '''
<div class = "co">
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
print(html)
result = etree.tostring(html)
print(result.decode('utf-8'))
res = html.xpath('//*')
print(res)
print(len(res))
lis = html.xpath('//li')
print(lis)
print(len(lis))
# print(etree.tostring(lis)) 错误
print(etree.tostring(lis[0]).decode('utf-8'))
print(html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class'))#获取父节点属性
print(html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/parent::*/@class'))
print( html.xpath('//li[@class="item-0"]'))
print(html.xpath('//li[@class="item-0"]/a/text()'))
print(html.xpath('//li/a/@href'))
print(html.xpath('//div[@class="co"]//li'))