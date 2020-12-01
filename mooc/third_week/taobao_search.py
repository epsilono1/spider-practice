# coding:utf-8
'''爬取淘宝搜索页商品信息'''

import requests
import re

cookie_str = '_samesite_flag_=true; cookie2=199a2256f829aaf5effcc3fe76fd38b6; t=6f73da8a5fc1f7ced02ee204d42efa46; _tb_token_=efeebe135b14f; xlly_s=1; enc=ZRab5KWqhvt6YIPQiAq13n68b6nQRAaMhlHeEpt1cvL3zrNDFoTvLmF2HXSd%2B7JW4TYCaAzKmWQbXGOmCJ%2B7xg%3D%3D; thw=cn; mt=ci=0_0; tracknick=; JSESSIONID=C15B45565518D1C51DA827D1E3C7AD42; cna=smA2GE28BW8CARsm/W9SzBwP; isg=BK-vcis1LIn4Xii1w8bp1g90PsO5VAN20bFj8cE8S54lEM8SySSTxq3ClgAuc9vu; l=eBTcK5_IOkqCSiPEBOfanurza77OSIRYYuPzaNbMiOCPO_CB53DPWZSHQfY6C3GVh649R3ujXzbpBeYBqQAonxv92j-la_kmn; tfstk=c4u5B9tiKTX5up-FzbO4aIeC4Qadw6_biZ2qN0UsQ0Y3wR1c_Ny_V7V5hZETG'
headers = {'user-agent':'Mozilla/5.0'}
session = requests.Session()

def get_session_cookie(cookie_str):
    cookie = {}
    for single in cookie_str.split(';'):
        key, value = single.split('=',1)
        cookie[key] = value
    session.cookies.update(cookie)

def get_html(url, page):
    try:
        r = session.get(url, headers=headers, timeout=5)
        r.raise_for_status
        return r.text
    except:
        print(f'第{page+1}页爬取失败！')
        return ''
    
def parse_page(html):
    pattern = re.compile(r'"raw_title":"(.*?)".*?'
                        r'"view_price":"(.*?)".*?'
                        r'"item_loc":"(.*?)".*?'
                        r'"view_sales":"(.*?)"')
    goods = re.findall(pattern, html)
    for good in goods:
        yield {
            'title':good[0],
            'price':good[1],
            'shop_loc':good[2],
            'sales':good[3]
        }
        
    
def main():
    kw = '书包'
    base_url = 'http://s.taobao.com/search?q=' + kw
    pages = 2
    for page in range(pages):
        url = base_url + '&s=' + str(page*44)
        get_session_cookie(cookie_str)
        html = get_html(url, page)
        goods = parse_page(html)
        #打印前每页三件商品信息看数据
        for good in list(goods)[:3]:
            print(good)
            
    
if __name__ == '__main__':
    main()