#encoding=gbk

import sys
import os
import fnmatch
import traceback
import re

def trace(obj):
    print "trace:", obj


def _findGoogleApis(filename):
    #trace(["_find_replace"])
    res=[]
    try:
        fo=open(filename, "r+")
        buf=fo.read(-1)
        #trace(["buf size:", len(buf)])
        #
        #trace(["find,replace:", ord(find), ord(replace)])
        #buf2=buf.replace(find, replace)
        #fo.truncate(0)
        #fo.seek(0,os.SEEK_SET)
        #fo.write(buf2)
        # 正则表达式
        #
        fo.close()
        #
        #fontGoogleapisUrl=[]
        #
        res=re.findall("\"http://fonts.googleapis.com/css[^\"]+\"", buf)
        #trace(rv)
        #rv=list(set(rv))
        #fontGoogleapisUrl+=rv
        
    except:
        excstr=traceback.format_exc()
        print excstr
        res=[]
        #fo.close()
    return res

def _findCssStaticFont(filename):
    trace(["_find_replace"])
    res=[]
    try:
        fo=open(filename, "r+")
        buf=fo.read(-1)
        #trace(["buf size:", len(buf)])
        #
        #trace(["find,replace:", ord(find), ord(replace)])
        #buf2=buf.replace(find, replace)
        #fo.truncate(0)
        #fo.seek(0,os.SEEK_SET)
        #fo.write(buf2)
        # 正则表达式
        #
        fo.close()
        #
        #fontGoogleapisUrl=[]
        #
        res=re.findall("url\(http://fonts[^)]+\)", buf)
        #trace(rv)
        #rv=list(set(rv))
        #fontGoogleapisUrl+=rv
        
    except:
        excstr=traceback.format_exc()
        print excstr
        res=[]
        #fo.close()
    print len(res)
    return res   

# 替换一个文件。   
def _find_replace(filename, findReplace):
    pass
    trace(["_find_replace"])
    try:
        fo=open(filename, "r+")
        buf=fo.read(-1)
        trace(["buf size:", len(buf)])
        #
        #trace(["find,replace:", ord(find), ord(replace)])
        for item in findReplace:
            find,replace=item[0:2]
            buf2=buf.replace(find, replace)
            buf=buf2
        #
        fo.truncate(0)
        fo.seek(0,os.SEEK_SET)
        fo.write(buf2)
        #
        fo.close()
    except:
        pass
        excstr=traceback.format_exc()
        print excstr
        #fo.close()

# 替换一个文件。   
def _find_replace_reg(filename, findReplace):
    pass
    trace(["_find_replace"])
    try:
        fo=open(filename, "r+")
        buf=fo.read(-1)
        trace(["buf size:", len(buf)])
        #
        #trace(["find,replace:", ord(find), ord(replace)])
        for item in findReplace:
            find,replace=item[0:2]
            #buf2=buf.replace(find, replace)
            buf2=re.sub(find, replace, buf)
            buf=buf2
        #trace(buf)
        #
        fo.truncate(0)
        fo.seek(0,os.SEEK_SET)
        fo.write(buf2)
        #
        fo.close()
    except:
        pass
        excstr=traceback.format_exc()
        print excstr
        #fo.close()
        
def findGoogleApis(target_dir, single_level=False):
    trace(["target_dir:", target_dir])
    #
    patterns='*.html'
    patterns = patterns.split(';')
    
    # 目录名称
    dirname = os.path.dirname(target_dir)
    pos=len(dirname)
    
    #print os.path.exists(target_dir)
    if not os.path.exists(target_dir):
        print "dir dose not exist"
        raise Exception
    
    # 
    fontGoogleapisUrl=[]
    for path, subdirs, files in os.walk(target_dir):
        #if yield_folders:
        #    files.extend(subdirs)
        #    files.sort()
        #print subdirs
        for name in files:
            #trace(["name:", name])
            for pattern in patterns:
                #trace(["pattern:", pattern])
                if fnmatch.fnmatch(name, pattern.strip()):# 去除pattern两端的空格
                    #print os.path.join(path, name)
                    #print "123"
                    #
                    abspath = os.path.join(path, name)
                    #abspath.replace("\\", "/")
                    #yield abspath[pos:]
                    #trace(["abspath:", abspath])
                    #
                    #rv=_findGoogleApis(abspath)
                    #rv=_findCssStaticFont(abspath)
                    #rv=list(set(rv))
                    #fontGoogleapisUrl += rv
                    #for item in rv:
                    #    if item not in fontGoogleapisUrl:
                    #        fontGoogleapisUrl.append(item)
                    
                    
            #
            #break
        
        if single_level:
            break  
    #
    #fo=open('fontgoogleapis.txt', 'w')
    #for item in fontGoogleapisUrl:
    #    fo.write(item+'\n')
    #fo.close()

# 替换
def findReplaceGoogleApis(target_dir, single_level=False):
    trace(["target_dir:", target_dir])
    #
    patterns='*.css'
    patterns = patterns.split(';')
    
    # 目录名称
    dirname = os.path.dirname(target_dir)
    pos=len(dirname)
    
    #print os.path.exists(target_dir)
    if not os.path.exists(target_dir):
        print "dir dose not exist"
        raise Exception
    
    #
    #"http://fonts.googleapis.com/css?family=Roboto+Condensed"
    #"http://fonts.googleapis.com/css?family=Roboto:light,regular,medium,thin,italic,mediumitalic,bold"
    #"http://fonts.googleapis.com/css?family=Roboto+Mono:400,500,700"
    
    '''
    findReplace=[
                #["http://fonts.googleapis.com/css?family=Roboto+Condensed", 
                ["//fonts.googleapis.com/css?family=Roboto+Condensed", 
                  'css_family_Roboto_Condensed.css'], 
                 #["http://fonts.googleapis.com/css?family=Roboto:light,regular,medium,thin,italic,mediumitalic,bold", 
                 ["//fonts.googleapis.com/css?family=Roboto:light,regular,medium,thin,italic,mediumitalic,bold", 
                  'css_family_Roboto_light_regular_medium_thin_italic_mediumitalic_bold.css'], 
                 #["http://fonts.googleapis.com/css?family=Roboto+Mono:400,500,700", 
                 ["//fonts.googleapis.com/css?family=Roboto+Mono:400,500,700", 
                  'css_family_Roboto_Mono_400_500_700.css']]
    '''
    #findReplace=[['https://developer.android.com/ytblogger_lists_unified.js', 'js/ytblogger_lists_unified.js']]
    #findReplace=[['http://www.google.com/jsapi', 'js/jsapi.js']]
    #[['www.google-analytics.com']]
    findReplace=[]
    fo=open('fontgoogleapis.txt')
    strLine=fo.readline()
    while strLine:
        strUrl=strLine.strip()[4:-1]
        strLine=strUrl[7:]
        #debug.trace(strLine)
        #trace(strUrl)
        urlSplit=strLine.split('/')
        strFileName='_'.join(urlSplit[1:])
        #debug.trace(urlSplit)
        #trace(strFileName)
        #
        #urllib.urlretrieve(strUrl, strFileName)
        findReplace.append([strUrl, '../font/'+strFileName])
        #
        strLine=fo.readline()
    fo.close()
    #trace(findReplace)
    #
    baseDirSize=len(target_dir)
    # 
    fontGoogleapisUrl=[]
    count=0
    for path, subdirs, files in os.walk(target_dir):
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern.strip()):# 去除pattern两端的空格
                    abspath = os.path.join(path, name)
                    # 替换
                    relPath=path[baseDirSize+1:]
                    #strPrefix='static/css/'
                    if len(relPath)==0:
                        dirNum=0
                        strPrefix='static/'
                    else:
                        dirNum=len(relPath.split('\\'))
                        strPrefix='../'*dirNum+'static/'
                    
                    #trace([relPath, dirNum, strPrefix])
                    # 是这里的问题。
                    #newFindReplac=[]
                    #for item in findReplace:
                    #    item[1]=strPrefix+item[1]
                    #newFindReplace=map(lambda x:[x[0], strPrefix+x[1]], findReplace)
                    newFindReplace=findReplace
                    #
                    #trace(newFindReplace)
                    _find_replace(abspath, newFindReplace)
                    #regExp='<script>([^<]*www.google-analytics.com/analytics.js[^<]*(?<!</))</script>'
                    #repExp='<!--<script>\\1</script>-->'
                    #_find_replace_reg(abspath, [[regExp, repExp]])
                    count+=1
                    #if count>100:return
        if single_level:
            break  
            
# @note zhoufan
# 命令行参数 target_dir pattern find replace 
# pattern用分号隔开。
if __name__ == "__main__":
    arg_size = len(sys.argv)
    if arg_size<2:
        print "[Usage]:target_dir pattern find replace "
        sys.exit(0)
    else:
        target_dir = sys.argv[1]
        #pattern = sys.argv[2]
        #find = sys.argv[3]
        #replace = sys.argv[4]
        #if find=="tab":
        #    find = "\t"
        #
        #trace(["find:", find])
        #trace(["replace:", replace])
        #trace(["pattern:", pattern])
        
    #
    #findGoogleApis(target_dir)
    findReplaceGoogleApis(target_dir)

