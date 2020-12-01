#selenium爬取头条街拍图片
#问题1：有时候会没有存储数据，不晓得为啥
#问题2：采用模块化后，浏览器不会自动关闭了
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support expected_conditions as EC

import time
import requests
import os

folder = 'jiepai'
url = 'https://www.toutiao.com'
kw = '街拍'

def get_img(url):
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
    for img in imgs:  
        src = img.get_attribute('src') #获取标题页小图链接
        #图片url重构
        urls = src.split('list')  
        url0 = urls[0].replace('-'+urls[0].split('-')[1],'.pstatp.com/origin/')
        if len(urls[1].split('/')) > 2:
            urls[1] = urls[1].split('/')[-2]+'/'+urls[1].split('/')[-1]
        img_url =url0 + urls[1]
        yield img_url
    
def save_img(img_url):
    if not os.path.exists(folder):
        os.mkdir(folder)
    #存储链接
    with open('{}/img.txt'.format(folder),'a') as f:    
        f.write(img_url+'\n')  

    #存储图片
    r = requests.get(img_url)
    path = '%s/%s.jpg'%(folder,img_url[-6:])
    with open(path,'ab') as f:
        f.write(r.content)

def main(url):
    imgs = get_img(url)
    for img in imgs:
        save_img(img)
        
if __name__ == '__main__':
    main(url)
#     time.sleep(2)
#     if browser:   
#         browser.quit() #奇怪：加上此句，浏览器不会自动关掉，抓取的数据也没有；如果把此句放入get_img模块，可以自动关闭浏览器，但没有数据