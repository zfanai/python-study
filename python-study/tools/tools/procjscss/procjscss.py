#encoding=gbk

import sys
import os
import fnmatch
import traceback
import re
import shutil
import random
from bs4 import BeautifulSoup
import uuid

'''
2016-8-1 这个目录开始是用来处理Android的文档的，安装的文档引用了很多Google的在线资源。
离线的情况下无法使用。加载很慢，所以写了一个脚本来处理，注释掉很多在线资源。
后来又用来处理过Java的项目结构变更。目的是要把这个工具做成一个通用的处理文件，目录的工具。
后面可能需要改一个合适的名字。
'''
class Debug(object):
    def trace(self, obj):
        print "trace:%s" % obj
    # @note python 不支持重载.
    def t(self, tag, msg):
        print "trace:%s,%s" % (tag, msg)
    def printraw(self, obj):
        print obj
debug=Debug()

class DirFileUtils(object):
    def __init__(self, target_dir):
        self.target_dir=target_dir
    
    # @note 把目录下的一级目录名加一个三位数字的前缀。
    def rename_subdir(self):
        debug.trace(["procjscss target_dir:", target_dir])
        dirList=None
        baseDir=None
        for path, subdirs, files in os.walk(target_dir):
            #debug.trace(['subdirs:', subdirs])
            #for item in subdirs:
            #    debug.printraw(item)
            dirList=subdirs
            baseDir=path
            break
        # \d匹配数字， 同[0-9], {N}匹配N次
        # 
        testCount=0
        dirNum=len(dirList)
        for i in range(dirNum):
            item=dirList[i]
            m=re.match('^\d{3}\.', item)
            if m:pass #debug.trace('match:%s' % item)
            else: # 重命名
                testCount+=1
                oldFilename=os.path.join(target_dir, item)
                newFilename=os.path.join(target_dir, ('%03d.'%i)+item)
                #debug.trace("filename:%s,%s"%(oldFilename, newFilename))
                os.rename(oldFilename, newFilename)
                #if testCount>1
                #break
        self.subdirs=dirList
        
    def find_file(self, pattern, excl=None):
        filelist=self.get_filelist(self.target_dir, pattern, True)
        if excl:
            filelist=filter(lambda x:not re.search(excl, x), filelist)
        #for f in filelist:debug.t("f", f)
        return filelist
            
    def get_filelist(self, d, pattern='.', r=False):
        #pattern = pattern.split(';')
        filelist=[]
        #debug.t("get_filelist", d)
        for path, subdirs, files in os.walk(d):
            #debug.t("files:", files)
            for name in files:
                #for p in pattern:
                #    if fnmatch.fnmatch(name, p.strip()): # 去除pattern两端的空格
                if re.search(pattern, name):
                    abspath = os.path.join(path, name)
                    #trace(["abspath:", abspath])
                    filelist.append(abspath)
            if not r:break
        return filelist
    
    def get_dirlist(self, d, pattern='.', r=False):
        dir_list=[]
        for path, subdirs, files in os.walk(d):
            #debug.t("files:", files)
            '''for name in files:
                for p in pattern:
                    if fnmatch.fnmatch(name, p.strip()): # 去除pattern两端的空格
                        abspath = os.path.join(path, name)
                        #trace(["abspath:", abspath])
                        filelist.append(abspath)'''
            for item in subdirs:
                #debug.t('d', item)
                abspath=os.path.join(path, item)
                if re.search(pattern, abspath):
                    dir_list.append(abspath)
            if not r:break
        return dir_list
    
    def find_dir(self, pattern, excl=None):
        dir_list=self.get_dirlist(self.target_dir, pattern, True)
        if excl:
            dir_list=filter(lambda x:not re.search(excl, x), dir_list)
        for d in dir_list:debug.t("d", d)
        return dir_list
    
    def del_dir(self, dir_list):
        for item in dir_list:
            #os.remove(item)
            shutil.rmtree(item, ignore_errors=True)
    
    def sub_pattern(self, patterns):
        pass
    
    def add_random_suffix(self, path_list):
        hex_suffix=self.get_random_hex_string(6)
        debug.t('hex', hex_suffix)
        res={}
        for item in path_list:
            abspath=os.path.join(self.target_dir, item)
            newpath=abspath+'_%s'%hex_suffix
            try:os.rename(abspath, newpath)
            except Exception,e:continue
    
    def get_random_hex_string(self, size):
        strHex='abcdef0123456'
        res=''
        num=len(strHex)
        while size>0:
            idx=(int(random.random()*num) % num)
            res += strHex[idx]
            size -= 1
        return res
    
    def del_files(self, pattern):
        dir_list=self.get_dirlist(self.target_dir)
        #for d in dir_list:debug.printraw(d)
        file_list=[]
        for d in dir_list:
            rv=self.get_filelist(d, pattern, True)
            for f in rv: debug.printraw(f)
            file_list += rv
        #
        for f in file_list:
            os.remove(f)

class ProcGoogleJs(DirFileUtils):
    def rep_googleapis(self):
        # https://ajax.googleapis.com/ajax/libs/jquery
        # http://ajax.googleapis.com/ajax/libs/jqueryui
        googleapis=['https?://ajax.googleapis.com/ajax/libs/jquery',
                    'https?://ajax.googleapis.com/ajax/libs/jqueryui']
        res=self.find_file('.*\.html$', '000.static')
        # 000.static_6f4106
        basedir_len=len(self.target_dir)
        for item in res:
            with open(item, 'r+') as f:
                rawdata=f.read(-1)
                '''lines=rawdata.split('\n')
                for line in lines:
                    for g in googleapis:
                        m=re.search(g, line)
                        if m:debug.t("m", '%s,%s'%(item, line))'''
                relPath=item[basedir_len+1:]
                if not relPath:continue
                dirNum=len(relPath.split('\\'))
                static_prefix='../'*dirNum+'000.static_6f4106/'
                
                find_replace=[
                    ['src="(https?://ajax.googleapis.com/ajax/libs/jquery/[\d.]+/jquery.min.js)"', 
                     'src="%sjquery-1.10.2/jquery-1.10.2.min.js"'%static_prefix], 
                              
                    ['src="(https?://ajax.googleapis.com/ajax/libs/jqueryui/[\d.]+/jquery-ui.min.js)"',
                     'src="%sjquery-ui-1.11.4/jquery-ui.min.js"'%static_prefix],
                              
                        ]
                '''
                find_pattern='src="(https?://ajax.googleapis.com/ajax/libs/jquery/[\d.]+/jquery.min.js)"'
                rep_pattern='src="%sjquery-1.10.2/jquery-1.10.2.min.js"'%static_prefix
                m=re.search(find_pattern, rawdata)
                new_data=rawdata
                need_write=False
                if m:
                    new_data=re.sub(find_pattern, rep_pattern, new_data)
                    #debug.t('file', item)
                    #debug.printraw(new_data)
                    need_write=True
                    
                #
                find_pattern='src="(https?://ajax.googleapis.com/ajax/libs/jqueryui/[\d.]+/jquery-ui.min.js)"'
                rep_pattern='src="%sjquery-ui-1.11.4/jquery-ui.min.js"'%static_prefix
                m=re.search(find_pattern, new_data)
                if m:
                    new_data=re.sub(find_pattern, rep_pattern, new_data)
                    #debug.t('file', item)
                    #debug.printraw(new_data)
                    need_write=True
                
                find_pattern='src="[./]*jquery-1.10.2/jquery-1.10.2.min.js"'
                rep_pattern='src="%sjquery-1.10.2/jquery-1.10.2.min.js"'%static_prefix
                m=re.search(find_pattern, new_data)
                if m:
                    new_data=re.sub(find_pattern, rep_pattern, new_data)
                    #debug.t('file', item)
                    #debug.printraw(new_data)
                    need_write=True
                        
                find_pattern='src="[./]*jquery-ui-1.11.4/jquery-ui.min.js"'
                rep_pattern='src="%sjquery-ui-1.11.4/jquery-ui.min.js"'%static_prefix
                m=re.search(find_pattern, new_data)
                if m:
                    new_data=re.sub(find_pattern, rep_pattern, new_data)
                    #debug.t('file', item)
                    #debug.printraw(new_data)
                    need_write=True
                        
                #break
                if need_write:
                    f.truncate(0)
                    f.seek(0,os.SEEK_SET)
                    f.write(new_data)
                    #debug.t('file', item)
                    #debug.printraw(new_data)'''


def procjscss(target_dir):
    proc_task=ProcGoogleJs(target_dir)
    #proc_task.rename_subdir()
    #proc_task.find_file("*.html")
    #res=proc_task.find_dir("jquery-ui", "000.static")
    #proc_task.del_dir(res)
    #res=proc_task.find_file("*.html", "000.static")
    #proc_task.rep_googleapis()
    #proc_task.add_random_suffix(['000.static'])
    proc_task.del_files('(^SICW\.|^SuperBackspace.em$)')

# ===============================================================
# 这个是把Java的实例代码从多个源目录改成三个源目录的过程。    
class ProcJavaCodeRepository(DirFileUtils):
       
    def testFunc1(self):
        debug.trace(["dir:", self.target_dir]) 
    def proc(self):
        dir_list=self.find_dir(r'fancy$', 'LibraryTest')
        debug.printraw(len(dir_list))
        move_to=self.target_dir+'/LibraryTest/org/fancy/'
        for d in dir_list:
            #subdir_list=self.find_dir('.')
            subdir_list=self.get_dirlist(d)
            for sub_dir in subdir_list:
                head,tail1=os.path.split(sub_dir)
                debug.printraw(sub_dir+','+move_to+tail1)
                #shutil.copytree(d, move_to+tail)
                os.mkdir(move_to+tail1)
                tmp_dir_list=self.get_dirlist(sub_dir)
                tmp_file_list=self.get_filelist(sub_dir)
                for tmp_d in tmp_dir_list:
                    head,tail2=os.path.split(tmp_d)
                    debug.printraw(tmp_d+','+move_to+tail1+"/"+tail2)
                    shutil.copytree(tmp_d, move_to+tail1+"/"+tail2)
                for tmp_f in tmp_file_list:
                    debug.printraw(tmp_f+','+move_to+tail1)
                    shutil.copy(tmp_f, move_to+tail1)
                    
def procJavaCodeRepository(target_dir):
    proc_task=ProcJavaCodeRepository(target_dir)
    #proc_tack.testFunc1()
    proc_task.proc()
    
# =================================================================
class CleanProject(DirFileUtils):

    def clean(self, desc):
        for k,v in desc.items():
            sub_dir=self.target_dir+'/'+k
            debug.trace(['subdir:', sub_dir])
            if 'dir' in v:
                dir_list=self.get_dirlist(sub_dir, v['dir'], True)
                for d in dir_list:
                    pass
                    debug.trace(['d:', d])
                    #shutil.rmtree(d, ignore_errors=True)
                    
            if 'file' in v:
                file_list=self.get_filelist(sub_dir, v['file'], True)
                for f in file_list:
                    pass
                    debug.trace(['f:', f])
                    #os.remove(f)
    
    def move_svn(self, desc):
        pass
        #dir_list=self.get_dirlist(d, pattern, r)
        svntemp=self.target_dir+'/'+desc.get('svntemp')
        
        for k in desc.get('sub_dirs'):
            sub_dir=self.target_dir+'/'+k
            debug.trace(['sub_dirs:', sub_dir])
            dir_list=self.get_dirlist(sub_dir, r'\\\.svn$', True)
            #for d in dir_list[0:1]:
            for d in dir_list:
                debug.trace(['svd_dir:', d, os.path.dirname(d)])   #basename
                dirtemp=uuid.uuid4().hex
                dirtemp=svntemp+'/'+dirtemp
                os.mkdir(dirtemp)
                with open(os.path.join(svntemp, 'svn_desc.txt'), 'w') as fo :
                    fo.write(d+','+dirtemp)
                shutil.move(d, dirtemp)
                
    def start(self):
        if False:
            self.move_svn({
                "svntemp":'SVNTemp',
                'sub_dirs':['Python']
            })
        #return 
        #
        desc={
              'Java': {'dir':r'\\bin$'} ,
              'Python':{'file':r'\.pyc$'},
              #'VS2012':{'dir':r'\\Debug$|\\Release$|\\ipch$', 'file':r'\.sdf$'},
              #'NRF51822':{'dir':r'\\_build$'},
              #'STM32F429':{'dir':r'\\Exe$|\\List$|\\Obj$'},
              #'ADT':{'dir':r'\\bin$|\\gen$'},
              #'Android':{'dir':r'\\build$'}
              }
        self.clean(desc)
        
        #self.clean_java()
        #self.clean_vs2012()
        #self.clean_python()
        
def clean_project(target_dir):
    clean=CleanProject(target_dir)
    clean.start()

# ***************************************************************************
class UrlforProc(DirFileUtils):
    def replace(self, desc):
        pass
        print self.target_dir
    
    def start(self):
        desc=[]
        self.replace(desc)
    
def urlfor_proc(target_dir):
    proc=UrlforProc(target_dir)
    proc.start()
    
# **************************************************************************
class ResumeViewer(DirFileUtils):
    def parse_msg(self, msg):
        info={}
        #print msg
        if re.search('Android开发工程师', msg):
            info['职位']='Android'
            #print 'position: Android'
        elif re.search('软件测试工程师', msg):
            info['职位']='软件测试'
            #print 'position: Android'
        elif re.search('嵌入式软件工程师', msg):
            info['职位']='嵌入式'
            #print 'position: Android'
        elif re.search('系统软件工程师', msg):
            info['职位']='系统软件'
        elif re.search('Web后端工程师', msg):
            info['职位']='Web后端'
        elif re.search('Web前端工程师', msg):
            info['职位']='Web前端'
        elif re.search('Python开发工程师', msg):
            info['职位']='Python开发'        
        else:
            info['职位']='未知'
            
        with open(msg, 'rb') as fo:
            data=fo.read(-1)
            #print len(data)
            m=re.search('<html xmlns="http://www.w3.org/1999/xhtml">([\s\S]*)</html>', data)
            #print m
            if m:
                #print m.group(1)
                strhtml='<html>'+m.group(1)+'</html>'
                strhtml=strhtml.replace('\n', '')
                #print strhtml
                # 搜索姓名
                soup=BeautifulSoup(strhtml, 'html.parser', from_encoding='gbk')
                #print soup.original_encoding
                wrap_tag=soup.body.table.tbody.tr.td
                tbl_list=[]
                #for t in a.children:
                #    tbl_list.append(t)
                #print len(tbl_list)
                #t=dir(a)
                #for k in dir(a):print k
                #b=a.findChild('table')
                #print len(b)
                #print wrap_tag.name
                #print a.table,type(a.table),a.table.strings
                #c=a.table.encode_contents()
                #print type(c)
                #print c.decode('utf8').encode('gbk')
                #print len(wrap_tag.contents)
                
                # *************************************************
                personinfo=wrap_tag.contents[0].tbody.tr.contents[1].table.tbody.tr.td
                #print personinfo.name
                #for s in personinfo.strings:print s
                name_tag=personinfo.strong
                #print name_tag.string
                txt=personinfo.encode('gbk')
                txt=re.sub('<td [^>]*>', '', txt)
                txt=re.sub('<strong [^>]*>', '', txt)
                txt=re.sub('</strong>', '', txt)
                txt=re.sub('</td>', '', txt)
                txt=re.sub('&#160;\|&#160;', ',', txt)
                #print txt
                xm_jy =txt.split(',')
                xm_jy=map(lambda x:x.strip(), xm_jy)
                #print xm_jy
                info['姓名'],info['性别'],info['年龄'],info['工作经验']=xm_jy[:]
                
                #print type(personinfo.text)
                #for c in personinfo.text:print c
                #print personinfo.get_text().encode('gbk')
                #print type(txt),txt.encode('gbk')
                
                
                # xueli *******************************************
                xueli_tbl=wrap_tag.contents[1].tbody.tr.td.table.tbody.tr.contents[1]
                xueli_info_tags=xueli_tbl.table.tbody.contents[1:4]
                
                #zhuanye,xuexiao,xueli=xueli_tbl.table.tbody.contents[0:3]
                #print xueli.contents[0].name
                #xuexiao=xueli.contents[1]
                #print xuexiao.string
                key_list=['专业', '学校', '学历']
                #for ct in xueli_info_tags:
                for i in xrange(3):
                    ct=xueli_info_tags[i]
                    #print ct.name
                    #key=ct.contents[0].string
                    val=ct.contents[1].get_text().encode('gbk')
                    #print val
                    info[key_list[i]]=val
                    #print key,val
            #for k,v in info.items():print k,v
        return info
        
    def parse_email_msg(self, filelist):
        res=[]
        num=len(filelist)
        count=0
        #num=10
        for item in filelist:
            count += 1
            #print item
            try:
                res.append(self.parse_msg(item))
            except Exception,e:
                print 'parse error', item
                #continue
            
            #try:
            #    res.append(self.parse_msg(item))
            #except Exception,e:
            #    print 'parse error', item
            #    continue
            if num==count:break
            pass
        return res
    
    def start(self, out_file='resumes.txt'):
        print 'start viewer'
        filelist=self.get_filelist(self.target_dir)
        #print filelist[0:10]
        #for k in filelist[0:10]:print k
        rv=self.parse_email_msg(filelist)
        #print len(rv)
        #print rv[0]
        #for k,v in rv[0].items():print k,v
        #for k,v in rv[0].items():print k,v,type(k),type(v)
        #with open('resumes.txt', 'w') as fres:
        with open(out_file, 'w') as fres:
            data=map(lambda x: ','.join([x.get('姓名'), x.get('性别'), x.get('年龄'), x.get('工作经验'), 
                                x.get('学校'), x.get('学历'), x.get('专业'), x.get('职位')]),  rv)
            
            #print data[0]
            fres.write('\n'.join(data))

def start_resume_viewer(target_dir, out_file='resumes.txt'):
    viewer=ResumeViewer(target_dir)
    viewer.start(out_file)

def find_big_files(target_dir, out_file='big_files.txt'):
    du=DirFileUtils(target_dir)
    filenames=du.get_filelist(du.target_dir, r=True)
    print 'filenames size:', len(filenames), filenames[0], os.path.getsize(filenames[0])
    rv=map(lambda x:[x, os.path.getsize(x)], filenames)
    rv.sort(key=lambda x:x[1], reverse=True)
    #print 'big files:', rv[0:50]
    for x in rv[0:50]:print 'big files:', x[1]/1024.0, x[0] 
    
    
        
    
# @note zhoufan
# 命令行参数 target_dir pattern find replace 
# pattern用分号隔开。
if __name__ == "__main__":
    arg_size = len(sys.argv)
    if arg_size<2:
        print "[Usage]:target_dir pattern find replace "
        sys.exit(0)
    #
    target_dir = sys.argv[1]
    out_file = sys.argv[2]
    #procjscss(target_dir)
    #procJavaCodeRepository(target_dir)
    #clean_project(target_dir)
    #urlfor_proc(target_dir)
    #start_resume_viewer(target_dir, out_file)
    find_big_files(target_dir, out_file)


