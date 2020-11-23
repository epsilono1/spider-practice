# coding:utf-8
import requests
from lxml import etree
import re
import pandas as pd
from openpyxl import load_workbook
import os
import time

base_url = 'https://book.douban.com/top250?start={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}


def parse_page(url):
    # 发请求
    try:
        r = requests.get(url, headers=headers, timeout=3)
    except Exception as e:
        print(f'请求出错：{e}')
        return ''
    # 解析
    sel = etree.HTML(r.text)
    table = sel.xpath('//*[@id="content"]/div/div[1]/div/table')

    for book in table:
        # 提出复杂情况项
        author = book.xpath('./tr/td[2]/p[1]/text()')[0].split('/')  # 含多项数据,有3,4,5,6项数据4种情况，先以4项数据为准采集，获取到后再清洗处理
        comment_num = book.xpath(
            './tr/td[2]/div[2]/span[3]/text()')[0],  # tuple
        comment = book.xpath('./tr/td[2]/p[2]/span/text()')  # 有些没有评论

        yield {
            'title': book.xpath('./tr/td[2]/div[1]/a/@title')[0],
            'author': author[0].strip(),
            'publisher': author[-3].strip(),
            'publish_time': author[-2].strip(),
            'price': re.findall(r'(\d+[.]?\d+)', author[-1])[0],  # 有些没有小数点，整元
            'score': book.xpath('./tr/td[2]/div[2]/span[2]/text()')[0],
            'comment_num': re.findall(r'(\d+)', comment_num[0])[0],
            'comment':  comment[0] if comment else ''  # 有些没有评论
        }


# 保存
def save(data):
    df = pd.DataFrame(data)
    df.to_csv('bookTop250.csv', mode='a', header=False,
              index=False, encoding='utf-8')

    # df.to_excel('bookTop.xlsx') #每一次循环数据会覆盖，只有最后一页数据

    # with pd.ExcelWriter('bookTop250.xlsx', engine='openpyxl', mode='a') as writer:  # pylint: disable=abstract-class-instantiated
    #     df.to_excel(writer, sheet_name='豆瓣读书250', header=False, index=False) #追加sheet, not in one.循环一次加一个sheet
    #     writer.save()


if __name__ == "__main__":

    for i in range(10):
        print(f'正在爬取第{i+1}页...')
        url = base_url.format(str(i*25))
        books = parse_page(url)
        if books:
            save(books)
            print(f"保存第{i+1}页成功")
        else:
            print(f"解析第{i+1}页失败")
        # 设置爬取间隔
        # if (i+1) % 3 == 0:
        #     time.sleep(1)
