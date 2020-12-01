'''爬boss直聘python爬虫相关岗位'''

import requests
from lxml import etree
import re
import pandas as pd


HEADERS = {
        'cookie':'lastCity=101280600; __g=-; t=Whf55ew7rhI1xFQs; wt=Whf55ew7rhI1xFQs; wt2=Whf55ew7rhI1xFQs; _bl_uid=htk0wi6s5O5d24bbqjwvcha9e7R2; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Frecommend&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __c=1606787665; __a=66333625.1606787665..1606787665.37.1.37.37; __zp_stoken__=5553bGmZEGURLbigncDw%2FJHEVa2l4I3A5TV4bKjc4GkNmVixpVjxwcAAPAGV%2FVDx0AkcJd2U1RyQcF0AdekRSBhxkc18SZ1MJRhUAfFpUQWp2Ung6MFIfQnQjNRYLIhMIBBYDZFdOHFs3bwl%2BdA%3D%3D',
        'user-agent':'Mozilla/5.0'
        }
HOST = 'https://www.zhipin.com'
BASE_URL = 'https://www.zhipin.com/c101280600/?query=python%E7%88%AC%E8%99%AB&page={}&ka=page-{}'
JOB_DESCPT = 'https://www.zhipin.com/wapi/zpgeek/view/job/card.json?'


def get_page(job_url, page):
    
    try:
        r = requests.get(job_url, headers=HEADERS, timeout=3)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(f'{page}页请求出错！',e.args)
        return None
    
def parse_page(html):
    sel = etree.HTML(html)
    lis = sel.xpath('//div[@class="job-list"]/ul/li')
    item = []
    for li in lis:
        jid = li.xpath('./div/div[1]/div[1]/div/@data-jid')[0]
        lid = li.xpath('./div/div[1]/div[1]/div/@data-lid')[0]
        # print('jid:',jid)
        # print('lid:',lid)
        
        
        title = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/text()')[0]
        area = li.xpath('./div/div[1]/div[1]/div/div[1]/span[2]/span/text()')[0]
        pub_time = li.xpath('./div/div[1]/div[1]/div/div[1]/span[3]/text()')[0]
        
        salary = li.xpath('./div/div[1]/div[1]/div/div[2]/span/text()')[0]
        work_year = li.xpath('./div/div[1]/div[1]/div/div[2]/p/text()')[0]
        edu = li.xpath('./div/div[1]/div[1]/div/div[2]/p/text()')[1]
        
        company = li.xpath('./div/div[1]/div[2]/div/h3/a/text()')[0]
        industry = li.xpath('./div/div[1]/div[2]/div/p/a/text()')[0]
        scale = li.xpath('./div/div[1]/div[2]/div/p/text()')[-1]
           
        tags = li.xpath('.//div[@class="tags"]/span/text()')
        tags = '，'.join(tags)
        
        job_descpt = get_job_descpt(JOB_DESCPT, jid, lid)
        
        item.append({
            'title':title,
            'area':area,
            'pub_time':pub_time,
            'salary':salary,
            'work_year':work_year,
            'edu':edu,
            'company':company,
            'industry':industry,
            'scale':scale,
            'tags':tags,
            'description':job_descpt
        })
        
    next_class = sel.xpath('//a[@ka="page-next"]/@class')[0]
    if next_class == 'next':
        next_url = HOST + sel.xpath('//a[@ka="page-next"]/@href')[0]
    else:
        next_url = None
    return next_url,item
    
    
def get_job_descpt(job_descpt_url,jid,lid):
    params = {
        'jid':jid,
        'lid':lid,
        'type':3
    }
    headers={'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(job_descpt_url,params=params,headers=headers,timeout=3)
        r.raise_for_status()
        if r.json().get('message') == 'Success':
            info = re.findall(r'detail-bottom-text\">(.*?)</div',r.json().get('zpData').get('html'),re.S)
            job_descpt = info[0].strip().replace('<br/>','\n')
            return job_descpt
    except Exception as e:
        # print(f'获取描述失败{e.args}')
        return None
        
        
def save(job_list,page):
    df = pd.DataFrame(job_list)
    if page == 1:
        df.to_csv('./job.csv',index=False, header=True, 
                    mode='a',encoding='utf-8')
    else:
        df.to_csv('./job.csv',index=False, header=False, 
                    mode='a',encoding='utf-8')
        
    
def main():
    page = 1
    next = BASE_URL.format(str(page),str(page))
    while next:
        html = get_page(next, page)
        if html:
            next, job_list = parse_page(html)
            page = next.split('=')[-1]
            save(job_list,page)
            print(f'保存第{page}页成功！')
            continue
        print(f'爬取{page}页失败！')
    print('爬取完成！')
        
    
if __name__ == '__main__':
    main()
