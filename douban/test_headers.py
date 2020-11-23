import requests

s = requests.Session()
HEADERS = {'user-agent': 'Mozilla/5.0'}


def headers_update():
    print(s.headers)  # python-requests/2.20.0
    s.headers.update(HEADERS)
    print(s.headers)  # Mozilla
    headers = {'referer': 'http://baidu.com'}
    s.headers.update(headers)
    print(s.headers)  # Mozilla + referer，并没有覆盖ua
    headers = {'referer': 'http://httpbin.org'}
    s.headers.update(headers)
    print(s.headers)  # Mozilla + referer,修改了referer


headers_update()

HEADERS.update({'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64)'})
s.headers.update(HEADERS)
print(s.headers)  # ua(后者) + referer(最后更改)

# 删除headers中的referer，其他不变（比如requests默认的Accept,Connection）
del s.headers['referer']
print(s.headers)

s.headers = HEADERS
print(s.headers)  # 清空了所有（包括requests默认的Accept,Connection），只剩UA
