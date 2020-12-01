#coding:utf-8
import execjs

pwd = '298723'
with open('getPwd.js', 'r') as f:
    js_text = f.read()
passwd = execjs.compile(js_text).call('getpwd', pwd)
print(type(passwd))
print(passwd)