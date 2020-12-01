# coding:utf-8
import requests

url = 'https://item.jd.com/12585508.html'
# headers = {'user-agent': 'Mozilla/5'}
try:
    r = requests.get(url,headers=headers)
    print(r.status_code)
    print(r.encoding)
    print(r.text[:1000])
except Exception as e:
    print(f'爬取错误！{e}')
    
'''响应
200
UTF-8
<script>window.location.href='https://passport.jd.com/uc/login?ReturnUrl=http%3A
%2F%2Fitem.jd.com%2F12585508.html'</script>

响应码正常，可能是headers问题
尝试添加UA，响应就正常了
'''