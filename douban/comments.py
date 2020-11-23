# coding:utf-8
'''爬取《姜子牙》20页短评共400条并保存到csv文件,并生成词云图
soft: python3.7.4
date: 2020-11-23
'''
import requests
from lxml import etree
import time
import random
import pandas as pd

import os
import csv
import jieba
from wordcloud import WordCloud

HEADERS = {'user-agent': 'Mozilla/5.0'}
s = requests.Session()


def login(url):
    '''
    reurn type: bool
    '''
    data = {
        'ck': None,
        'remember': 'false',
        'name': 'yourname',
        'password': 'yourpwd'
    }
    headers = {
        'Referer': 'https://accounts.douban.com/passport/login?source=movie'}
    HEADERS.update(headers)
    s.headers.update(HEADERS)
    try:
        r = s.post(url, data=data, timeout=3)
        r.raise_for_status()
        r.encoding = 'utf-8'
        if r.json().get('status') == 'success':
            print('登陆成功')
            return True
        if r.json().get('status') == 'failed':
            print('参数缺失')
            return False
    except Exception as e:
        print(f'登陆失败！{e}')
        return False


def get_page(url, page):
    try:
        r = s.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(f'爬取{page+1}页失败！{e}')
        return None


def parse_page(html):
    sel = etree.HTML(html)
    divs = sel.xpath('//div[contains(@class,"comment-item")]/div[2]')
    for div in divs:
        try:
            nick = div.xpath('./h3/span[2]/a/text()')[0]
            star = div.xpath('./h3/span[2]/span[2]/@class')[0][7:8]
            vote = div.xpath('./h3/span[1]/span/text()')[0]
            text = div.xpath('./p/span/text()')[0]
            yield [nick, star, vote, text]
        except Exception as e:
            print(f'解析失败！{e}')
            continue


def save(data, page):
    df = pd.DataFrame(data)
    if page == 0:
        csv_header = ['昵称', '星级', '有用', '评论']
        df.to_csv('./comments.csv', header=csv_header,
                  index=False, mode='a', encoding='utf-8')
    else:
        df.to_csv('./comments.csv', header=False,
                  index=False, mode='a', encoding='utf-8')


def ciyun():
    with open('./comments.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        columns = [row[-1] for row in reader]
        content = ''.join(columns)
        # 分词
        cut_text = ' '.join(jieba.cut(content, cut_all=True))

        # 加载停用词库
        with open('./停用词库.txt', 'r', encoding='utf-8') as uselessfile:
            stopwords = uselessfile.read().split('\n')

        # 生成词云图
        wc = WordCloud(
            # 不指定字体路径，会出现口字乱码
            font_path='C:/Windows/Fonts/STXINGKA.TTF',
            width=700,
            height=500,
            stopwords=stopwords
        ).generate(cut_text)

        # 保存词云图
        wc.to_file('词云图.jpg')

        # 显示词云图
        img = wc.to_image()
        img.show()


if __name__ == "__main__":
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    base_url = 'https://movie.douban.com/subject/25907124/comments?start={}'
    if login(login_url):
        del s.headers['Referer']  # 去掉Referer，添加Host
        s.headers.update({'Host': 'movie.douban.com'})

        page = 20
        for i in range(page):
            print(f'爬取第{i+1}页...')
            comment_url = base_url.format(str(20*i))
            if i % 3 == 0:  # 爬3页休息下
                time.sleep(random.random()*3)
            html = get_page(comment_url, i)
            if html:
                data = parse_page(html)
                save(data, i)
                print('保存成功')

    # 生成词云图
    if os.path.exists('./comments.csv'):
        print('生成词云图...')
        ciyun()
