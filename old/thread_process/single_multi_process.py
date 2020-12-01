# -*- coding: utf-8 -*-

'''
项目：单进程、多进程耗时测试
Author: epsilono1
Date: 2020年9月16日 16:36:24 
'''

import time
import os
from multiprocessing import Process, Pool, cpu_count

def long_time_task():  #计算8^20
    print('当前进程：{}'.format(os.getpid()))
    time.sleep(2)
    print('计算结果：{}'.format(8**20))

def single_process():
    start = time.time()
    for i in range(2): #计算2次
        long_time_task()
        
    end = time.time()
    print('单进程耗时 {} 秒'.format(end-start))
    

def long_time_task_mltp(i): #计算1次8^20
    print('子进程：{} - 任务{}'.format(os.getpid(),i))
    time.sleep(2)
    print('计算结果：{}'.format(8**20)) 
    
'''
多进程multiprocess.Process实现
'''    
def multi_process():
    start = time.time()
    
    p1 = Process(target=long_time_task_mltp, args=(1,))
    p2 = Process(target=long_time_task_mltp, args=(2,))
    print('等待所有子进程完成...')
    p1.start()
    p2.start()
    p1.join()  
    p2.join()
    
    end = time.time()
    print('多进程耗时 {} 秒'.format(end-start))
    
'''
多进程multiprocessing.Pool实现  
5个计算任务，每个任务大约耗时2秒，多进程只耗时4.63秒，耗时减少53% 
'''
def multi_pool():
    count = cpu_count()
    print('CPU内核数：{}'.format(count))
    start = time.time()
    p = Pool(count)
    for i in range(count+1):
        p.apply_async(long_time_task_mltp, args=(i,))
    
    print('等待所有子进程完成...')
    p.close()
    p.join() #join方法阻塞主进程等待子进程退出，要在close或terminate之后使用
    end = time.time()
    print('多进程耗时：{}'.format(end-start))

    
if __name__ == '__main__':
    print('当前主进程：{}'.format(os.getpid()))
    single_process()
    #multi_process()    
    multi_pool()





















 