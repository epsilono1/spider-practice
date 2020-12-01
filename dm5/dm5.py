# coding:utf-8
import requests
import json
import os
import parsel
import re
from urllib.parse import urlparse, urlencode
import execjs

headers = {
    'Referer': 'http://www.dm5.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
LIST_API = 'http://www.dm5.com/dm5.ashx?'
JS_API = 'http://www.dm5.com/m1058716-p2/chapterfun.ashx?'
HOST = 'http://www.dm5.com'


def get_comics_list(page):
    data = {
        'pagesize': 68,
        'pageindex': page,
        'tagid': 0,
        'areaid': 0,
        'status': 0,
        'usergroup': 0,
        'pay': -1,
        'char': None,  # 注意网页上这个参数啥都没有，不要写成0，不然得到错误数据
        'sort': 10,
        'action': 'getclasscomics'
    }
    response = requests.post(LIST_API, data=data)
    # print(response.json())
    ret = response.json()['UpdateComicItems']
    comics_list = []
    for i in ret:
        item = {}
        item['Title'] = i['Title']
        item['Url'] = HOST + '/' + i['UrlKey']
        item['Author'] = i['Author'][0]
        item['ShowLastPartName'] = i['ShowLastPartName']
        item['LastUpdateTime'] = i['LastUpdateTime']
        item['ShowReads'] = i['ShowReads']
        # yield item
        comics_list.append(item)
    print('漫画列表获取完成！')
    return comics_list


def save_comics_list(comics_list):
    with open('漫画/漫画列表.json', 'w', encoding='utf-8') as f:
        for i in comics_list:
            f.write(json.dumps(i, indent=2, ensure_ascii=False))


def download_comics(comics_list) -> None:

    for i in comics_list:
        comics_url = i['Url']
        comics_name = safe_str(i['Title'])

        # 获取章节链接列表
        chapter_list = get_chapter(comics_name, comics_url)

        if chapter_list:  # 章节不为空
            # 创建漫画名文件夹
            # 1级目录存放漫画名，2级目录存放章节名，3级目录存放章节图片
            path_1 = os.sep.join(['漫画', comics_name])
            if not os.path.exists(path_1):
                os.makedirs(path_1)
            print(f'创建文件夹<{comics_name}>成功！')

            # 保存章节
            for j in chapter_list:
                chapter_name = j['chapter_name']
                chapter_url = j['chapter_url']

                path_2 = os.sep.join([path_1, chapter_name])
                if not os.path.exists(path_2):  # 创建2级目录存放章节
                    os.makedirs(path_2)
                print(f'创建文件夹<{chapter_name}>成功！')

                # 下载章节
                download_chapter(chapter_name, chapter_url, path_2)


def safe_str(_str):
    return re.sub(r'[ ,!~*\?&$！？，：￥]', '_', _str)


def get_chapter(comics_name, comics_url):
    response = requests.get(comics_url)
    text = response.text
    sel = parsel.Selector(text=text)
    lis = sel.css('ul.view-win-list.detail-list-select li')  # 漫画可能因某些原因详情页没有章节
    if not lis:
        print(f'<{comics_name}>章节调整中，链接:{comics_url}')
        return

    chapter_list = []
    for li in lis:
        chapter_item = {}
        name_text = li.xpath('./a/text()').getall()  # 可能含有大量空格
        chapter_item['chapter_name'] = re.sub(' ', '', ''.join(name_text))
        chapter_item['chapter_url'] = HOST + li.xpath('./a/@href').get()
        print('正在获取章节<%s>' % (chapter_item['chapter_name']))
        chapter_list.append(chapter_item)
    print(f'<{comics_name}>章节列表获取完成！')
    return chapter_list
    # yield {
    #     'chapter_url':chapter_url,
    #     'chapter_name':chapter_name
    # }


def download_chapter(chapter_name, chapter_url, path):
    try:
        r = requests.get(chapter_url, headers=headers)
    except Exception as e:
        print(f'章节<{chapter_name}>下载失败:{e}')
        return None
    ret = parsel.Selector(text=r.text)
    div1 = ret.css('div#barChapter')  # 一页一章
    div2 = ret.css('div#cp_img')  # 多页一章
    if div1:
        # 如果章节不分页，直接从源码获取章节图片集
        # 下载图片超时（把链接打开提示“请到官网浏览”），出现反爬
        # print('一页一章情况')
        # return
        # 注意源码中src是空，数据在data_src属性中
        imgs = div1.xpath('./img/@data-src').getall()
        for img in imgs:
            img_url = img
            img_name = urlparse(img).path.split('/')[-1]
            print(f'下载{chapter_name}<{img_name}>...')
            download_img(img_name, img_url, path)

    if div2:
        # 如果章节分页，通过api下载
        cid = re.search('DM5_CID=(.*?);', r.text).group(1)
        img_count = re.findall('DM5_IMAGE_COUNT=(.*?);', r.text)[0]
        mid = re.findall('DM5_MID=(.*?)', r.text)[0]
        dt = re.findall('DM5_VIEWSIGN_DT="(.*?)"', r.text)[0]
        sign = re.findall('DM5_VIEWSIGN="(.*?)"', r.text)[0]
        img_page = 1
        while img_page <= int(img_count):
            params = {
                'cid': cid,
                'page': img_page,
                'key': None,
                'language': 1,
                'gtk': 6,
                '_cid': cid,
                '_mid': mid,
                '_dt': dt,
                '_sign': sign
            }
            js_api = JS_API + urlencode(params)
            ret = requests.get(js_api, headers=headers)
            img_list = execjs.eval(ret)
            img_url = img_list[0]
            img_name = urlparse(img_url).path.split('/')[-1]
            print(f'下载{chapter_name}<{img_name}>...')
            download_img(img_name, img_url, path)
            img_page += 1


def download_img(img_name, img_url, path):
    try:
        r = requests.get(img_url, headers=headers)
    except Exception as e:
        print(f'图片<{img_name}下载失败>：{e}')
        return None
    img_path = os.sep.join([path, img_name])
    with open(img_path, 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    page = 1
    comics_list = get_comics_list(page)
    save_comics_list(comics_list)
    download_comics(comics_list)
