#encoding:gbk

import urllib

class Debug(object):
    def trace(self, msg):
        print msg
debug=Debug()

def func1():
    #fh=urllib.urlopen("http://192.168.30.26:5000")
    #debug.trace(["typeof fh:", type(fh), dir(fh)])
    #fh.close()
    
    #fh=urllib.urlretrieve("http://192.168.30.26:5000/static/images/ad_9.jpg", "1.jpg")
    fh=urllib.urlretrieve("http://192.168.30.26:5000", "index.html")
    debug.trace(["typeof fh:", type(fh), fh])
    

if __name__=="__main__":
    func1()