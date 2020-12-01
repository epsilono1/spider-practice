# -*- coding: utf-8 -*-

'''
title：爬取云代理网站免费代理
author: epsilono1
date: 2020年10月6日 14:33:51
软件：python3.7
'''
import requests
import parsel  #含有xpath,css,re解析工具
import time

class Proxy():
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        self.proxies = []
        
    def getPage(self, url):
        #url
        #headers
        #发送请求
        try:
            response = requests.get(url, headers=self.headers, timeout=3)
        except:
            print('请求出错')
            return None
        response.encoding = 'gb2312'
        # 解析数据
        if response.status_code == 200:
            sel = parsel.Selector(response.text)
            trs = sel.xpath('//*[@id="list"]/table/tbody/tr')
            for tr in trs:
                ip = tr.xpath('./td[1]/text()').get()
                port = tr.xpath('./td[2]/text()').get()
                # protocol = tr.xpath('./td[4]/text()').get()
                self.proxies.append(':'.join([ip,port]))
                # self.proxies.append(''.join([protocol, '://', ip, ':', port]))

    def run(self):
        for page in range(1, 11):
            url = 'http://www.ip3366.net/?stype=1&page={}'.format(str(page))
            print('=============第{}页========'.format(page))
            self.getPage(url)
            time.sleep(1)  #设置每页爬取间隔
            # self.proxies.append(proxy)
        self.sav(self.proxies)


        # 保存
    def sav(self, data):
        with open('proxies.txt', 'w') as f:
            for proxy in data:
                f.write(proxy + '\n')

        #检测可用性

if __name__ == '__main__':
    proxy = Proxy()
    proxy.run()