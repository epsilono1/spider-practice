#爬豆瓣电影TOP250 https://movie.douban.com/top250的第一页，其他页可据此完善
#title,score,people
#提取导演，演员，上映时间等数据差点吐了，问题1是定位到多个相同标签中的某一个，问题2是提取到文本中有换行符和拉丁空格符

import requests
from pyquery import PyQuery as pq

url = 'https://movie.douban.com/top250'
headers = {'user-agent':'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'}
html = requests.get(url,headers=headers).text 
#没有加headers返回418 I'm a teapot,表示服务器拒绝煮咖啡，因为它是一个茶壶.可能被反爬程序识别了，所以加上headers的user-agent,请求成功！
doc = pq(html)
items = doc('.item').items() #items()方法进行遍历
for item in items:   
    title = item.find('.title').text()
    director = item.find('.bd p').eq(0).text().split('\n')[0].split('\xa0')[0] #\xa0是一种特殊拉丁空格
    actors = item.find('.bd p').eq(0).text().split('\n')[0].split('\xa0')[-1]
    time = item.find('.bd p').eq(0).text().split('\n')[1].split('/')[0].strip()
    position = item.find('.bd p').eq(0).text().split('\n')[1].split('/')[1].strip()
    sorts = item.find('.bd p').eq(0).text().split('\n')[1].split('/')[2].strip()
#     print('\n'.join([title,director,actors]))  #影名，导演，演员
#     print(' '.join([time,position,sorts]))     #上映时间，地点，类型
    score = item.find('.rating_num').text()
    people = item.find('.star span').eq(-1).text() #多个span标签取最后一个标签的文本
    print('\n'.join([title,time,score,people]))        #评分，人数
    
