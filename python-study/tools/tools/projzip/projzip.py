#encoding=gbk

import sys
import os
import fnmatch
import traceback
import re
import shutil
import random
import datetime
#from bs4 import BeautifulSoup
import uuid
import ConfigParser

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
    def __init__(self, target_dir=None):
        if target_dir:self.target_dir=target_dir
    
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


# =================================================================
class ProjZip(DirFileUtils):

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
    
    def move_file(self, desc, action=False):
        pass
        #dir_list=self.get_dirlist(d, pattern, r)
        #svntemp=desc.get('svntemp')
        dt=datetime.datetime.now()
        svntemp=dt.strftime('%Y%m%d%H%M%S')
        self.tempdir=svntemp
        move_info=[]
        for item in desc.get('move_dirs'):
            k,v=item[:]
            sub_dir=self.target_dir+'/'+k
            debug.trace(['sub_dirs:', sub_dir])
            dir_list=self.get_dirlist(sub_dir, v, True)
            #for d in dir_list[0:1]:
            for src_dir in dir_list:
                #debug.trace(['svd_dir:', d, os.path.dirname(d)])   #basename
                #dirtemp=uuid.uuid4().hex
                dest_dir=svntemp+'/'+''.join(random.sample('0123456789ABCDEF', 16))
                os.makedirs(dest_dir)
                print 'from,to:1:', src_dir, dest_dir
                move_info.append([src_dir, dest_dir])
                
        with open(os.path.join(svntemp, 'db.txt'), 'w') as fo :
            fo.write('\n'.join(map(lambda x:','.join(x), move_info)))
        if not move_info:return
        num=len(move_info)
        #for i in xrange(1):
        for i in xrange(num):
            src_dir,dest_dir=move_info[i][:]
            print 'move from_to:', src_dir, dest_dir
            if action:shutil.move(src_dir, dest_dir)
    
    def do_move_file(self):
        self.move_file({
                #"svntemp":'SVNTemp',
                'move_dirs':[
                             ['NRF51822', r'\\\.svn$|\\_build$'],
                             #['Python', r'\\\.svn$'],
                             #['VS2012', r'\\Debug$|\\Release$|\\ipch$' ],
                             ]
            }) 
           
    def start(self):
        self.do_move_file()
        return 
    
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
    
    def back(self, tempdir, action=False):
        move_info=[]
        with open(tempdir+'/db.txt', 'r') as fo:
            lines=fo.readlines()
            for line in lines:
                #print 'line:', line
                move_info.append(map(lambda x:x.strip(), line.split(',')))
        for item in move_info:
            #print 'item:', item
            src_path,dest_path=item[:]
            #print 'basename:', os.path.basename(src_path), os.path.dirname(src_path)
            src_dir=os.path.dirname(src_path)
            src_base=os.path.basename(src_path)
            back_src=os.path.join(dest_path, src_base)
            back_dest=src_dir
            print 'back:', back_src, back_dest
            if action:shutil.move(back_src, back_dest)

        
def proj_zip():
    #clean=CleanProject()
    #clean.start()
    cf=ConfigParser.ConfigParser()
    cfpath=sys.argv[1]
    mode=sys.argv[2]
    
    # 保存模式和复原模式。
    if mode=='save':
        cf.read(cfpath)
        base_dir=cf.get('common', 'base_dir')
        action=cf.get('common', 'action')=='1'
        print 'base_dir:', base_dir, action
        if action:print 'action is True'
        # Project zip 
        if 'output' not in cf.sections():
            cf.add_section('output')
        # 
        #tempdir=cf.get('output', 'tempdir')
        #print 'tempdir:1:', tempdir
        #if not tempdir:
        print 'output options:', cf.options('output')
        if 'tempdir' not in cf.options('output'):
            pz = ProjZip(base_dir)
            #pz.start()
            pz.move_file({
                    #"svntemp":'SVNTemp',
                    'move_dirs':[
                                 ['NRF51822', r'\\\.svn$|\\_build$'],
                                 #['Python', r'\\\.svn$'],
                                 #['VS2012', r'\\Debug$|\\Release$|\\ipch$' ],
                                 ]
                }, action) 
            cf.set('output', 'tempdir', pz.tempdir)
            cf.write(open(cfpath, 'w'))
    elif mode=='back':
        cf.read(cfpath)
        base_dir=cf.get('common', 'base_dir')
        action=cf.get('common', 'action')=='1'
        print 'base_dir:', base_dir, action
        # Project zip 
        pz = ProjZip(base_dir)
        #tempdir=cf.get('output', 'tempdir')
        #print 'tempdir:', tempdir
        #if tempdir:
        print 'output options:', cf.options('output')
        if 'tempdir' in cf.options('output'):
            pz.back(cf.get('output', 'tempdir'), action)
        cf.remove_option('output', 'tempdir')
        cf.write(open(cfpath, 'w'))
        
        
    
# @note zhoufan
# 命令行参数 target_dir pattern find replace 
# pattern用分号隔开。
if __name__ == "__main__":
    arg_size = len(sys.argv)
    if arg_size<3:
        print "[Usage]:need a config file and mode arg"
        sys.exit(0)
    proj_zip()


