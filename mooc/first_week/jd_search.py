# coding:utf-8
import requests

param = {'keyword': 'python爬虫'}
url = 'https://search.jd.com/Search?'
headers = {'user-agent': 'Mozilla/5.0'}
try:
    r = requests.get(url, params=param, headers=headers)
    print(r.status_code)
    print(r.encoding)
    print(r.text[500:1500])
except Exception as e:
    print(f'爬取错误！{e}')
    
'''运行结果
200
UTF-8
<script>window.location.href='https://passport.jd.com/uc/login'</script>

添加UA后返回结果正常

'''