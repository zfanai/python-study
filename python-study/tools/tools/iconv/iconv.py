#encoding=gbk

import sys
import os
import fnmatch
import traceback
import chardet
import re

def trace(obj):
    print "trace:", obj
class Debug(object):
    def trace(self, obj):
        print "trace:%s" % obj
    # @note python 不支持重载.
    def t(self, tag, msg):
        print "trace:%s,%s" % (tag, msg)
    def printraw(self, obj):
        print obj
debug=Debug()

def iconvFile(filename):
    pass
    trace(["_find_replace"])
    try:
        fo=open(filename, "r+")
        buf=fo.read(-1)
        trace(["buf size:", len(buf)])
        #
        #trace(["find,replace:", ord(find), ord(replace)])
        #for item in findReplace:
        #    find,replace=item[0:2]
        #    buf2=buf.replace(find, replace)
        #    buf=buf2
        buf2=buf.decode("gbk").encode('utf8')
        
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

def iconvDir(target_dir, patterns, single_level=False):
    trace(["target_dir:", target_dir])
    patterns = patterns.split(';')
    
    # 目录名称
    #print "dirname:",os.path.dirname(target_dir)
    #print "basename:",os.path.basename(target_dir)
    dirname = os.path.dirname(target_dir)
    pos=len(dirname)
    
    #print os.path.exists(target_dir)
    if not os.path.exists(target_dir):
        print "dir dose not exist"
        raise Exception
    
    
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
                    trace(["abspath:", abspath])
                    #
                    iconvFile(abspath)
            #
            #break
        
        if single_level:
            break    

class ProcIconv(object):
    def __init__(self, target_dir):
        self.target_dir=target_dir
    
    def get_filelist(self, d, pattern, r):
        pattern = pattern.split(';')
        filelist=[]
        #debug.t("get_filelist", d)
        for path, subdirs, files in os.walk(d):
            #debug.t("files:", files)
            for name in files:
                for p in pattern:
                    if fnmatch.fnmatch(name, p.strip()): # 去除pattern两端的空格
                        abspath = os.path.join(path, name)
                        #trace(["abspath:", abspath])
                        filelist.append(abspath)
            if not r:break
        return filelist
    
    def to_gbk(self, pattern):
        file_list=self.get_filelist(self.target_dir, pattern, True)
        
        for f in file_list:
            #debug.t("f", f)
            with open(f, 'r+') as fo:
                rawdata=fo.read(-1)
                
                enc_res=chardet.detect(rawdata)
                new_data=rawdata
                lines=rawdata.split('\n')
                #if len(lines)>2:lines=lines[0:2]
                #debug.t("lines", lines)
                
                declare_change=self.change_enc_declare(lines, 'gbk')
                if declare_change:debug.t("f", f)
                
                # 如果文件编码是utf-8， 转换成gbk, 并且声明也要改成GBK
                # 声明都需要改成GBK。
                if enc_res['encoding']=='utf-8':
                    #new_data=rawdata.decode('utf-8')
                    #self.change_enc_declare(lines, 'gbk')
                    #for i in range(len(lines)):
                    new_data='\n'.join(lines)
                    new_data=new_data.decode('utf-8').encode('gbk')
                    #
                    #debug.printraw(new_data)
                    fo.truncate(0)
                    fo.seek(0, os.SEEK_SET)
                    fo.write(new_data)
                    break
                    
                # 文件编码是GB2312的，要检查编码声明是否正确。
                #elif enc_res['encoding']=='GB2312':
                #    pass
                    #self.change_enc_declare(lines, 'gbk')
                #m=re.search('\n?#.*(utf8|utf-8|gbk)', rawdata)
                #if m:debug.t("f", [f, chardet.detect(rawdata), m.group(1)])
                
                '''if enc_res['encoding']=='utf-8':
                    #debug.t("f", [f, chardet.detect(rawdata)])
                    m=re.search('^#.*(utf8|utf-8)', rawdata)
                    #if m:debug.t('m', m.group())'''
               
    def check_enc_declare(self):
        file_list=self.get_filelist(self.target_dir, "*.py", True)
        
        for f in file_list:
            #debug.t("f", f)
            with open(f, 'r+') as fo:
                rawdata=fo.read(-1)
                enc_res=chardet.detect(rawdata)
                #new_data=rawdata
                lines=rawdata.split('\n')
                enc_decl=self.get_enc_declare(lines)
                
                enc_use=enc_res['encoding']
                #debug.t("f", [f, enc_decl, enc_use])
                if (enc_use=='utf-8' and (enc_decl not in ('utf8', 'utf-8'))) or \
                    (enc_use=='GB2312' and (enc_decl not in ('gbk'))):
                    debug.t("f", [f, enc_decl, enc_use])
                    self.set_enc_declare(lines, enc_use)
                    new_data='\n'.join(lines)
                    #new_data=new_data.decode('utf-8').encode('gbk')
                    #
                    #debug.printraw(new_data)
                    fo.truncate(0)
                    fo.seek(0, os.SEEK_SET)
                    fo.write(new_data)
                    
                #if len(lines)>2:lines=lines[0:2]
                #debug.t("lines", lines)
                
                #declare_change=self.change_enc_declare(lines, 'gbk')
                #if declare_change:debug.t("f", f)
    
    def change_enc_declare(self, lines, enc):
        change=False
        for i in range(2):
            line=lines[i]
            m=re.match('#.*(utf8|utf-8|gbk)', line)
            if m:
                debug.t('line', [line, m.group(1), enc])
                cur_enc=m.group(1)
                if enc=='gbk' and cur_enc in ['utf8', 'utf-8']:
                    rv=re.sub('#(.*)(utf8|utf-8|gbk)', '#\\1gbk', line)
                    debug.t('rv', rv)
                    lines[i]=rv
                    change=True
                break
        return change
    
    def set_enc_declare(self, lines, enc):
        for i in range(2):
            line=lines[i]
            m=re.match('#.*(utf8|utf-8|gbk)', line)
            if m:
                debug.t('line', [line, m.group(1), enc])
                cur_enc=m.group(1)
                #if enc=='gbk' and cur_enc in ['utf8', 'utf-8']:
                rv=re.sub('#(.*)(utf8|utf-8|gbk)', '#\\1%s'%enc, line)
                debug.t('rv', rv)
                lines[i]=rv
                break
    
    def get_enc_declare(self, lines):
        for i in range(2):
            line=lines[i]
            m=re.match('#.*(utf8|utf-8|gbk)', line)
            if m:
                #debug.t('line', [line, m.group(1), enc])
                cur_enc=m.group(1)
                return cur_enc
    
def proc_iconv(target_dir):
    proc_task=ProcIconv(target_dir)
    #proc_task.to_gbk("*.py")
    proc_task.check_enc_declare()
        
            
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
    proc_iconv(target_dir)
    #iconvDir(target_dir, "*.java")

