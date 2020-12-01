# coding:utf-8
import requests
from lxml import etree
import json
import urllib3 # 用于消除ssl禁用警告

# 消除ssl禁用警告 InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
headers = {'user-agent':'Mozilla/5.0'}
def get_page(url):
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(f'爬取失败！{e}')
        return None
    
def parse_page(html):
    selector = etree.HTML(html)
    trs = selector.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr')
    for tr in trs:
        rank = tr.xpath('./td[1]/text()')[0].strip()
        univer = tr.xpath('./td[2]/a/text()')[0]
        yield {rank:univer}

def save_data(data) ->None:
    with open('univer_rank.json','w',encoding='utf-8') as f:
        for item in data:
            print(f'\r正在保存{item}',end='')
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
        print('\n保存成功')
def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
    html = get_page(url)
    if html:
        data = parse_page(html)    
        save_data(data)
    
if __name__ == '__main__':
    main()