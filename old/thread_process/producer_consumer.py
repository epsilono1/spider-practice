#-*- coding: utf-8 -*-

'''
经典生产者-消费者模型
使用queue实现线程间通信
Author: epsilono1
Date: 2020年9月17日 10:34:15
'''

from queue import Queue
from threading import Thread
import time, random

class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name) #只写name不写name=name,报错：AssertionError: group argument must be None for now
        self.queue = queue
        
    def run(self):
        for i in range(1, 5):
            print('{} is producing {}'.format(self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10)/5)
        print('%s finished!' % self.getName())
            
class Consumer(Thread):
    def __init__(self, name, queue):
        # Thread.__init__(self, name=name)
        # super(Consumer, self).__init__(name=name) #python2的super
        super().__init__(name=name)                 #python3的super
        self.queue = queue
        
    def run(self):
        for i in range(1, 5):
            val = self.queue.get()
            print('{} is consuming {}'.format(self.getName(), val))
            time.sleep(random.randrange(10))
        print('%s finished!' % self.getName())
        
def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    
    producer.start()
    consumer.start()
    
    producer.join()
    consumer.join()
    print('All threads finished!')
    
    
if __name__ == '__main__':
        main()

        
        