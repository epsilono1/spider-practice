# 爬取 https://gank.io/special/Girl/page/10 的全部妹纸图(一期一张，共93期，10页)
# 拟用 requests + lxml.etree.HTML() + xpath 爬取图片

import requests
from lxml import etree
import os

base_url = 'https://gank.io/special/Girl/page/'
base_image = 'https://gank.io'
folder = 'Girls2'
pages = 10

def pageOne(url):
    try:
        resp = requests.get(url, timeout = 5)
        html = etree.HTML(resp.text) #response先转Element对象，才进行数据提取
        results = html.xpath('//div[@class="media media-21x9 mb-md-3"]')

        for result in results:
            image_url = result.xpath('./a/@style')[0].split('\'')[1]
            image = base_image + image_url

            #下载
            r = requests.get(image)
            if not os.path.exists(folder):
                os.mkdir(folder)
                print('文件夹%s创建成功'%folder)
            path = '%s/%s.jpg'%(folder,image[-3:])
            with open(path,'wb') as f:
                f.write(r.content)
    except:
        print('爬取错误')
 
if __name__ == '__main__':
    for i in range(1,pages+1):
        url = base_url + str(i)
        print('爬取第%s页...'%i)
        pageOne(url)
    print('爬取完成')