#!usr/bin/env 
#encoding:utf-8

import sys
 
import gevent
from gevent import monkey
 
monkey.patch_all()
 
import grequests
import urllib2
 
def call_back(resp):
    content = resp.content
    #title = content.split('')[1].split('')[0].strip()
    return content
 
def worker(url, use_urllib2=False):
    if use_urllib2:
        content = urllib2.urlopen(url).read().lower()
        #title = content.split('')[1].split('')[0].strip()
 
    else:
        rs = [grequests.get(u) for u in url]
        resps = grequests.map(rs)
        for resp in resps:
            call_back(resp) 
 
#urls = ['http://www.douban.com']*5
urls = ['http://192.168.30.26:5000']*5
 
def by_requests():
    worker(urls)
def by_urllib2():
    jobs = [gevent.spawn(worker, url, True) for url in urls]
    gevent.joinall(jobs)
 
if __name__=='__main__':
    from timeit import Timer
    t = Timer(stmt="by_requests()", setup="from __main__ import by_requests")
    print 'by grequests: %s seconds'%t.timeit(number=3)
    t = Timer(stmt="by_urllib2()", setup="from __main__ import by_urllib2")
    print 'by gurllib2: %s seconds'%t.timeit(number=3)
    sys.exit(0)