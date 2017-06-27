#encoding:utf8
import urllib
import urllib2
import httplib
import time
from urlparse import urlparse
import traceback

class Debug(object):
    def trace(self,msg):
        print msg
debug=Debug()

def func1():
    test_data = {'user_name':'xfy123','user_type':'P', 'password':'123456'}
    test_data_urlencode = urllib.urlencode(test_data)
    #requrl = "http://192.168.40.202:5000/mobile/ajax/login"
    requrl = "http://192.168.30.26:5000/test/xxxx"
    req = urllib2.Request(url = requrl, data =test_data_urlencode)
    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    
def func2():
    conn=httplib.HTTPConnection("192.168.30.26:5000")
    conn.request("GET", "/test/xxxx")
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
    if False:
        set_cookie=httppost('POST','http://192.168.40.202:5000/mobile/ajax/login', None, **{'user_name':'test13','user_type':'P', 'password':'qqqqqq'})
        #httppost('http://192.168.40.202:5000/mobile/ajax/login', user_name='xfy123')
        print set_cookie
        httppost('GET', 'http://192.168.40.202:5000/report')
    if True:
        httppost('GET', 'http://192.168.30.26:5000/test/xxx', **{'username':'joy'})
    
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
            #print 'status:', response.status
            #print 'reason:', response.reason
            #print 'read():', response.read()
            #print 'getheaders():', response.getheaders()
            for item in response.getheaders():
                print 'response headers:', item[0]
                if item[0]=='set-cookie':set_cookie=item[1]
        except Exception, e:
            print e
            excstr = traceback.format_exc()
            print excstr
        finally:
            if httpClient:
                httpClient.close()
        return set_cookie
    rv=httppost('POST','192.168.30.26', 5000, '/mobile/ajax/login', None, **{'user_name':'test13','user_type':'P', 'password':'qqqqqq'})
    #rv=httppost('http://192.168.40.202:5000/mobile/ajax/login', user_name='xfy123')
    #set_cookie='session=.eJwdjkFvgkAQRv9KM2cPsJQeSDzYLG7aZGazZiqZvZh0pcICF9SgGP97idcvL-99Dzj8jfW5geIyXusVHNojFA94-4UCvP5sRZU5Geotl6lnN6GRBJXvkbvEmlKRxpRYZlt93TFuB4rhjiwKK6dE7XsyviUdlMwu97FcdkyRfRTeN1LhO-m-83G3dLYd8a6zmoaFmUgfB9Knm8whX5wTme9G2OXImwTNT4YcbmRc6uMpsRzW8FzB9VyPr_-QZR_w_Afdh0Ww.Cs-Vqw.CIhHAezb3Cgk5uGvNnU59NKI27g; HttpOnly; Path=/'
    print 'rv:', rv
    #return 
    #set_cookie='session=.eJwdjrFqwzAQQH-l3Jyh0cUdDB1S5IYEJCEjV9wtgaZuE8lenAaFC_n3Ot0ejze8G-y_p_58hPp3uvQL2J--oL7B0yfUQClXVr2fWO9GksPSprXQ2BQO3YqizaQM0vgxcGiTC7ni0QtJd51ZKJLi1BS3aQejt4U3W2X1-sopI6kGXTigjU01O7QhLznujhQ8PhpSHRr5mRv_7LQX1lScbrPVPNhghJRHF_3KyNvjq7hoXuG-gMu5n_7_AfEF7n-8m0a7.CvmVXA.GBcBruckgiEzDyECieZnl91BBZE; HttpOnly; Path=/'
    set_cookie=rv
    
    #print set_cookie
    #rv=httppost('GET', '192.168.30.26', 5000, '/mobile/ajax/getinfo', set_cookie, 
    #        **{'flag':'person_info'})
    #print len(set_cookie), len(rv)
    for i in xrange(10):
        #set_cookie=None
        print 'cookie:', set_cookie
        #rv=httppost('POST', '192.168.30.26', 5000, '/mobile/ajax/user', set_cookie, 
        #        **{'action':'chklogin', 'deviceToken':'xxxxx', 'uid':109} )
        rv=httppost('POST', '192.168.30.26', 5000, '/mobile/ajax/getinfo', set_cookie, 
                **{'action':'chklogin', 'deviceToken':'xxxxx', 'uid':109} )
        #print len(set_cookie) #, len(rv)
        #set_cookie=rv
        print 'set_cookie:1:', rv
        time.sleep(1)
    
# 
if __name__=='__main__':
    func5()