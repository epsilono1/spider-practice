# coding:utf-8
# 2020-10-27
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import json

email='xxx' #email = input('会员名/邮箱/手机号：')
pwd = 'xxx' #pwd = input('密码：')

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') #忽略证书错误和ssl错误
options.add_argument('--ignore-ssl-errors')
#无图模式
options.add_experimental_option('prefs',{'profile.managed_default_content_settings.images':2})

driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window() #最大化窗口
wait = WebDriverWait(driver, 10)

index = 'https://login.taobao.com/member/login.jhtml'
driver.get(index)

#获取用户名密码输入框，并输入,输入后等待1s
name = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
name.send_keys(email)

passwd = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
passwd.send_keys(pwd)
time.sleep(1)
#获取登陆按钮并点击，然后等待跳转1s
lg_btn =wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fm-btn button'))) 
lg_btn.click()
time.sleep(1)

#登陆没成功，遇到手机号验证
if '身份验证' in driver.title:
    #切换iframe
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-check-left iframe')))
    driver.switch_to_frame(iframe)
    #获取手机验证码
    phone_cpt_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkcode-warp button')))
    phone_cpt_button.click()
    #输入验证码
    while True:
        phone_cpt = input("手机验证码：")
        phone_cpt_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.checkcode-warp #J_Phone_Checkcode')))
        phone_cpt_input.send_keys(phone_cpt)
        if phone_cpt:
            break
    #确认提交手机验证码，并等待加载1s
    submit = wait.until(EC.element_to_be_clickable((By.ID, 'submitBtn')))
    submit.click()
    time.sleep(1)
    driver.switch_to.default_content() 

#验证登陆成功（获取用户呢称）
user_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.site-nav-user a')))
print(user_name.text + '---登陆成功！')

cookies = driver.get_cookies()
# print(type(cookies))
# print(cookies)
#关闭浏览器
time.sleep(3)
driver.quit()

#cookies转化为字符串，方便以后放到headers中使用
#先从列表字典元素中提取name和value键值，组成新的列表元素，再将列表转为str
cookie = [item['name'] + '=' + item['value'] for item in cookies]
cookie_str = ';'.join(cookie)
#保存
with open('cookie.txt','w',encoding='utf-8') as f:
    f.write(cookie_str)
    print('cookie保存成功！')

