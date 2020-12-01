import requests
from lxml import etree

url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    trs = selector.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr')
    for tr in trs[:20]:
        rank = tr.xpath('./td[1]/text()')[0].strip() 
        univer = tr.xpath('./td[2]/a/text()')[0]
        print(rank + ':' + univer)
   
except Exception as e:
    print(f'爬取失败！{e}')
    
