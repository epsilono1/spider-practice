#coding:utf-8
#传统方法解析漫画列表
import requests
import parsel

base_url = 'http://www.dm5.com/manhua-list-p{}/'
HOST = 'http://www.dm5.com'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

def parse_page(url):
    r = requests.get(url, headers=HEADERS)
    print(r.status_code)
    sel = parsel.Selector(r.text)
    lis = sel.css('ul.mh-list.col7 li')
    item =[]
    for li in lis:
        title = li.css('div.mh-item-detali h2 a::text').get()
        link = HOST + li.css('div.mh-item-detali h2 a').attrib['href']
        update = li.css('div.mh-item-detali p.chapter a::text').get()
        author = li.css('div.mh-item-tip-detali p.author span a::text').get()
        item.append('\n'.join([title,link,update,author]))

    return item

def save_list(data):
    with open('list.txt', 'a',encoding='utf-8') as f:
        for i in data:
            f.write(i)
    
if __name__ == "__main__":
    for i in range(1,10): #9页热门
        print('='*5 + f"第{i}页"+ "="*5)
        url = base_url.format(str(i))
        item = parse_page(url)
        save_list(item)
