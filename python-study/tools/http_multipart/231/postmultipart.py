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
data.append('Content-Disposition: form-data; name="libzip"; filename="C:/Users/zhoufan/Desktop/12/002.png"')  
data.append('Content-Type: application/octet-stream\r\n')  
  
fr=open('C:/Users/zhoufan/Desktop/12/002.png')  
content=fr.read()  
data.append(content)  
#print content  
fr.close()
data.append('--%s--\r\n'%boundary)  
httpBody='\r\n'.join(data)  

print type(httpBody) , len(httpBody)
print httpBody
#print type(httpBody)  
#print httpBody  
  
postDataUrl='http://192.168.30.26:5001/xieruhuause/upload.php'  
print postDataUrl
req=urllib2.Request(postDataUrl,data=httpBody)  
print req,dir(req)

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
