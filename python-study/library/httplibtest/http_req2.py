#encoding:utf8
import urllib
import urllib2
import httplib
import time
from urlparse import urlparse
import traceback
import json

class Debug(object):
    def trace(self,msg):
        print msg
debug=Debug()

def func1():
    test_data = {'user_name':'xfy123','user_type':'P', 'password':'123456'}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "http://192.168.40.202:5000/mobile/ajax/login"
    req = urllib2.Request(url = requrl, data =test_data_urlencode)
    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    
def func2():
    conn=httplib.HTTPConnection("192.168.30.26:5000")
    conn.request("GET", "/login")
    res=conn.getresponse()
    debug.trace(["status:", res.status])
    debug.trace(["reason:", res.reason])
            
def func3():
    test_data = {'user_name':'xfy123','user_type':'P', 'password':'123456'}
    test_data_urlencode = urllib.urlencode(test_data)
    print test_data_urlencode, type(test_data_urlencode)
    #
    conn=httplib.HTTPConnection("192.168.30.26:5000")
    conn.request("POST", "/mobile/ajax/login", body=test_data_urlencode)
    res=conn.getresponse()
    debug.trace(["res:", res, dir(res)])
    debug.trace(["status:", res.status])
    debug.trace(["reason:", res.reason])
    buf=res.read(-1)
    debug.trace(["buf:", buf])
    debug.trace(["header:", res.getheaders()])
    #debug.trace(["header:", res.getheader()])
    
def func4():
    def httppost(med, url, cookie=None, **kwgs):
        httpClient = None
        conn = urlparse(url)
        set_cookie=None
        try:
            params = urllib.urlencode(dict(kwgs))
            # Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
            header = {"Content-type": "application/x-www-form-urlencoded",
                      "Accept": "text/plain", 
                      }
            if cookie:header['Cookie']=cookie
            

            httpClient = httplib.HTTPConnection('192.168.30.26', conn.port, timeout=30)
            print conn.netloc, conn.port, conn.path
            httpClient.request(med, conn.path, params, header)

            response = httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
            print response.getheaders()
            for item in response.getheaders():
                if item[0]=='set-cookie':set_cookie=item[1]
        except Exception, e:
            print e
            excstr = traceback.format_exc()
            print excstr
        finally:
            if httpClient:
                httpClient.close()
        return set_cookie
    set_cookie=httppost('POST','http://192.168.40.202:5000/mobile/ajax/login', None, **{'user_name':'test13','user_type':'P', 'password':'qqqqqq'})
    #httppost('http://192.168.40.202:5000/mobile/ajax/login', user_name='xfy123')
    print set_cookie
    httppost('GET', 'http://192.168.40.202:5000/report')
    
def func5():
    def httppost(med, host, port, path, cookie=None, **kwgs):
        httpClient = None
        #conn = urlparse(url)
        set_cookie=None
        try:
            params = urllib.urlencode(dict(kwgs))
            # Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
            # 必须要指定Content-type字段。
            header = {
                "Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain", 
            }
            if cookie:header['Cookie']=cookie
            

            httpClient = httplib.HTTPConnection(host, port, timeout=30)
            #print conn.netloc, conn.port, conn.path
            httpClient.request(med, path, params, header)

            response = httpClient.getresponse()
            print 'status:', response.status
            #print 'reason:', response.reason
            print 'read():', response.read()
            #print 'getheaders():', response.getheaders()
            for item in response.getheaders():
                if item[0]=='set-cookie':set_cookie=item[1]
        except Exception, e:
            print e
            excstr = traceback.format_exc()
            print excstr
        finally:
            if httpClient:
                httpClient.close()
        return set_cookie
    #set_cookie=httppost('POST','192.168.40.202', 5000, '/mobile/ajax/login', None, **{'user_name':'test13','user_type':'P', 'password':'qqqqqq'})
    #httppost('http://192.168.40.202:5000/mobile/ajax/login', user_name='xfy123')
    #set_cookie='session=.eJwdjkFvgkAQRv9KM2cPsJQeSDzYLG7aZGazZiqZvZh0pcICF9SgGP97idcvL-99Dzj8jfW5geIyXusVHNojFA94-4UCvP5sRZU5Geotl6lnN6GRBJXvkbvEmlKRxpRYZlt93TFuB4rhjiwKK6dE7XsyviUdlMwu97FcdkyRfRTeN1LhO-m-83G3dLYd8a6zmoaFmUgfB9Knm8whX5wTme9G2OXImwTNT4YcbmRc6uMpsRzW8FzB9VyPr_-QZR_w_Afdh0Ww.Cs-Vqw.CIhHAezb3Cgk5uGvNnU59NKI27g; HttpOnly; Path=/'
    
    set_cookie='session=.eJwdjrFqwzAQQH-l3Jyh0cUdDB1S5IYEJCEjV9wtgaZuE8lenAaFC_n3Ot0ejze8G-y_p_58hPp3uvQL2J--oL7B0yfUQClXVr2fWO9GksPSprXQ2BQO3YqizaQM0vgxcGiTC7ni0QtJd51ZKJLi1BS3aQejt4U3W2X1-sopI6kGXTigjU01O7QhLznujhQ8PhpSHRr5mRv_7LQX1lScbrPVPNhghJRHF_3KyNvjq7hoXuG-gMu5n_7_AfEF7n-8m0a7.CvmVXA.GBcBruckgiEzDyECieZnl91BBZE; HttpOnly; Path=/'
    
    
    #print set_cookie
    #rv=httppost('GET', '192.168.30.26', 5000, '/mobile/ajax/getinfo', set_cookie, 
    #        **{'flag':'person_info'})
    #print len(set_cookie), len(rv)
    for i in xrange(2):
        print 'set_cookie:1:', set_cookie
        rv=httppost('GET', '192.168.30.26', 5000, '/mobile/ajax/getinfo', set_cookie, 
                **{'flag':'person_info'})
        #print len(set_cookie) #, len(rv)
        set_cookie=rv
        print 'set_cookie:2:', set_cookie
        time.sleep(1)

debug_mode=False
        
# 安卓推送测试代码
def func6():
    post_data={
        'to':'fpHjmZ2sTA8:APA91bHIShqTcPe2zhvnPEmVxoPfpLbLDEpqlOwN_1bQkfuhsHrXZkKmd9IE4EGW0xD99yk-5mqFmTfWXnz6Nnnkm6wl5wRoNgENDLt_F5QIoPi9yb6hw8ZBhuyGYnLmnEf8Y59a91FI',
        'data':{
            'score':'5x1',
            'time':'15:10'
        },
    }
    post_urlenc = urllib.urlencode(post_data)
    print 'post_urlenc:', post_urlenc
    post_json=json.dumps(post_data, ensure_ascii=False)
    print 'post_json:', post_json
    
    header = {
        "Content-type": "application/json",
        #"Accept": "text/plain", 
        'Authorization':'key=AAAAQWyKfIw:APA91bHRxZm5KIu8QG6E8ZpG-2XVs0Hq0hvpRML577ztwaHgHfQhRz22jV6JMN3FYbez_rM-DWccmdkP6Go48a2EeAp_9Enbqf5yGLBfNWIsrVT69djQ1uBp4OCTHjzYD06g11RtZVd9'
    }
    
    try:
        if debug_mode:
            httpClient = httplib.HTTPSConnection('192.168.30.26', 5010, timeout=30)
        else:
            httpClient = httplib.HTTPSConnection('fcm.googleapis.com', 80, timeout=30)
        #print conn.netloc, conn.port, conn.path
        if debug_mode:
            httpClient.request('POST', '/ajax/json', post_json, header)
        else:
            httpClient.request('POST', '/fcm/send', post_json, header)
        response = httpClient.getresponse()
        print 'status:', response.status
        #print 'reason:', response.reason
        print 'read():', response.read()
    except Exception, e:
        print e
        excstr = traceback.format_exc()
        print 'excstr:1:', excstr
    finally:
        if httpClient:
            httpClient.close()
# 
if __name__=='__main__':
    #func5()
    func6()