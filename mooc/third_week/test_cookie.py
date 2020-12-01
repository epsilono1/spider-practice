# from selenium import webdriver
 
# driver=webdriver.Chrome()
# url="http://baidu.com"
# driver.get(url)
# cookie_list=driver.get_cookies()
# cookies = {item['name']:item['value'] for item in cookie_list}
# print(cookies)
# cookie_dict = {}
# for cookie in cookie_list:    
    # cookie_dict[cookie['name']]=cookie['value']   
# print(cookie_dict)
'''使用
requests.get(cookies=cookies)

'''
    
import requests
url="http://douban.com"
headers={'user-agent':'Mozilla/5.0'}
headers={
    # 'cookie':'ll="118282"; bid=4jNicp0_6a0; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; dbcl2="81004991:5pRhjXAJjSM"; ck=rioB',
    'user-agent':'Mozilla/5.0'
}
# cookies = {'cookie':'ll="118282"; bid=4jNicp0_6a0; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; dbcl2="81004991:5pRhjXAJjSM"; ck=rioB'}
    
r = requests.get(url,headers=headers,timeout=5)
r.raise_for_status()
print(r.text[:1000])
cookie = {}
for k,v in r.cookies.items():
    cookie[k] = v
print(cookie)


# from urllib import request
# from http import cookiejar
# cookie = cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://baidu.com')
# print(cookie)
# for item in cookie:
    # print(dict([(item.name,item.value)]))
    





















