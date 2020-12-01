#-*- coding: utf-8 -*-

'''
使用队列Queue实现不同进程间的通信或数据共享
防止进程间因共享内存相互竞争
Author: epsilono1
Date: 2020年9月16日 17:49:12
'''

import os, time, random
from multiprocessing import Process, Queue

#写数据进程执行代码
def write(q):
    print('Process to write: {}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)   #程序主体向CPU写入，主体视角
        time.sleep(random.random())

#读数据进程执行代码         
def read(q):
    print('Process to read: {}'.format(os.getpid()))
    while True: #死循环程序
        value = q.get(True)  #程序主体从CPU读取/获取，主体视角
        print('Get %s from queue.' % value)
        
if __name__ == '__main__':
    #主进程创建Queue，并传给各个子进程
    q = Queue()    
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()      #等待pw结束
    pr.terminate() #pr子进程有死循环，无法等待结束，只能强制终止
    