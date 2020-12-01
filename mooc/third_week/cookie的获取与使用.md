cookie的获取及使用

1. 从浏览器复制（手动），得到cookie_str
    
    获取：
    
    - F12+刷新
    - F12+console（document.cookie）
    
    使用：
    
    - 直接放入headers或 cookies
    
        ```python
        # 放入headers
        headers = {'cookie':'ll="118282"; bid=4jNicp0_6a0'}
        # 放入cookies
        cookies = {'cookie':'ll="118282"; bid=4jNicp0_6a0'}
        ```
    
    - 转为cookieJar，放入get （好像没必要）
      
        ```python
        import requests
        cookie_str = 't=0788cbca9ac1808eb5410bb233084581; thw=cn'
        jar = requests.cookies.RequestsCookieJar()
        for cookie in cookie_str.split(';'):
            key, value = cookie.split('=', 1)
            jar.set(key,value)
        r = requests.get(url, cookies=jar)
        ```
        
    - 转为dict，存入session或get
      
        ```python
        import requests
        session = requests.Session()
        cookie_str = 't=0788cbca9ac1808eb5410bb233084581; thw=cn'
        cookie = {}
        for single in cookie_str.split(';'):
            k, v = single.split('=',1)
            cookie[k] = v
        session.cookies.update(cookie)
        ```
    
2. selenium获取，得到 cookie_dict，再筛选
    - 获取
      
```python
        cookie_list = driver.get_cookies()
```

    - 转为可用格式dict
        
        ```python
    # 法1
        cookies = {item['name']:item['value'] for item in cookie_list}
        # 法2
        cookies = {}
        for cookie in cookie_list:
            cookies[cookie['name']] = cookie['value']
        ```

3. requests获取，得到 RequestsCookieJar，使用直接在get(cookies=jar)即可。
    另可通过dict([(cookie.name,cookie.value)])转为字典
    
    - 获取
      
        ```python
        r = requests.get(url,headers=headers)
        cookie_jar = r.cookies
        ```
    
    - 转化为dict （遍历cookieJar可先用items()方法将其转为元组组成的list再遍历）：
      
        ```python
        cookie = {}
        for key, value in cookie_jar.items():
            cookie[key] = value
        ```
    
4. urllib获取，得到CookieJar，使用直接在get(cookies=jar)即可。
    可通过dict([(cookie.name,cookie.value)])转为字典
    - 获取
      
        ```python
        from urllib import request
        from http import cookiejar
        cookie = cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
    response = opener.open('http://baidu.com')
        cookie_jar = cookie
        ```
        
    - 转化同requests
    
        

- cookie使用问题

  get()方法中，cookies=cookies，这个cookies可以是cookie_jar，也可以是dict









