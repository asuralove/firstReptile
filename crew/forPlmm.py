import requests
import random

#爬取https://tuchong.com  图片
def get_html_json_data(keyword,page):
    url = 'https://tuchong.com/rest/3/search/posts'
    params = {
        'query':keyword,
        'count':20,
        'page':page
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Referer':'https://tuchong.com/search/all/?query=%E7%8C%AB'
    }
    reponse = requests.get(url,params=params,headers=headers)
    json_data = reponse.json()
    print(reponse.json())
    #遍历图片
    for each_images in json_data['data']['post_list']:
        url = each_images['title_image']['url']
        if 'img_id' in each_images['title_image'] and 'user_id' in each_images['images'][0] :
            img_id = each_images['title_image']['img_id']
            user_id = each_images['images'][0]['user_id']
        else:
            img_id = str(random.randint(1,100)) + str(random.randint(1,100))
            user_id = str(random.randint(1,100)) + str(random.randint(1,100))
        print({'url':url,'user_id':user_id,'img_id':img_id})
            #下载图片
        # download_image(url,user_id,img_id)

def download_image(url,user_id,image_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)z AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    with open("C:/sifang/{}-{}.jpg".format(user_id,image_id),'wb')as f:
        f.write(response.content)

def main():
    # get_html_json_data('猫',1)
    for page in range(1,20):
        data = get_html_json_data('私房',page)


if __name__ == '__main__':
    main()
