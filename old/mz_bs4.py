# requests + BeautifulSoup + CSS 爬 https://gank.io/special/Girl/page/1

import requests
from bs4 import BeautifulSoup
import os

base_url = 'https://gank.io/special/Girl/page/'
base_image = 'https://gank.io'
folder = 'Girls'
pages = 10

def onePage(url):
    r = requests.get(url, timeout = 5)
    soup = BeautifulSoup(r.text,'lxml')
    results = soup.select('div[class="media media-21x9 mb-md-3"]') #获取所有图片标签
    
    #获取图片链接 (选择器结果有内标签)
    for a in results:
        short_url = a.find('a').get('style').split('\'')[1] #先提取内标签<a>;提取属性值用 get()，提取文本用 get_text()
        image = base_image + short_url
        
        #存储
        image_r = requests.get(image, timeout = 5)
        if not os.path.exists(folder):
            os.mkdir(folder)
        path = '%s/%s.jpg' % (folder, short_url[-3:])
        with open(path, 'wb') as f:
            f.write(image_r.content)
            
def main(pages):
    for i in range(1,pages+1):
        url = base_url + str(i)
        print('正在爬取第%s页...'%i)
        onePage(url)
    print('爬取完成')
    
if __name__ == '__main__':
    main(pages)
