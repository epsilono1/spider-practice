'''cookie_str源于浏览器
测试：cookie放在session，session请求
结果：200，正确结果，并且成功率高
注：附加实现 cookie_str 转为 dict
'''
import requests
s = requests.Session()
cookie_str = 't=0788cbca9ac1808eb5410bb233084581; thw=cn; enc=bhz9mE71cTcFH7ZmesmIdWqPKXjuiGIei4rTBPRqn%2B7zLZW0ifGWcHpAkLzQ2OyG7c6ZuvIVTeQVhdsoElNF0Q%3D%3D; tracknick=; cna=anodGCkKKRUCARsm9WDzld0/; xlly_s=1; JSESSIONID=8347B7E9D1898FC1F7D37D184A37A7F6; tfstk=cLKfBwgHsSVXnu3a0KMP38hNDksGZ5r5EufyhEp7TYwon_9fiYrFOZ6ch7ZRJT1..; l=eBLoZMorOAXr5ajzBOfwourza77OSIRAguPzaNbMiOCP_05e5QChWZSBQSTwC3GVh6z2R38oqoz_BeYBqIv4n5U62j-la_kmn; isg=BF9fYcxVfLvKhHicSeMndCWS7rPpxLNmR8jmDPGs-45VgH8C-ZRDtt1SQhD-GIve'
for single in cookie_str.split(';'):
    cookie = {}
    key, value = single.split('=', 1)
    cookie[key] = value
    s.cookies.update(cookie)
    
url = 'http://s.taobao.com/search?q=书包&s=0'
headers = {'user-agent':'Mozilla/5.0'}
try:
    r = s.get(url, headers=headers, timeout=5)
    print(r.status_code)
    r.raise_for_status
    print(r.text[:1000])
except Exception as e:
    print(f'爬取失败！{e}')


