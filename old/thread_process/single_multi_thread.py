# -*- coding: utf-8 -*-

'''
单线程、多线程测试计算耗时
Author: epsilono1
Date: 2020年9月16日 18:24:46
'''

from threading import Thread, current_thread
import time

def long_time_task(i):
    print('当前子线程：{} - 任务{}'.format(current_thread().name, i))
    time.sleep(2)
    print('计算结果：{}'.format(8**20))
    
def multi_thread():
    print('当前线程：{}'.format(current_thread().name))
    start = time.time()
    t1 = Thread(target=long_time_task, args=(1,))
    t2 = Thread(target=long_time_task, args=(2,))
    t1.start()
    t2.start()
    t1.join()    #没有这两句join语句，耗时为0秒，这是因为主线程没等子线程执行完就打印时间结束了
    t2.join()    #并且主线程结束后，子线程还在执行，显然不妥，所以必需join来同步主子线程。如果希望主线程结束后子线程不再执行，则在子线程开始前用t1.setDaemon(True)
    end = time.time()
    print('多线程耗时：{} 秒'.format(end-start))

if __name__ == '__main__':
    print('主线程：{}'.format(current_thread().name))
    multi_thread()

