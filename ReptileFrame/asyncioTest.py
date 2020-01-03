import time
import asyncio

async def hi(msg,sec):
    print('enter hi(),{} @{}'.format(msg,time.strftime('%H:%M:%S')))
    await asyncio.sleep(sec)
    print('{} @{}'.format(msg,time.strftime('%H:%M:%S')))
    return sec

async def main():
    print('main() begin at {}'.format(time.strftime('%H:%M:%S')))
    tasks = []
    for i in range(1,5):
        #生成协程未运行
        t = asyncio.create_task(hi(i,i))
        tasks.append(t)
    #print('main asyncio sleeping')
    #await asyncio.sleep(2)
    for t in tasks:
        r = await t
        print('r:',r)
    print('end at {}'.format(time.strftime('%H:%M:%S')))

asyncio.run(main())