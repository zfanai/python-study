#encoding:utf8

import urllib2,urllib

data=urllib.urlencode({
    'data':'ddd'
    })
#req1=urllib2.Request('https://easyview.medtrum.cn/async/push_msg_to_app', data)
req1=urllib2.Request('https://easyview.medtrum.cn/async/push_msg_to_app')
r=urllib2.urlopen(req1)
print r

