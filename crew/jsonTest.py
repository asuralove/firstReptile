import json
books = [
    {
        'title':'西游记',
        'price':'23.1'
    },
    {
        'title':'红楼梦',
        'price':'13.2'
    }
]
#dumps将对象转json
json_str = json.dumps(books,ensure_ascii=False)
print(type(json_str))
print(json_str)
#直接dump到文件中
with open('a.json','w',encoding='utf-8') as fp:
    json.dump(books,fp,ensure_ascii=False)
#将json字符串load成对象
newbooks = json.loads(json_str,encoding='utf-8')
print(type(newbooks))
print(newbooks)