import requests
import time
import json
import hook_dy_rpc

def download_video(url, video_id):
    detail_header = {
        'Accept-Encoding': 'identity',
        'User-Agent': 'okhttp/3.10.0.1 vpwp/',
        'Connection': 'keep-alive',
    }
    #心动飞吻 channel 第一个视频 url
    #'http://v9-dy.ixigua.com/329fceabb797fe1c38836803e66fe923/5dc80310/video/m/22042f5b1e82e9c4a0d97be1cf48d71a15d116414b9c00000d1eb495cfaf/?a=2329&br=442&cr=0&cs=0&dr=0&ds=6&er=&l=20191110193058010012064224432C72&lr=&qs=0&rc=am9uaHZvanJncTMzaGkzM0ApOjg3O2Y0Ozs8NzdlNTtkM2duNWJmLWU1aS5fLS00LS9zczY2YTBgNWI2M2AtYTViXmI6Yw%3D%3D&device_platform=android&device_type=Nexus+6P&version_code=203&device_id=69852570923&channel=xiaomi'
    print('download video')
    r = requests.get(url=url, verify=False, headers=detail_header)
    print(r.status_code)
    with open('D:/code/test_decompile/dy/{}.mp4'.format(video_id),'wb') as f:
        f.write(r.content)

def start():
    channel_header = {
    'Accept-Encoding': 'gzip',
    'User-Agent': 'com.ss.android.ugc.aweme.lite/203 (Linux; U; Android 6.0; zh_CN; Nexus 6P; Build/MDA89D; Cronet/58.0.2991.0)',
    #'X-SS-TC': '0',
    #'X-Khronos': '1573196036',
    #'X-Gorgon': '03006cc0000584aa92b9cdd8cfad0a17cb929fe05b8b32bd5836',
    #'X-SS-REQ-TICKET': '1573196036485',
    'Connection': 'keep-alive',
    'Host': 'aweme.snssdk.com'
    }

    r = requests.get(url='https://aweme.snssdk.com/aweme/v1/challenge/aweme/?ch_id=1649450080661508&query_type=0&cursor=20&count=20&type=5&retry_type=no_retry&iid=91658564592&device_id=69852570923&ac=wifi&channel=xiaomi&aid=2329&app_name=douyin_lite&version_code=203&version_name=2.0.3&device_platform=android&ssmix=a&device_type=Nexus+6P&device_brand=google&language=zh&os_api=23&os_version=6.0&openudid=dd08f504420bcde0&manifest_version_code=203&resolution=1440*2392&dpi=560&update_version_code=2030&_rticket=1573385459665&ts=1573385457&as=aad341fde85dc7f4f3d341&cp=fe38d341fde8d341fe3032&mas=01199323991959b313f319b9b985dc10f0b313f319f3591359d3f9', verify=False, headers=channel_header)
    
    print(r.status_code)

    data = json.loads(r.text)

    for i in data['aweme_list']:
        print('***video id/forward_count/play_count/digg_count/comment_count/share_count/download_count***')
        print('{}/{}/{}/{}/{}/{}/{}'.format(i['statistics']['aweme_id'],i['statistics']['forward_count'],\
        i['statistics']['play_count'],i['statistics']['digg_count'],i['statistics']['comment_count'],\
            i['statistics']['share_count'], i['statistics']['download_count']))

        download_video(i['video']['play_addr']['url_list'][0], i['statistics']['aweme_id'])

start()