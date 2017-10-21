#encoding:utf8
import json
import datetime
import time
import base64
import urllib2,urllib

#host_url='http://127.0.0.1:5000'
#host_url='http://192.168.30.26:5000'
host_url='http://192.168.30.26:8081'
#host_url='http://192.168.40.202:5000'


login_url=host_url+'/api/v2.0/login'
logout_url=host_url+'/api/v2.0/logout'
user_url=host_url+'/api/v2.0/user/%(username)s'

regist_url=host_url+'/api/v2.0/regist'
pdm_sessions_url=host_url+'/api/v2.0/pdm/%(uid)s/sessions'

context={}

def login(args):
    #data = urllib.urlencode({
    #    #'user_name': 'test13', 'user_type': 'P', 'password': 'qqqqqq'
    #})
    data=urllib.urlencode(args)
    req = urllib2.Request(login_url, data)
    rsp = urllib2.urlopen(req)
    # print 'rsp:', dir(rsp), rsp.headers, type(rsp)
    # print 'cookie:', rsp.headers.get('Set-Cookie')
    cookie = rsp.headers.get('Set-Cookie')
    rv = rsp.read()
    rv=json.loads(rv, encoding='utf8')
    #if 'OK'==rv['res']:
    if 0==rv['error']:
        print 'cookie:', cookie
        context['cookie']=cookie
    return rv

def login_v2(args):
    #data = urllib.urlencode(args)
    data=json.dumps(args, ensure_ascii=False)
    req = urllib2.Request(login_url, data, {'Content-Type':'application/json;charset=UTF-8'})
    rsp = urllib2.urlopen(req)
    # print 'rsp:', dir(rsp), rsp.headers, type(rsp)
    # print 'cookie:', rsp.headers.get('Set-Cookie')
    cookie = rsp.headers.get('Set-Cookie')
    rv = rsp.read()
    print 'login:', rv
    with open('login.txt', 'wb') as fo:
        fo.write(rv)
    rv = json.loads(rv, encoding='utf8')
    # if 'OK'==rv['res']:
    if 0 == rv['error']:
        print 'cookie:', cookie
        context['cookie'] = cookie
    return rv

def http_post(req_url, args, **opt):
    show_header=opt.get('show_header', False)
    pass
    #data = urllib.urlencode({
    #    'flag': 'apply_monitor', 'user_name': 'test15'
    #})
    #if args:
    if args:
        data = urllib.urlencode(args)
    else:
        data=None
    req = urllib2.Request(req_url, data, {'Cookie':context.get('cookie')})
    rsp = urllib2.urlopen(req)
    
    rv = rsp.read()
    if show_header:
        print 'header:', rsp.headers
    return rv


def http_post_v2(req_url, args, **opt):
    show_header = opt.get('show_header', False)
    pass
    '''
    # data = urllib.urlencode({
    #    'flag': 'apply_monitor', 'user_name': 'test15'
    # })
    # if args:
    if args:
        data = urllib.urlencode(args)
    else:
        data = None
    
    req = urllib2.Request(req_url, data, {'Cookie': context.get('cookie')})
    rsp = urllib2.urlopen(req) '''

    data = json.dumps(args, ensure_ascii=False).encode('utf8')
    #print 'data:', data
    #with open('out.txt', 'wb') as fo:
    #    fo.write(data)
        
    req = urllib2.Request(req_url, data, {'Content-Type': 'application/json;charset=UTF-8',
                                          'Cookie': context.get('cookie')  })
    rsp = urllib2.urlopen(req)
    
    
    rv = rsp.read()
    if show_header:
        print 'header:', rsp.headers
    return rv


def http_get(req_url, args=None, **opt):
    show_header = opt.get('show_header', False)
    pass
    # data = urllib.urlencode({
    #    'flag': 'apply_monitor', 'user_name': 'test15'
    # })
    # if args:
    if args:
        data = urllib.urlencode(args)
        req_url += '?'+data
    #else:
    #    data = None
    req = urllib2.Request(req_url, None, {'Cookie': context.get('cookie')})
    rsp = urllib2.urlopen(req)
    
    rv = rsp.read()
    if show_header:
        print 'header:', rsp.headers
        
    try:
        pass
        #return json.loads(rv, encoding='utf8')
    except Exception,e:
        pass
    with open('rv.txt', 'wb') as fo:
        fo.write(rv)
        
    return rv


# ===========================================================================================================

#@app_login_wrap(user_name='zftest1', user_type='P', password='123122', apptype='S6')
def test_api_login():
    login_v2({
        'user_name':'zftestp5',
        'user_type': 'P',
        'password': 'A1122b',
        'apptype': 'S6',
        'bundleID':'com.medtrum.EasySense.mg',
        'deviceToken':'test_token',
        'platform':'ios',
        'production':'no'
    })
    #rv = http_post(set_device_option_url, {'name':'cgms', 'option':'on'})
    #print 'set dev opt:', rv
    
    #rv=http_post_v2(logout_url, {})
    #print 'login:', rv

def test_api_user():
    rv=http_get(user_url%{'username':'zftestp1'})
    print 'rv:', rv

def test_api_regist():
    rv=http_post(regist_url, {
        'user_name':'zftest1a', 
        'user_type':'P',
        'password':'123456',
        'invite_code':'259470'
        
    })
    print 'rv:', rv


def test_api_pdm_sessions():
    rv = login_v2({
        'user_name': 'tshenks3',
        'user_type': 'P',
        'password': 'sks.0116',
    })
    print 'login.rv:', rv
    uid = rv.get('uid')
    
    if not rv.get('error'):
        rv = http_get(pdm_sessions_url % {'uid': uid})
        print 'sessions:', rv

def func1():
    # urllib2的Request好像会受到谷歌浏览器设置HTTP代理的影响。
    # 但是HttpConnect好像不会。
    http_get("http://192.168.30.26:8081/")
    
if __name__=='__main__':
    pass
    #
    #test_api_login()
    func1()