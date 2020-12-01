#coding:utf-8
#python3.7.4
import requests
import execjs

# iframe_url = 'https://www.iqiyi.com/iframe/loginreg'
stoken_url = 'https://passport.iqiyi.com/apis/qrcode/gen_login_token.action'
login_url = 'https://passport.iqiyi.com/apis/reglogin/login.action'
userinfodetail_url = 'https://pcw-api.iqiyi.com/passport/user/userinfodetail'

HEADERS = {
    'Referer': 'https://www.iqiyi.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'

}

headers = {
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-site',
    'Host': 'passport.iqiyi.com',
    'Origin': 'https://www.iqiyi.com',
    'Referer': 'https://www.iqiyi.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
email = 'xxxx'
pwd = '****'

#获取密码加密str
with open('getPwd.js', 'r') as f:
    js_text = f.read()
passwd = execjs.compile(js_text).call('getpwd', pwd)
print(passwd)



post_data = {
    'email': email,
    'fromSDK': 1,
    'sdk_version': '1.0.0',
    'passwd': passwd,
    'agenttype': 1,
    '__NEW': 1,
    'checkExist': 1,
    'lang': None,
    'ptid': '01010021010000000000',
    'nr': 2,
    'verifyPhone': 1,
    'dfp': 'a15553fa59a9d447a7b497ad073162d5d0040335bc1545d3cfbc67afabfd64d92d'
}

session = requests.Session()
r = session.post(login_url, headers=headers)
# userinfo = session.get(userinfodetail_url, headers=HEADERS)

print(r.json())

