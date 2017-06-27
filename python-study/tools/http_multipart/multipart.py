# coding=utf8
import sys
import urllib2;

import json;
import formdata
 
port=5001 

def post_data():

    parameters = {'id': '', 'user': { 'username': '', 'password': '' }, 'query': { 'fromStation': 'beijing', 'fromStationText': 'shanghai' }}

    jdata = json.dumps( parameters )

    #post_multipart( 'http://extention.ie.sogou.com/mm_12306/prebook', jdata )
    post_multipart( 'http://192.168.30.26:8001/xieruhuause/upload.php', jdata )

def post_data2():
    fields=[('args1', 'sdf'), 
            #('userfile[]', r"f'C:/Users/zhoufan/Desktop/12/002.txt'"), 
            #('userfile[]', r"f'C:/Users/zhoufan/Desktop/12/003.txt'"),
            ('userfile2', r"f'C:/Users/zhoufan/Desktop/12/004.txt'"),
            ]
    #post_multipart( 'http://192.168.30.26:%s/xieruhuause/upload.php' % port, fields )
    post_multipart( 'http://192.168.40.202:%s/xieruhuause/upload.php' % port, fields )

def post_multipart( url , fields ):

 

    #content_type, body = encode_multipart_formdata( "data", fields )
    content_type, body = formdata.encode_multipart_formdata(fields )
    print 'content_type', content_type
 

    req = urllib2.Request( url, data=body )
    print url
    print body
    
    #req.add_header( "User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0)" )

    #req.add_header( "Accept", "*/*" )

    #req.add_header( "Accept-Language", "zh-CN,zh;q=0.8" )

    #req.add_header( "Accept-Encoding", "gzip,deflate,sdch" )

    #req.add_header( "Connection", "keep-alive" )

    req.add_header( "Content-Type", content_type )

    #req.add_header( "User-Agent1", "SogouMSE" )

   

    try:

        response = urllib2.urlopen( req )

        tmp_resp=response.read()
        print type(tmp_resp)
        print tmp_resp
        the_page = tmp_resp.decode( 'utf-8' )

        print the_page
        with open('result.html', 'w') as fo:
            fo.write(the_page.encode('gbk'))

        return the_page

    except urllib2.HTTPError, e:

        print e.code

        pass

    except urllib2.URLError, e:

        print str( e )

        pass

 

def encode_multipart_formdata( key, value ):

 

    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'

    CRLF = '\r\n'

    L = []

    L.append( '--' + BOUNDARY )

    L.append( 'Content-Disposition: form-data; name="%s"' % key )

    L.append( '' )

    L.append( value )

 

    L.append( '--' + BOUNDARY + '--' )

    L.append( '' )

    body = CRLF.join( L )

    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY

    return content_type, body

   

if __name__ == '__main__':
    if len(sys.argv)>=2:
        port=sys.argv[1]

    post_data2();