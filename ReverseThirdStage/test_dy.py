import requests
import time
import json

channel_header = {
  'Accept-Encoding': 'gzip',
  'User-Agent': 'com.ss.android.ugc.aweme.lite/203 (Linux; U; Android 6.0; zh_CN; Nexus 6P; Build/MDA89D; Cronet/58.0.2991.0)',
  #'X-SS-TC': '0',
  #'X-Khronos': '1573478823',
  #'X-Gorgon': '032456cc000058570ca7dcdd8cfda9c4732439fe05b8b02b07dea',
  #'X-SS-REQ-TICKET': '1573478823322',
  'Connection': 'keep-alive',
  'Host': 'aweme.snssdk.com'
}

#'https://aweme.snssdk.com/aweme/v1/challenge/aweme/?ch_id=1649450080661508&query_type=0&cursor=0&count=20&type=5&retry_type=no_retry&iid=91658564592&device_id=69852570923&ac=wifi&channel=xiaomi&aid=2329&app_name=douyin_lite&version_code=203&version_name=2.0.3&device_platform=android&ssmix=a&device_type=Nexus+6P&device_brand=google&language=zh&os_api=23&os_version=6.0&openudid=dd08f504420bcde0&manifest_version_code=203&resolution=1440*2392&dpi=560&update_version_code=2030&_rticket=1573385459665&ts=1573385457&as=aad341fde85dc7f4f3d341&cp=fe38d341fde8d341fe3032&mas=01199323991959b313f319b9b985dc10f0b313f319f3591359d3f9'
r = requests.get(url='https://aweme.snssdk.com/aweme/v1/challenge/aweme/?ch_id=1646112699144196&query_type=0&cursor=0&count=20&type=5&retry_type=no_retry&iid=91658564592&device_id=69852570923&ac=wifi&channel=xiaomi&aid=2329&app_name=douyin_lite&version_code=203&version_name=2.0.3&device_platform=android&ssmix=a&device_type=Nexus+6P&device_brand=google&language=zh&os_api=23&os_version=6.0&openudid=dd08f504420bcde0&manifest_version_code=203&resolution=1440*2392&dpi=560&update_version_code=2030&_rticket=1573478104709&ts=1573478103&as=aad363ede85dc95ed8d363&cp=ee38d363ede8d363ee3034&mas=01199323991999f353f319b9b985ac4524f353f31923199993a3f9', verify=False, headers=channel_header)
print(r.status_code)
print(r.text)
#with open('D:/code/test_decompile/dy/test.txt','w') as f:
#    f.write(r.text)


# detail_header = {
#   'Accept-Encoding': 'identity',
#   'User-Agent': 'okhttp/3.10.0.1 vpwp/',
#   #'X-SS-TC': '0',
#   #'X-Khronos': '1573196036',
#   #'X-Gorgon': '03006cc0000584aa92b9cdd8cfad0a17cb929fe05b8b32bd5836',
#   #'X-SS-REQ-TICKET': '1573196036485',
#   'Connection': 'keep-alive',
#   'Host': 'v9-dy.ixigua.com'
# }
# #心动飞吻 channel 第一个视频 url
# #'http://v9-dy.ixigua.com/329fceabb797fe1c38836803e66fe923/5dc80310/video/m/22042f5b1e82e9c4a0d97be1cf48d71a15d116414b9c00000d1eb495cfaf/?a=2329&br=442&cr=0&cs=0&dr=0&ds=6&er=&l=20191110193058010012064224432C72&lr=&qs=0&rc=am9uaHZvanJncTMzaGkzM0ApOjg3O2Y0Ozs8NzdlNTtkM2duNWJmLWU1aS5fLS00LS9zczY2YTBgNWI2M2AtYTViXmI6Yw%3D%3D&device_platform=android&device_type=Nexus+6P&version_code=203&device_id=69852570923&channel=xiaomi'
# r = requests.get(url='http://v9-dy.ixigua.com/329fceabb797fe1c38836803e66fe923/5dc80310/video/m/22042f5b1e82e9c4a0d97be1cf48d71a15d116414b9c00000d1eb495cfaf/?a=2329&br=442&cr=0&cs=0&dr=0&ds=6&er=&l=20191110193058010012064224432C72&lr=&qs=0&rc=am9uaHZvanJncTMzaGkzM0ApOjg3O2Y0Ozs8NzdlNTtkM2duNWJmLWU1aS5fLS00LS9zczY2YTBgNWI2M2AtYTViXmI6Yw%3D%3D&device_platform=android&device_type=Nexus+6P&version_code=203&device_id=69852570923&channel=xiaomi', verify=False, headers=detail_header)
# print(r.status_code)
# with open('D:/code/test_decompile/dy/test_video.mp4','wb') as f:
#     f.write(r.content)

#print(r.text)


