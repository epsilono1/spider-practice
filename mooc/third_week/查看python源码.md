查看函数源码的方法

- 1. help()方法在idle中查看，看FILE路径,没有FILE，继续help()
    ```python
    >>> import requests
    >>> help(requests.cookies.RequestsCookieJar)
    Squeezed text(266 lines)
    '''
    Help on class RequestsCookieJar in module requests.cookies:
    ...没有FILE，继续help()
    '''
    >>> help(requests.cookies)
    '''
    Help on module requests.cookies in requests:

    NAME
        requests.cookies
    ...
    FILE
        d:\program files\python37\lib\site-packages\requests\cookies.py
    '''
    ```
  
- 2. 在pycharm中查看，``CTRL + 查看函数`` pycharm会自动打开函数源码

- 3. inspect获取源码文件路径
    ```python
    >>> import inspect
    >>> inspect.getsourcefile(requests.cookies.RequestsCookieJar)
    'D:\\Program Files\\Python37\\lib\\site-packages\\requests\\cookies.py'
    ```









