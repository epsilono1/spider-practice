# coding:utf-8
import requests

params = {'wd':'python爬虫'}
url = 'http://www.baidu.com/s?'
try:
    r = requests.get(url, params=params)
    # print(r.status_code)
    r.raise_for_status()
    print(r.text[500:1000])
except Exception as e:
    print(f'爬取错误！{e}')
    
'''结果
200
/>
        <link rel="icon" sizes="any" mas
5496f291521eb75ba38eacbd87.svg">
        <link rel="search" type="applica
ontent-search.xml" title="百度搜索" />


<title>python爬虫_百度搜索</title>

'''