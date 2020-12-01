'''cookie_str源于浏览器
测试：cookie放在请求头
结果：200,正确结果，成功率次于session
注：附 cookie_str 转为 CookieJar
'''
import requests
cookie_str = 't=0788cbca9ac1808eb5410bb233084581; thw=cn; enc=bhz9mE71cTcFH7ZmesmIdWqPKXjuiGIei4rTBPRqn%2B7zLZW0ifGWcHpAkLzQ2OyG7c6ZuvIVTeQVhdsoElNF0Q%3D%3D; tracknick=; cna=anodGCkKKRUCARsm9WDzld0/; xlly_s=1; JSESSIONID=8347B7E9D1898FC1F7D37D184A37A7F6; tfstk=cLKfBwgHsSVXnu3a0KMP38hNDksGZ5r5EufyhEp7TYwon_9fiYrFOZ6ch7ZRJT1..; l=eBLoZMorOAXr5ajzBOfwourza77OSIRAguPzaNbMiOCP_05e5QChWZSBQSTwC3GVh6z2R38oqoz_BeYBqIv4n5U62j-la_kmn; isg=BF9fYcxVfLvKhHicSeMndCWS7rPpxLNmR8jmDPGs-45VgH8C-ZRDtt1SQhD-GIve'
jar = requests.cookies.RequestsCookieJar()
for single in cookie_str.split(';'):
    key, value = single.split('=', 1)
    jar.set(key,value)
    
url = 'http://s.taobao.com/search?q=书包&s=0'
headers = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url, headers=headers, cookies=jar, timeout=5)
    print(r.status_code)
    r.raise_for_status()
    print(r.text[:1000])
except Exception as e:
    print(f'爬取失败！{e}')
