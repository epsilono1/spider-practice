
import requests

url = 'https://pcw-api.iqiyi.com/passport/user/userinfodetail'

headers = {
    'Referer': 'https://www.iqiyi.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

r = requests.get(url,headers=headers)
print(r.text)








