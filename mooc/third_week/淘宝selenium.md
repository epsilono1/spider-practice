## selenium登陆淘宝

#### 1. 忽略证书错误和ssl错误

options操作：

```python
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') #忽略证书错误和ssl错误
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
```

#### 2.手机号验证码输入(切换 iframe)

```python
iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-check-left iframe')))
driver.switch_to_frame(iframe)
```

操作完后切换回默认 `driver.switch_to.default_content()`

#### 3.cookie处理

cookies转化为字符串，方便以后放到headers中使用。

先从列表字典元素中提取name和value键值，组成新的列表元素，再将列表转为str。

```python
cookies = driver.get_cookies()
cookie = [item['name'] + '=' + item['value'] for item in cookies]
cookie_str = ';'.join(cookie)
```

#### 4.用cookie登陆

4.1 headers只用cookie+ua+host不行，还加 accept + accept-Language+accept-Encoding+Connection

4.2 运行报错 `requests.exceptions.TooManyRedirects: Exceeded 30 redirects.`

原因：网页发生了重定向。 （重定向到登录页）

分析：在get ()方法中添加 `allow_redirects=False` ,可以看到返回的响应码是302，即发生了重定向。也可以通过 `new_url = response.headers['Location']` 查看重定向网址。查看重定向网址发现，网页重定向到登录页去了。

4.3  响应码200，但正则提取不到script中数据

方案：加载js代码来解决，检查测试正则是否正确

