#zip的使用 将对象中的元素打包成一个个元祖，组成列表
import re
import random
from typing import List

print(type(str(random.randint(1,100))))


def twoSum(self, nums: List[int], target: int) -> List[int]:
    list = []
    for num in nums:
        for n in nums[(nums.index(num) + 1):]:
            if (num + n == target):
                list.append(nums.index(num))
                list.append(nums.index(n))
                return list
print(twoSum(7,[3,0,7,5],8))

def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive
g=gen()
print(g.send(None))
print(g.send('hello'))
print(g.send(123456))
print(g.send('e'))
print('#'* 30)
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


mylist = [x*x for x in range(3)]
for i in mylist :
    print(i)

mygenerator = (x*x for x in range(3))
#生成器只能被迭代一次
for i in range(2):
    for i in mygenerator :
        print(i)



title = '\n\r冰岛巨型冰川雄伟壮阔：人与自然同框秒变“小斑点”\n'
new = re.sub(r'\.[1]',"为什么",title)
print(new)
print(title.replace('\n','123').replace('\r','456'))

str = {'width': 1094, 'height': 731, 'url': 'https://tuchong.pstatp.com/2977435/lr/57606834.jpg'}
print(str['url'])

a = [1,2,3]
b = [4,5,6]
c = [3,4,5,6,7]
print(zip(a,b))
d = zip(a,b)
print(type(d))
for di in d:
    print(di)



