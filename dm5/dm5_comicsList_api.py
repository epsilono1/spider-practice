#coding:utf-8
'''
2020年10月11日 
本来源代码可以找到数据，然后解析一波完事，但抓包突然发现有api返回json数据，然后贪便宜走近道api，可是
第二页返回空，我觉得被反爬玩弄了
update：2020年10月12日 
昨天api出不来正确数据，是因为把form的char参数弄成了0，而实际上应该设置为None，注意0不等于None。
优化了一下，api的参数时间戳可以去掉，并且api请求不需要headers
'''
import requests
import json

LIST_API = 'http://www.dm5.com/dm5.ashx?' #t=1602438143000参数去掉
HOST = 'http://www.dm5.com' #用于衔接漫画短链接

def parse_page(page):
    data = {
        'pagesize':68,
        'pageindex':page,
        'tagid':0,
        'areaid':0,
        'status':0,
        'usergroup':0,
        'pay':-1,
        'char':None, #注意网页上这个参数啥都没有，不要写成0，不然得到错误数据
        'sort':10,
        'action':'getclasscomics'
    }
    r = requests.post(LIST_API,data=data)  
    ret = r.json()['UpdateComicItems']
    comics_list = []
    for i in ret:
        item = {}
        item['title'] = i['Title']
        item['Author'] = i['Author'][0]
        item['Url'] = HOST + i['UrlKey']
        item['ShowLastPartName'] = i['ShowLastPartName'] #最新话
        item['LastUpdateTime'] = i['LastUpdateTime'] #更新时间
        item['ShowReads'] = i['ShowReads'] #阅览量
        comics_list.append(item)
    return comics_list

def sav_data(comics_list):
    with open('list0.json','a',encoding='utf-8') as f:
        f.write(json.dumps(comics_list,indent=2, ensure_ascii=False))

if __name__ == "__main__":
    for i in range(1,11): #爬取前10页热门漫画
        print('*'*5 + f'第{i}页' + '*'*5)
        comics_list = parse_page(i)
        sav_data(comics_list)
