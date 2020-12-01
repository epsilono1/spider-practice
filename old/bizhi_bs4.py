# requests + BeautifulSoup + CSS 爬取案例2

import requests
from bs4 import BeautifulSoup
import os

base_url = 'http://www.obzhi.com/category/renwubizhi/page/'
pages = 6
folder = 'people'

def onePage(url):
    r = requests.get(url,timeout = 5)
    soup = BeautifulSoup(r.text,'lxml')
    results = soup.select('.post.box.row.fixed-hight') #属性多值匹配
    #提取image链接
    for result in results:
        img = result.find('img').get('src').split('=')[1].replace('&h','')
        #存储
        rep = requests.get(img)
        if not os.path.exists(folder):
            os.mkdir(folder)
        path = '%s/%s'%(folder,img.rsplit('/',1)[1]) #rsplit('/',1)指从右边分割一个出来，rsplit('/',2)从右分割两个出来
        with open(path,'wb') as f:
            f.write(rep.content)          
       
if __name__ == '__main__':
    for page in range(1,pages+1):
        url = base_url + str(page)
        print('第%s页..'%page)
        onePage(url)
    print('完成！')