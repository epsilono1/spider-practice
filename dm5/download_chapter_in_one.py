
#测试爬取一章（一页一章情况）
#测试结果：成功抓取到图片链接，图片全是“正义”图片

import requests
import parsel
from urllib.parse import urlparse

url = 'http://www.dm5.com/m1063579/'

headers = {
    'host':'www.dm5.com',
    'Referer': 'http://www.dm5.com/m1063579/'
}
def main(url):
    try:
        r = requests.get(url,headers=headers,timeout=2) #获取章节图片页必须加headers
        print('章节页获取成功！')
        ret = parsel.Selector(text=r.text)
        div1 = ret.css('div#barChapter') #一页一章
        imgs = div1.xpath('./img/@data-src').getall()
        for img in imgs:
            print(img)
            img_name = urlparse(img).path.split('/')[-1]
            img_url = img
            get_img(img_url,img_name)
    except Exception as e:
        print('章节获取出错：',e)

def get_img(url,img_name):    
    try:
        ret = requests.get(url,timeout=2)
        with open(f'{img_name}','wb') as f:
            f.write(ret.content)
            print(f'保存{img_name}成功！')
    except Exception as e:
        print(f'图片{img_name}获取出错：{e}') 

if __name__ == '__main__':
    main(url)
    
    
    






























