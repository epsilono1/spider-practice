#爬取一个知乎问题下所有答案2020/6/1
#目的：熟悉Ajax加载模式的爬取，熟悉MongoDB的操作，熟悉多线程爬取
#问题1：爬出来的数据重复率很高，为什么?
#答：因为运行了多次脚本,新抓取的数据被添加进去末尾
#问题2：开进程池死机？
#答：


import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
# from multiprocessing.pool import Pool

client = MongoClient('mongodb://localhost:27017/') #MongoClient(host='localhost',port=27017)
db = client['zhihu']
collection = db['answerer']

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
base_url = 'https://www.zhihu.com/api/v4/questions/386437349/answers?'

def get_page(offset):
    params = {
        'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
        'limit':5,
        'offset':offset,
        'platform':'desktop',
        'sort_by':'default'
    }
    url = ''.join([base_url, urlencode(params)])
    r = requests.get(url, headers = headers)
    return r.json()

def parse_page(jsonData):
    if jsonData.get('data'):
        for item in jsonData.get('data'):
            answer = {}
            answer['name'] = item.get('author').get('name')
            answer['gender'] = item.get('author').get('gender')
            answer['voteup'] = item.get('voteup_count')
            answer['comment'] =item.get('comment_count')
            yield answer

def save_to_mongo(result):
    collection.insert_one(result)

def main(offset):
    jsonDoc = get_page(offset)
    answers = parse_page(jsonDoc)
    for answer in answers:
        save_to_mongo(answer)
            
if __name__ == '__main__':
    #获取总页数来求offset最大值
    url = 'https://www.zhihu.com/api/v4/questions/386437349/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default'
    resp = requests.get(url, headers = headers)
    total = resp.json().get('paging').get('totals')  
    page = total//5 if total%5==0 else total//5+1
    offset_last = (page-1)*5
    print('total:%s, page:%s, offset_last:%s'%(total,page,offset_last))
    for i in range(page):
        result = get_page(i*5)
        answers = parse_page(result)
        for answer in answers:
            print(answer)
            save_to_mongo(answer)
    #使用进程池
#     GROUP_START = 0
#     GROUP_END = page-1
#     pool = Pool()
#     groups = ([x*5 for x in range(GROUP_START,GROUP_END+1)])
#     pool.map(main,groups)
#     pool.close()
#     pool.join()