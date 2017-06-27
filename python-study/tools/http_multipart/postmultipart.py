#encoding:utf8

import urllib2

boundary='-------------------------7df3069603d6'  
data=[]  
data.append('--%s' % boundary)  
data.append('Content-Disposition: form-data; name="app_id"\r\n')  
data.append('xxxxxx')  
data.append('--%s' % boundary)  
data.append('Content-Disposition: form-data; name="version"\r\n')  
data.append('xxxxx')  
data.append('--%s' % boundary)  
data.append('Content-Disposition: form-data; name="platform"\r\n')  
data.append('xxxxx')  
data.append('--%s' % boundary)  
# name字段决定Flask的request.files里面的关键字。
#data.append('Content-Disposition: form-data; name="libzip"; filename="001.jpeg"')  
#data.append('Content-Disposition: form-data; name="userfile"; filename="001.jpeg"')  
data.append('Content-Disposition: form-data; name="pdmdata"; filename="pdmdata.json"')  
data.append('Content-Type: application/octet-stream\r\n')  
  
#fr=open('C:/Users/zhoufan/Desktop/12/002.png')  
#fr=open('001.jpeg', 'rb')  
fr=open('pro_upload.json', 'rb')  
content=fr.read(-1)  
#print 'file size:', len(content)
data.append(content)  
#print content  
fr.close()
data.append('--%s--\r\n'%boundary)  
httpBody='\r\n'.join(data)  
content_type = 'multipart/form-data; boundary=%s' % boundary 

print type(httpBody) , len(httpBody)
#print httpBody
#print type(httpBody)  
#print httpBody  
  
#postDataUrl='http://192.168.30.26:5001/xieruhuause/upload.php'  
#postDataUrl='http://192.168.30.26:5000/pro/84/patients/397/portrait'  
#postDataUrl='http://192.168.30.26:5000/pro/84/patients/397/pdm'  
#postDataUrl='http://192.168.30.26:5000/pro/84/patients/109/pdm'  
postDataUrl='http://192.168.40.202:5000/pro/84/patients/344/pdm'  
print postDataUrl
req=urllib2.Request(postDataUrl,data=httpBody)  
print req,dir(req)
req.add_header( "Content-Type", content_type )

try:
    response = urllib2.urlopen( req )
    the_page = response.read().decode( 'utf-8' )
    print the_page
    #return the_page
except urllib2.HTTPError, e:
    print e.code
    pass
except urllib2.URLError, e:
    print str( e )
    pass
