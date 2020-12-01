#ajax+requests.post+response.json
#爬到1517张后出现“MissingSchema: Invalid URL '': No schema supplied. Perhaps you meant http://?”错误
#经过获取标题和链接分析，发现第1518张图片链接为空，所以发生以上错误，可以通过添加if语句解决
import requests
import os

url = 'http://yywallpaper.top/query/picture'
folder = 'bizhi'

def get_page(page):
    data = {
        'picType':0,
        'pageNum':page,
        'pageSize':10
    }
    r = requests.post(url,data=data)
    return r.json()
def get_images(results):
    if(results.get('elements')):
        for item in results.get('elements'):
            yield item.get('bigUrl')
              
def save_image(item):
    if item:  #链接不为空
        rsp = requests.get(item)
        with open('%s/%s'%(folder,item.split('/')[-1]),'wb') as f:
            f.write(rsp.content)
        
if __name__ == '__main__':
    rst = get_page(1)
    if rst.get('elements'):
        totalNum = rst.get('totalNumber')
        totalPage = rst.get('totalPageCount')
        print('totalNum:%s,totalPage:%s'%(totalNum,totalPage))
    if not os.path.exists(folder):
        os.mkdir(folder)
    for i in range(1,totalPage+1): 
        results = get_page(i)
        items = get_images(results) #img_urls
        for item in items:
            save_image(item)