# coding:utf-8
import requests

url = 'https://www.amazon.cn/dp/B07VBL72CB/'
headers = {
    # 'Cookie': 'session-id=459-6174462-7711802; i18n-prefs=CNY; ubid-acbcn=461-7051870-8991536; session-token=ZQae4QrOn0WX3kVnTI1qwQNk7RWxWIyW4FY9ngswK5yTTcuWVq4Uod04pvCTjve42nJNIS5mT+Vau96PCLQO9031HDhkL0NyoYbwL3H+ubpcnm7+RVHr7gXDLPSeRgoDXG74UiKDjROlUIog6hgDo2/t07QYPiEeVYIi13b0D9UECpPNGx93RUjYmWO7l9FZ; csm-hit=tb:8DBW2951B6N050Q6QR9H+s-4JJABKDSXSVWXN3F5CKA|1605173412341&t:1605173412341&adb:adblk_yes; session-id-time=2082729601l',
    'user-agent':'Mozilla/5.0'
}
try:
    r = requests.get(url, headers=headers)
    # r.raise_for_status()
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text[54000:55000])
except Exception as e:
    print(f'爬取失败！{e}')
    
'''结果(无header)
503
...
<h4>请输入您在下方看到的字符</h4>
<p class="a-last">抱歉，我们只是想确认一下当前访问者并非自动程序
。为了达到最佳效果，请确保您浏览器上的 Cookie 已启用。</p>

503错误，并且编码异常
添加UA和cookie才能正常爬取，只有UA则响应码200但内容不对

'''