#coding:utf-8
#python3.7.4
# 先爬章节有页码列表的漫画
#先下一章的图片
#先下一张图片
import requests
import re
import execjs
import os
from urllib.parse import urlparse

chapter_url = 'http://www.dm5.com/m1058716/'
JS_API = 'http://www.dm5.com/m1058716-p2/chapterfun.ashx?cid=1058716&page={}&key=&language=1&gtk=6&_cid=1058716&_mid=61292&_dt={}&_sign={}'
headers = {
    'Referer': 'http://www.dm5.com'
}
PATH = '动漫/怪兽8号/第10话'

def get_img(js_api):
    try:
        r = requests.get(js_api,headers=headers,timeout=2)
        imgs = execjs.eval(r.text) #js执行eval函数
        img = imgs[0]
        return img
    except Exception as e:
        print('api请求出错：',e)
        
def download(url,img_name):
    _path = os.sep.join([PATH,img_name])
    r = requests.get(url)
    with open(_path,'ab') as f:
        f.write(r.content)
        print(f'--->{img_name}下载成功<')
    
    
    
if __name__ == '__main__':
    #获取每页接口参数
    r = requests.get(chapter_url)
    _dt = re.findall('DM5_VIEWSIGN_DT="(.*?)";',r.text)[0]
    _sign = re.findall('DM5_VIEWSIGN="(.*?)"',r.text)[0]
    pages = int(re.findall('DM5_IMAGE_COUNT=(.*?);', r.text)[0])
    
    if not os.path.exists(PATH): #创建相关文件夹
        os.makedirs(PATH) #注意不要写成 mkdir（只能创建一层），make别写成mk
    
    for page in range(1,pages+1):
        js_api = JS_API.format(page, _dt, _sign)
        img = get_img(js_api)
        img_name = urlparse(img).path.split('/')[-1]
        download(img,img_name)
    print('第10话下载完成！')
    
    
    
    