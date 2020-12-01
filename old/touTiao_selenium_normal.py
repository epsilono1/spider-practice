#selenium爬取头条图片
#可以正常存储数据，浏览器自动关闭
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os

folder = 'jiepai'
url = 'https://www.toutiao.com'
kw = '街拍'

browser = webdriver.Chrome()
browser.get(url)
# time.sleep(1) 
#搜索“街拍”
input = browser.find_element_by_css_selector('.tt-input__inner')
input.send_keys(kw)
input.send_keys(Keys.ENTER) 
browser.switch_to.window(browser.window_handles[1]) #切换到搜索结果标签页

#获取图片数据
imgs = browser.find_elements_by_css_selector('.img-wrap img')
if not os.path.exists(folder):
        os.mkdir(folder)
for img in imgs:  
    src = img.get_attribute('src') #获取标题页小图链接
    #图片url重构
    urls = src.split('list')  
    url0 = urls[0].replace('-'+urls[0].split('-')[1],'.pstatp.com/origin/')
    if len(urls[1].split('/')) > 2:
        urls[1] = urls[1].split('/')[-2]+'/'+urls[1].split('/')[-1]
    img_url =url0 + urls[1]
    
    #存储链接
    with open('{}/img.txt'.format(folder),'a') as f:    
        f.write(img_url+'\n')  

    #存储图片
    r = requests.get(img_url)
    path = '%s/%s.jpg'%(folder,img_url[-6:])
    with open(path,'ab') as f:
        f.write(r.content)

# time.sleep(3)
browser.quit()  