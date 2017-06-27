#!/usr/bin/env python
#encoding:utf-8

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json
import time

def fetch(pid):
    #response = urllib2.urlopen('http://json-time.appsopt.com/time.json')
    response = urllib2.urlopen('http://192.168.30.26:5000')
    
    print 'Process %s:%s' % (pid, time.time())
    '''result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']
    
    print 'Process %s:%s' % (pid, datetime)
    #return json_result['datetime']'''

def synchronous():
    for i in range(1, 10):
        fetch(i)
        
def asynchronous():
    threads=[]
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    #    
    gevent.joinall(threads)

print 'Synchronous:'
synchronous()

print 'Asynchronous:'
asynchronous()        
            