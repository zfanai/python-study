#encoding:utf8

import requests

files={'app_id':(None,'123456'),
  'version':(None,'2256'),
  'platform':(None,'ios'),
  'libzip':('libmsc.zip',open('C:\Users\danwang3\Desktop\libmsc.zip','rb'),'application/x-zip-compressed')
 }
 

request.post() 