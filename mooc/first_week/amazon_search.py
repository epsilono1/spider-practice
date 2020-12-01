# coding:utf-8
import requests

url = 'https://www.amazon.cn/s?'
params = {'k':'python'}
headers = {
    'Cookie': 'session-id=459-6174462-7711802; i18n-prefs=CNY; ubid-acbcn=461-7051870-8991536; session-token=ZQae4QrOn0WX3kVnTI1qwQNk7RWxWIyW4FY9ngswK5yTTcuWVq4Uod04pvCTjve42nJNIS5mT+Vau96PCLQO9031HDhkL0NyoYbwL3H+ubpcnm7+RVHr7gXDLPSeRgoDXG74UiKDjROlUIog6hgDo2/t07QYPiEeVYIi13b0D9UECpPNGx93RUjYmWO7l9FZ; session-id-time=2082729601l; csm-hit=tb:8DBW2951B6N050Q6QR9H+s-QJ85P13QJN0SW151NWBT|1605170677742&t:1605170677743&adb:adblk_yes',
    'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(len(r.text))
    print(r.text[128000:130000])
except Exception as e:
    print(f'爬取错误！{e}')
    
    
'''结果
503
ISO-8859-1
<!DOCTYPE html>
<!--[if lt IE 7]> <html...

503错误，并且编码异常
添加UA，响应码正常。但有时候会出现字符验证，最后添加cookie解决
r.apparent_encoding：从响应中分析的编码
r.encoding：从HTTP header中猜测的编码
'''