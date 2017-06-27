#!usr/bin/env 
#encoding:utf-8

import sys
import requests
import urllib2
from timeit import Timer
import threading as thread

urls = [
    #'http://www.douban.com',
    'http://192.168.30.26:5000',
] * 5
 
def call_back(resp):
    content = resp.content
    #print content
    title = content.split(' ')[1].split(' ')[0].strip()
    return title
 
def by_requests():
    for u in urls:
        call_back(requests.get(u))
 
class doWorker(thread.Thread):
    def __init__(self, url, use_urllib2):
        thread.Thread.__init__(self)
        self.url = url
        self.use_urllib2 = use_urllib2
 
    def run(self):
        if self.use_urllib2:
            content = urllib2.urlopen(self.url).read().lower()
            title = content.split(' ')[1].split(' ')[0].strip()
        else:
            resp = requests.get(self.url)
            call_back(resp)
 
def by_mutiRequests():
    threads = []
    for url in urls:
        threads.append(doWorker(url, False))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
 
def by_mutiUrllib2():
    threads = []
    for url in urls:
        threads.append(doWorker(url, True))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
 
if __name__ == '__main__':
    t = Timer(stmt="by_requests()", setup="from __main__ import by_requests")
    print 'by requests: %s seconds' % t.timeit(number=3)
    t = Timer(stmt="by_mutiRequests()", setup="from __main__ import by_mutiRequests")
    print 'by mutiRequests: %s seconds' % t.timeit(number=3)
    t = Timer(stmt="by_mutiUrllib2()", setup="from __main__ import by_mutiUrllib2")
    print 'by mutiUrllib2: %s seconds' % t.timeit(number=3)